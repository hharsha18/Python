print("Name   : Harsha D S")
print("USN    : 1AY24AI041")
print("Section : M")
import re

with open('madlib_input.txt') as file:
    content = file.read()

placeholders = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', content)
for word in placeholders:
    replacement = input(f"Enter a {word.lower()}: ")
    content = content.replace(word, replacement, 1)

print("\nGenerated Text:\n", content)

with open('madlib_output.txt', 'w') as file:
    file.write(content)
