#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
from shutil import copy
from zipfile import ZipFile
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "not nate"


# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    arr = []
    for filename in os.listdir(dir):
        r = re.search(".*__.*__.*", filename)
        if r:
            arr.append(dir + "/" + filename)
    return arr

def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for path in paths:
        copy(path, dir+"/")

def zip_to(paths, zippath):
    with ZipFile(zippath+".zip", 'w') as myzip:
        for path in paths:
            myzip.write(path)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--from_dir', help='src dir for special files', default=os.getcwd())

    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit(1)

    special_paths = get_special_paths(args.from_dir)
    if args.todir:
        copy_to(special_paths, args.todir)
    if args.tozip:
        zip_to(special_paths, args.tozip)
    if not args.tozip and not args.todir:
        print("nothing done with :", special_paths)


    # +++your code here+++



if __name__ == "__main__":
    main()
