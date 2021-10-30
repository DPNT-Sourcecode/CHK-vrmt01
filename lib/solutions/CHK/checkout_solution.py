# noinspection PyUnusedLocal
# skus = unicode string

test_input = "AAAAAAAAAAAAAA"

def checkout(skus):

    if type(skus) != str:
        return -1

    total = 0
    occrs = {}

    offers = {"A" : {3 : 20, 5 : 50}, 
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

        nums = list(offers.get(item).keys())

        ans = []
        temp = []

        offer_comb(ans, nums, temp, occrs[item], 0)
        print(ans)

        max = []
        for comb in ans:
            total = 0
            for i in range(len(comb)):
                total += offers[item][comb[i]]

            print(total)



    return total



def offer_comb(ans, nums, temp, sum, i):

    if sum >= 0:
        print(temp)
        ans.append(list(temp))
    if sum < 0:
        return

    for i in range(i, len(nums)):
        if(sum - nums[i]) >= 0:
            temp.append(nums[i])
            offer_comb(ans, nums, temp, sum-nums[i], i)

            temp.remove(nums[i])


print(checkout(test_input))

