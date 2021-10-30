
test_input = "AAABBB"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    total = 0
    occrs = {}
    offers = {"A" : [3, 20], "B" : [2, 15]}
    costs = {"A" : 50, "B" : 30, "C" : 20, "D" : 15}

    for sku in skus:

        cost = costs[sku]

        total += cost   #Add cost to total
        curr = occrs.get(sku, 0)  #Current no. of occurences
        occrs[sku] = curr + 1 #Increment no. of occurences

        if sku in offers:
            #Check if offer satisified
            if occrs[sku] == offers[sku][0]:
                total -= offers[sku][1]

    return total

print(checkout(test_input))


