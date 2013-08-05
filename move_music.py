#!/usr/bin/env python

import os
import sys
import time
import glob
import string
import shutil
import datetime
import tempfile
import fnmatch

# GLOBALS
arg_version = ""

folder_seperator = os.sep
root_code_path = os.path.dirname(os.path.abspath(__file__))
code_file_path = root_code_path + folder_seperator + "Outlook Scheduler"
res_file_path = code_file_path + folder_seperator + "Properties"

csproj_file_name = "Outlook Scheduler.csproj"
csver_file_name = "AssemblyInfo.cs"
msft_build_evn = "C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\Common7\\Tools\\VsDevCmd.bat"


def now():
    return datetime.datetime.now().strftime("%A-%b-%d-%Y-%H:%M:%S")

def log(str):
    print "[%s][%s] %s" % ("client",now(),str)
    sys.stdout.flush()

def error(str):
    print "[%s][%s][error] %s" % ("client",now(),str)
    sys.stdout.flush()

def print_usage():
    log( "usage: %s <version> <relnum>" % sys.argv[0] )

def run_command(cmd):

    if not cmd:
        return

    pipe = os.popen(cmd + ' 2>&1','r')

    text = pipe.read()
    sts = pipe.close()

    if sts is None:
        sts = 0
    if text[-1:] == '\n':
        text = text[:-1]

    return sts,text
	
def parse_dirs():
    # replace the temp cert information in the VSTO ClickOnce settings
    # with the ecovate code signing cert
    for root, dirnames, filenames in os.walk("test"):
        for dirname in dirnames:
            log("dirname %s" % dirname)
            art, album = dirname.split(" ")
            log("artist is - %s ....  album is - %s" % (art,album))
            full_path = root + folder_seperator + art + folder_seperator + album
            log("path is %s" % full_path)
            if not os.path.exists(full_path):
                # dir doesn't exists so create it and move all the content
                log("moving - %s ....  to - %s" % (root+folder_seperator+dirname, full_path))
                shutil.move(root+folder_seperator+dirname, full_path)

parse_dirs()
