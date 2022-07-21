#!/usr/bin/env python

# Author : Claudéric DeRoy
# goal : this is the script to automate, facilitate and open as much as possible
#        Xanthy Lajoie's seed to voxel correlation code so that it could be
#        easily re-use by anybody no matter what their experience with computer.
# Last date of modification : 21 jully 2022

from argparse import ArgumentParser
import json
import seed_voxel

def main():
    description = "this is a script that read a .txt file containing all the \
      argument to use in Xanthy's seed to voxel correlation."

    parser = ArgumentParser(__file__, description)
    parser.add_argument("--batch", help="input the directory to the .txt file")

    args = parser.parse_args()

    with open(args.batch) as f:
        batch = json.load(f)

    print(batch)

    

    
if __name__ == "__main__":
    main()
    
