# noinspection PyUnusedLocal
# skus = unicode string

import math

def checkout(skus):

    if type(skus) != str:
        return -1

    total = 0
    occrs = {}

    offers = {"A" : {3 : 20, 5 : 50},
              "B" : {2 : 15}
              }

    free = {"E" : [2, "B"]}

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
    for item in occrs:

        #B1G1F
        if item in free:

            #How many possible discount
            count = math.floor(occrs[item] / free[item][0])

            #Item thats free
            free_item = free[item][1]

            if free_item in occrs:

                x = min(count, occrs[free_item])
            
                total -= x * items[free[item][1]]

                



    for item in occrs:            

        if item in offers:
            nums = list(offers.get(item).keys())

            ans = []
            temp = []

            offer_comb(ans, nums, temp, occrs[item], 0) #Compute all combinations of offers

            best_comb = []
            maximum = 0
            for comb in ans:
                discount = 0
                for i in range(len(comb)):
                    discount += offers[item][comb[i]]

                if maximum < discount:
                    maximum = discount
                    best_comb = comb

            total -= maximum




    return total



def offer_comb(ans, nums, temp, sum, i):

    if sum >= 0:
        ans.append(list(temp))
    if sum < 0:
        return

    for i in range(i, len(nums)):
        if(sum - nums[i]) >= 0:
            temp.append(nums[i])
            offer_comb(ans, nums, temp, sum-nums[i], i)

            temp.remove(nums[i])



