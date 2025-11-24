tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    num_cols = len(table)
    col_width = [0] * num_cols

    for i in range(num_cols):
        col_width[i] = max(len(col) for col in table[i])

    num_rows = len(table[0])

    for row in range(num_rows):
        row_items = []
        for col in range(num_cols):
            row_items.append(table[col][row].rjust(col_width[col]))
        print(' '.join(row_items))

print_table(tableData)
