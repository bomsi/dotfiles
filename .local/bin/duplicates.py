#!/usr/bin/env python3

import os
import hashlib
from os.path import join, getsize
from collections import Counter, defaultdict

rootdir = os.getcwd()
print('[i] using ' + rootdir + ' as root directory')

files = []

for dirpath, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        currentfilename = join(dirpath, filename)
        try:
            currentfilesize = getsize(currentfilename)
            if currentfilesize != 0:
                filewithsize = currentfilename, currentfilesize
                files.append(filewithsize)
        except FileNotFoundError:
            print('[-] could not get ' + currentfilename + 'file size')

print('[i] sorting ' + str(len(files)) + ' files by size')
files.sort(key = lambda t: t[1])

print('[i] removing unique files by size')
counter = Counter(t[1] for t in files)
files = [t for t in files if counter[t[1]] > 1]

print('[i] hashing remaining ' + str(len(files)) + ' files')
duplicates = defaultdict(list)

for filename in files:
    if filename[1] > 102400000:
        print('[i] hashing large file: ' + filename[0])
    hasher = hashlib.sha256()
    try:
        with open(filename[0], 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)
        duplicates[hasher.hexdigest()].append(filename[0])
    except PermissionError:
        print('[-] could not hash ' + filename[0] + ' due to permissions')
    except OSError:
        print('[-] could not hash ' + filename[0] + ' due to OS error')

for candidate in duplicates.items():
    if len(candidate[1]) > 1:
        print('[+] duplicates with hash ' + candidate[0] + ':')
        for duplicate in candidate[1]:
            print(duplicate)