print("Name   : Harsha D S")
print("USN    : 1AY24AI041")
print("Section : M")

class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        return f'Kangaroo with pouch contents: {self.pouch_contents}'

kanga = Kangaroo()
roo = Kangaroo()

kanga.put_in_pouch('apple')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)

