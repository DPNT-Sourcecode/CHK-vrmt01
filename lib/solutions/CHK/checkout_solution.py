

test_input = """+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
| A    | 50    | 3A for 130     |
| A    | 50    | 3A for 130     |
+------+-------+----------------+"""

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    #Check if illegal input
    #   return -1

    #Split input into lines
    #   remove first 3 and last
    lines = skus.splitlines()[3:-1]

    #Split each line by "|"
    lines = [item.split("|")[1:-1] for item in lines]
    print(lines)


    #Loop sku
    #   add cost to total sum
    #   add occurnce of item into dictionary
    #   check if offer?
    #       if so, satisifed?
    #           if so, reduce sum

    return -1


checkout(test_input)



