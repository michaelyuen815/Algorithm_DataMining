def generate_itemset(numitemin1set, basket):
    #running recursion to generate 
    itemsets = []
    for i in range(len(basket)):
        if numitemin1set == 1:
            itemsets.append(basket[i])
        else:
            temp = generate_itemset(numitemin1set - 1, basket[i+1:])
            for itemset in temp:
                itemsets.append("".join(sorted([basket[i]+itemset])))
    return itemsets

def frequentitemsNaive(baskets, uniqueItems, therholds):
    frequentItem = {}
    numUniqueItems = len(uniqueItems)
    tot_n_actual = 0
    tot_n_theortical = 0


    print(f"Use Naive algorithm, will run {numUniqueItems} passes to find all frequents items")
    for i in range(numUniqueItems):
        print(f"Pass {i+1}:")
        dict_itemset = {}
        n = 0
        full_itemsets = generate_itemset(i+1, uniqueItems)
        for basket in baskets:
            itemsets = generate_itemset(i+1, basket)
            n += len(itemsets)
            for itemset in itemsets:
                if itemset not in dict_itemset:
                    dict_itemset[itemset] = 1
                else:
                    dict_itemset[itemset] += 1
            
        for itemset in dict_itemset.keys():
            if dict_itemset[itemset] >= therholds:
                print(f"itemset ({itemset}) has {dict_itemset[itemset]} count, become a frequent item")
                frequentItem[itemset] = dict_itemset[itemset]
        print(f"Pass {i+1} completed, total {n} itemset has been checked this round")
        tot_n_theortical += len(full_itemsets) * len(basket)
        tot_n_actual += n

    print(f"{numUniqueItems} passes is completed and {tot_n_actual} itemsets(theoretically {tot_n_theortical}) are examinated.")
    return frequentItem


def frequentitemsAPriori(baskets, uniqueItems, therholds):# not completed
    frequentItem = {}
    dict_itemset = {}
    numUniqueItems = len(uniqueItems)
    startflag = True

    print(f"Use A-Priori algorithm, will stop if no more frequents items in current pass")
    #Continue loop if 1st round or continue 
    while(dict_itemset or startflag):

        #generate list of single unique items to be considered in this pass
        if startflag:
            startflag = False
        else:
            previousfrequentItem = [dict_itemset.keys()]
        dict_itemset = {}
        n = 0
        for basket in baskets:
            #short list the baskets based on list of single unique items


            #generate itemsets based on short list items
            itemsets = generate_itemset(i+1, basket)
            n += len(itemsets)
            for itemset in itemsets:
                if itemset not in dict_itemset:
                    dict_itemset[itemset] = 1
                else:
                    dict_itemset[itemset] += 1
            
        for itemset in dict_itemset.keys():
            if dict_itemset[itemset] >= therholds:
                print(f"itemset ({itemset}) has {dict_itemset[itemset]}, count as a frequent items")
                frequentItem[itemset] = dict_itemset[itemset]
            else:
                del dict_itemset[itemset]
        print(f"Pass {i+1} completed, total {n} itemset has been checked this round")
        tot_n_theortical += len(generate_itemset(i+1, uniqueItems))
        tot_n_actual += n

    print(f"{numUniqueItems} passes is completed and {tot_n_actual} itemsets are examinated.")
    return frequentItem



baskets = ["acde", "abc", "acd", "ab"]
uniqueItems = ['a', 'b', 'c', 'd', 'e']

print(frequentitemsNaive(baskets, uniqueItems, 2))
