print("Harsha D S,USN:1AY24AI041,SEC:M")

rows = 3         
cols = 8     
for row in range(rows):
    for col in range(cols):
        if ((row + col) % 4 == 0) or (row == 1 and col % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
