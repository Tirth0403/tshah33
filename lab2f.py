#!/usr/bin/env python3

# Author: Tirth Amitkumar Shah
# Author ID: 175983212
# Date Created: 2024/05/30

import sys

# Assign the value of the first command line argument to the timer object
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <timer>")
    sys.exit(1)

try:
    timer = int(sys.argv[1])
except ValueError:
    print(f"Error: {sys.argv[1]} is not a valid number")
    sys.exit(1)

# While loop that repeats until timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message when the timer reaches 0
print("blast off!")

