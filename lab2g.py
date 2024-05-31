#!/usr/bin/env python3

# Author:Tirth Amitkumar Shah
# Author ID:175983212
# Date Created:2024/05/30

import sys

# Check if command line arguments were provided
if len(sys.argv) > 1:
    # If an argument was provided, use it as the timer value
    timer = int(sys.argv[1])
else:
    # If no argument was provided, default the timer to 3
    timer = 3

# While loop that repeats until (and not including when) timer equals 0
while timer > 0:
    print(timer)
    timer -= 1

# Print the final message when the timer reaches 0
print("blast off!")

