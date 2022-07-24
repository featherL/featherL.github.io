#!python3

from os import path
import os
import sys

def rename(prev, files):
	for file in files:
		dir_name, name = path.split(file)
		name = prev+name
		final_path = path.join(dir_name, name)
		print('%s -> %s' % (file, final_path) )
		os.rename(file, final_path)


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Usage: python %s prev filename1 [filename2 filename3 ..]' % sys.argv[0])
		sys.exit(0)
	prev = sys.argv[1]
	files = sys.argv[2:]
	rename(prev, files)