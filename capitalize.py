#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    capitalized_words = [w.capitalize() for w in words]
    return " ".join(capitalized_words)

if __name__ == '__main__':
