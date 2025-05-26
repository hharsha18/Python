print("Harsha D S, USN: 1AY24AI041, SEC: M")

game_inventory = {'rope': 1, 'gold coin': 42}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    print("\nUpdated Inventory:")
    total = 0

    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1

    print(f"{'Item Name':<15}{'Count':>10}")
    print("-" * 25)
    for item, count in inventory.items():
        print(f"{item:<15}{count:>10}")
        total += count

    print("-" * 25)
    print(f"{'Total number of items:':<15}{total:>10}")

addToInventory(game_inventory, dragon_loot)
