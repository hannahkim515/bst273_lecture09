#!/usr/bin/env python

import argparse
#Another way: import system
#Another way: file = sys.argv[1]

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )
print("args.data_file =",args.data_file)

fh = open(args.data_file)
print("the file handle is",fh)

lines = 0
words = 0
chars = 0

for line in fh:
	print(line)
	


#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
