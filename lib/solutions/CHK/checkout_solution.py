# noinspection PyUnusedLocal
# skus = unicode string

test_input = "AAAAAA"

def checkout(skus):

    if type(skus) != str:
        return -1

    total = 0
    occrs = {}

    offers = {"A" : [[3, 20], [5, 50]], 
              "B" : [[2, 15]],
              "E" : [[2, 30]]
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

    print(occrs)

    #Apply offers 
    for item in occrs:

        offers = 


        #Find optimal combination of special offers
        nums = []
        for offer in offers[item]:
            nums.append(offer[0])
            

        if item in occrs:
            print(offer_comb(nums, occrs[item]))

    return total



def offer_comb(nums, goal):
    res = []

    def dfs(i, current, total):
        if total <= goal:
            res.append(current.copy())
            return
        if i >= len(nums) or total > goal:
            return

        current.append(nums[i])
        dfs(i, current, total+nums[i])
        current.pop()
        dfs(i+1, current, goal)

    dfs(0, [], 0)

    return res

    



print(checkout(test_input))