#!/usr/bin/env python3

import os
import hashlib
from sys import stdout
from os.path import join, getsize
from collections import Counter, defaultdict

rootdir = os.getcwd()
print('[i] using ' + rootdir + ' as root directory')
stdout.flush()

files = []

# XXX in case you have circular symlinks, we'll loop forever
for dirpath, dirnames, filenames in os.walk(rootdir, followlinks=True):
    for filename in filenames:
        currentfilename = join(dirpath, filename)
        try:
            currentfilesize = getsize(currentfilename)
            if currentfilesize != 0:
                filewithsize = currentfilename, currentfilesize
                files.append(filewithsize)
        except FileNotFoundError:
            print('[-] could not get ' + currentfilename + ' file size')
            stdout.flush()

print('[i] sorting ' + str(len(files)) + ' files by size')
stdout.flush()
files.sort(key = lambda t: t[1], reverse=True)

print('[i] removing unique files by size')
stdout.flush()
counter = Counter(t[1] for t in files)
files = [t for t in files if counter[t[1]] > 1]

print('[i] hashing remaining ' + str(len(files)) + ' files')
stdout.flush()
duplicates = defaultdict(list)

for f in files:
    if f[1] > 102400000:
        print('[i] hashing large file: ' + f[0])
        stdout.flush()
    hasher = hashlib.sha256()
    try:
        with open(f[0], 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)
        duplicates[hasher.hexdigest()].append(f)
    except PermissionError:
        print('[-] could not hash ' + f[0] + ' due to permissions')
        stdout.flush()
    except OSError:
        print('[-] could not hash ' + f[0] + ' due to OS error')
        stdout.flush()

for candidate in duplicates.items():
    if len(candidate[1]) > 1:
        print('[+] duplicates with hash ' + candidate[0] + ':')
        for duplicate in candidate[1]:
            print(duplicate[0] + ' (' + str(duplicate[1]) + ' bytes)')
            stdout.flush()
