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

  if args.right_key:
    right_index = args.right_key - 1
  else:
    right_index = 0

  return left_file, right_file, left_index, right_index  

def get_keys(infile, key_index):
  keys = []
  with open(infile) as f:
    for line in f:
      clean_line = line.rstrip('\n')
      line_list = clean_line.split(" ")
      keys.append(line_list[key_index])
  return keys

def get_joint_keys(comparison_key_list, infile, key_index):
  joint_keys = []
  with open(infile) as f:
    for line in f:
      clean_line = line.rstrip('\n')
      line_list = clean_line.split(" ")
      if line_list[key_index] in comparison_key_list:
        joint_keys.append(line_list[key_index])
  return joint_keys

def get_left_and_joint_output(left_file, right_file, left_index, right_index, joint_keys):
  with open(left_file) as lf:
    for line in lf:
      clean_line = line.rstrip('\n')
      line_list = clean_line.split(" ")
      key = line_list.pop(left_index)
      out = []
      out.append(key)
      for item in line_list:
        out.append(item)
      if key in joint_keys:
        with open(right_file) as rf:
          for right_line in rf:
            right_clean_line = right_line.rstrip('\n')
            right_line_list = right_clean_line.split(" ")
            if right_line_list[right_index] == key:
              right_line_list.pop(right_index)
              for right_item in right_line_list:
                out.append(right_item)
      print(out)

def get_right_output(right_file, right_index, joint_keys): 
  with open(right_file) as f:
    for line in f:
      clean_line = line.rstrip('\n')
      line_list = clean_line.split(" ")
      key = line_list.pop(right_index)
      if key not in joint_keys:
        out = []
        out.append(key)
        for item in line_list:
          out.append(item)
        print(out)


def main(): 
  left_file, right_file, left_index, right_index = get_arguments()
  left_keys = get_keys(left_file, left_index)
  joint_keys = get_joint_keys(left_keys, right_file, right_index)

  get_left_and_joint_output(left_file, right_file, left_index, right_index, joint_keys)
  get_right_output(right_file, right_index, joint_keys)

if __name__ == "__main__":
  main()
