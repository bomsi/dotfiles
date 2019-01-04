#!/usr/bin/env python3

import os
import hashlib
from sys import argv
from os.path import join, getsize

srcfilename = join(os.getcwd(), argv[1])
dstfilename = join(argv[2], argv[1])
srcfilesize = getsize(srcfilename)

print('[i] source file ' + srcfilename + ' (' + str(srcfilesize) + ' B)')
print('[i] destination file ' + dstfilename)
confirmation = input('[?] Begin copy operation? (N/y) ')

if confirmation != 'y':
    print('[i] operation canceled')
    exit()

try:
    hasher = hashlib.sha256()
    with open(srcfilename, 'rb') as srcfile:
        with open(dstfilename, 'wb') as dstfile:
            print('[i] started copying')
            for chunk in iter(lambda: srcfile.read(4096), b""):
                hasher.update(chunk)
                dstfile.write(chunk)
    srcfilehash = hasher.hexdigest()
    print('[i] source file SHA256: ' + srcfilehash)
    if getsize(dstfilename) != srcfilesize:
        print('[-] operation failed, file sizes do not match')
        exit()
    hasher = hashlib.sha256()
    with open(dstfilename, 'rb') as dstfile:
        for chunk in iter(lambda: dstfile.read(4096), b""):
            hasher.update(chunk)
    dstfilehash = hasher.hexdigest()
    print('[i] destination file SHA256: ' + dstfilehash)
    if srcfilehash == dstfilehash:
        print('[+] operation completed successfully')
    else:
        print('[-] operation failed, file hashes do not match')
except PermissionError:
    print('[-] could not copy due to permissions')
except OSError:
    print('[-] could not copy due to OS error')


