def display_inventory(inventory):
    item_total = 0

    for item, count in inventory.items():
        print(str(count) + ' ' + str(item))
        item_total += count

    print('Total number of items: ' + str(item_total))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)
