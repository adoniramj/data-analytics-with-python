#!/usr/bin/env python3

import os

THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_DIRECTORY, "a_poem.txt")

file_data = open(file, "r").read()

print(file_data)