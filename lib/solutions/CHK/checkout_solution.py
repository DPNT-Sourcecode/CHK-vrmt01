# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):

    if type(skus) != str:
        return -1

    total = 0
    occrs = {}

    offers = {"A" : [[3, 20], ["A", 5, 50]], 
              "B" : [[2, 15]],
              "E" : [[2, ]]
              }

    items = {"A" : 50, 
             "B" : 30, 
             "C" : 20, 
             "D" : 15,
             "E" : 40
             }

    for sku in skus:

        if not sku in items:
            return -1


        cost = items[sku]

        total += cost   #Add cost to total
        curr = occrs.get(sku, 0)  #Current no. of occurences
        occrs[sku] = curr + 1 #Increment no. of occurences

        if sku in offers:
            #Check if offer satisified
            if occrs[sku] == offers[sku][0]:
                total -= offers[sku][1]
                occrs.pop(sku)

    return total

