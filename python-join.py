#!/usr/bin/env python3

import sys
import os.path
import argparse

def get_arguments():
  # Accept command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("left_file", help="name of file to be used as left file in key join")
  parser.add_argument("right_file", help="name of file to be used as right file in key join")
  parser.add_argument("--left-key", help="index to use as key in left file", type=int)
  parser.add_argument("--right-key", help="index to use as key in right file", type=int)
  args = parser.parse_args()

  # Check that first two positional arguments are indeed files
  if os.path.isfile(args.left_file) and os.path.isfile(args.right_file):
    left_file = args.left_file
    right_file = args.right_file
  else:
    sys.stderr.write("Input files not found.\n")

  # Check for optional arguments and set indexes accordingly
  if args.left_key:
    left_index = args.left_key - 1
  else:
    left_index = 0
  print("left_index: "+str(left_index))

  if args.right_key:
    right_index = args.right_key - 1
  else:
    right_index = 0
  print("right_index: "+str(right_index))

  return left_file, right_file, left_index, right_index  

def get_left_keys(infile, key_index):
  left_keys = []
  return left_keys  

def get_joint_keys(key_list, key_index, infile):
  joint_keys = []
  return joint_keys

def main(): 
  left_file, right_file, left_index, right_index = get_arguments()
  left_keys = get_left_keys(left_file, left_index)
  joint_keys = get_joint_keys(left_keys, right_index, right_file)

if __name__ == "__main__":
  main()
