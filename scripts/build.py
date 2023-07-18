#!/usr/bin/python3
import argparse
import subprocess
import os

DESCRIPTION = "Helper script to build and format code in a cpp repository"

SCRIPT_DIR = os.path.dirname(__file__)
BUILD_DIR = f'{SCRIPT_DIR}/../build'
SRC_DIR = f'{SCRIPT_DIR}/..'

def run(cmd, dryrun):
    if(dryrun):
        print(cmd)
        return

    ret = subprocess.run(cmd, shell=True)
    if(ret.returncode != 0):
        print("error") # TODO: add error handler

def format_repo(dryrun):
    '''
    Runs clag-format one all *.cpp and *.h files in ../
    '''
    cmd = f'find {SRC_DIR} -iname *.h -o -iname *.cpp | xargs clang-format -i'
    run(cmd, dryrun)
    

def cmake(dryrun):
    cmd = f'cmake -B {BUILD_DIR} -S {SRC_DIR}'
    run(cmd, dryrun)

def build_application(dryrun):
    cmd = f'cmake --build {BUILD_DIR}'
    run(cmd, dryrun)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-d', '--dryrun', action='store_true')
    parser.add_argument('-c', '--cmake', action='store_true', help='Run cmake')
    parser.add_argument('-b', '--build', action='store_true', help='Build the project')
    parser.add_argument('-f', '--format', action='store_true', help='Run clamg-format on all *.cpp and *.h files in the repository.')
    args = parser.parse_args()
    
    if(args.format):
        format_repo(args.dryrun)
    
    if(args.cmake):
        cmake(args.dryrun)

    if(args.build):
        build_application(args.dryrun)

