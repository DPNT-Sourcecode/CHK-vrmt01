# noinspection PyUnusedLocal
# skus = unicode string

test_input = "AAABBB"

def checkout(skus):

    if type(skus) != str:
        return -1

    total = 0
    occrs = {}

    offers = {"A" : [[3, 20], [5, 50]], 
              "B" : [[2, 15]],
              "E" : [[2, 30]] #TODO 
              }

    items = {"A" : 50, 
             "B" : 30, 
             "C" : 20, 
             "D" : 15,
             "E" : 40
             }

    #Count occurences of items
    for sku in skus:

        if not sku in items:
            return -1

        cost = items[sku]

        total += cost   #Add cost to total
        curr = occrs.get(sku, 0)  #Current no. of occurences
        occrs[sku] = curr + 1 #Increment no. of occurences

    #Apply offers 
    for item in offers:
        #Find optimal combination of special offers
        nums = []
        for offer in offers[item]:
            nums.append(offer[0])
            
        print(nums)

    return total



def offer_comb(num, goal, partial=[]):

    s = sum(partial)

    if s < goal:
        print(partial)
    if s >= goal:
        return

    for i in range(len(nums)):
    n = nums[i]
    remaining = nums[i+1:]
    offer_comb(remaining, goal, partial + [n])



print(checkout(test_input))


