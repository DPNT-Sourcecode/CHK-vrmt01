
test_input = "AAABBB"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    total = 0
    occrs = {}
    offers = {"A" : [3, 20], "B" : [2, 15]}

    for sku in skus:

        cost = int(line[1])
        item = line[0]

        total += cost   #Add cost to total
        curr = occrs.get(item, 0)  #Current no. of occurences
        occrs[item] = curr + 1 #Increment no. of occurences

        offer = line[2].strip().split(" ")

        #Check offer exists for item
        if len(offer) > 2:

            if item in offers:
                #Check if offer satisified
                if occrs[item] == offers[item][0]:
                    total -= offers[item][1]
            else:
                #Add offer
                num_needed = int(offer[0][:-1])
                discount = cost * num_needed - int(offer[2])
                offers[item] = [num_needed, discount]

    return total


