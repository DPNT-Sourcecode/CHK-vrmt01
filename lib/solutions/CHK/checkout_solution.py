# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    if not type(skus) == str:
        return -1

    #Split input into lines and remove first 3 and last
    lines = skus.splitlines()[3:-1]

    #Split each line by "|" and remove first and last
    lines = [item.split("|")[1:-1] for item in lines]

    total = 0
    occrs = {}
    offers = {}

    for line in lines:

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
