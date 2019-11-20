#!/usr/bin/env python

# This script was copied and pasted from @rvaser (Robert Vaser) from his comment in an issue for racon.
# His original words can be found at https://github.com/isovic/racon/issues/68 
# Essentially, it takes paired-end Illumina data, and interleaves the fastqs and changes the names to be unique.
# This is from a version on May 3, 2018

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def parse_file(file_name, read_set):
    line_id = 0
    name = ''
    data = ''
    qual = ''
    valid = False
    with (open(file_name)) as f:
        for line in f:
            if (line_id == 0):
                if (valid):
                    if (len(name) == 0 or len(data) == 0 or len(data) != len(qual)):
                        eprint('File is not in FASTQ format')
                        sys.exit(1)
                    valid = False
                    if (name in read_set):
                        print(name + '2')
                    else:
                        read_set.add(name)
                        print(name + '1')
                    print(data)
                    print('+')
                    print(qual)
                name = line.rstrip().split(' ')[0]
                data = ''
                qual = ''
                line_id = 1
            elif (line_id == 1):
                if (line[0] == '+'):
                    line_id = 2
                else:
                    data += line.rstrip()
            elif (line_id == 2):
                qual += line.rstrip()
                if (len(qual) >= len(data)):
                    valid = True
                    line_id = 0

    if (valid):
        if (len(name) == 0 or len(data) == 0 or len(data) != len(qual)):
            eprint(len(name), len(data), len(qual))
            eprint('File is not in FASTQ format')
            sys.exit(1)
        if (name in read_set):
           print(name + '2')
        else:
           read_set.add(name)
           print(name + '1')
        print(data)
        print('+')
        print(qual)

if __name__ == '__main__':

    read_set = set()

    if (len(sys.argv) > 1):
        parse_file(sys.argv[1], read_set)
    if (len(sys.argv) > 2):
        parse_file(sys.argv[2], read_set)
