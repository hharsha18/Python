print("Harsha D S, USN:1AY24AI041, SEC:M")

def print_table(data):
    if not data:
        print("No data to display.")
        return

    num_columns = len(data[0])
    col_widths = [max(len(str(row[i])) for row in data) for i in range(num_columns)]

    
    header = data[0]
    print(" | ".join(str(header[i]).ljust(col_widths[i]) for i in range(num_columns)))

    print("-+-".join('-' * col_widths[i] for i in range(num_columns)))

    for row in data[1:]:
        print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(num_columns)))

table_data = [
    ["Name", "Age", "City"],
    ["Ravi", 28, "Bangalore"],
    ["Sneha", 22, "Mumbai"],
    ["Aditya", 31, "Chennai"]
]


print_table(table_dat
