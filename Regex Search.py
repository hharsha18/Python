print("Name   : Harsha D S")
print("USN    : 1AY24AI041")
print("Section : M")

import os, re

pattern = input("Enter a regex pattern: ")
regex = re.compile(pattern)

for filename in os.listdir():
    if filename.endswith('.txt'):                                                                                             
        with open(filename) as f:
            for line in f:
                if regex.search(line):
                    print(f"{filename}: {line.strip()}")         
