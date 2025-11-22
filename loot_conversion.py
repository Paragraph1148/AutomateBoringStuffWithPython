def add_to_inventory(inventory, items):
    updated = inventory.copy()
    for item in items:
        updated[item] = updated.get(item, 0) + 1
    return updated
    
def display_inventory(inventory):
    item_total = 0

    for item, count in inventory.items():
        print(str(count) + ' ' + str(item))
        item_total += count

    print('Total number of items: ' + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)