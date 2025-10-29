def searchinCluster(lcluster, point):
    #return True if point is in cluster. Otherwise return False
    for item in lcluster:
        if type(item) is list:
            if searchinCluster(item, point):
                return True
        else:
            if item == point:
                return True
    return False


def agglomerativeClustering(distanceMatrix, linkage="Single"): #Only handle single linkage, will update complete linkage and average linkage
    cluster_reseult = []
    numCluster = 0


    while (numCluster < len(distanceMatrix)):
        cur_pt = []
        cur_min_distance = 0
        #finding the points with the shortest distance
        for i in range(len(distanceMatrix)-1):
            for j in range(1 + i, len(distanceMatrix)):
                if (not(searchinCluster(cluster_reseult,i + 1) and searchinCluster(cluster_reseult,j + 1)) and (not cur_pt or distanceMatrix[i][j] <= cur_min_distance)):
                    if distanceMatrix[i][j] == cur_min_distance:
                        if i + 1 in cur_pt:
                            cur_pt.append[j + 1]
                        else:
                            cur_pt.append[i + 1]
                    else:
                        cur_pt = [i + 1,j + 1]
                    cur_min_distance = distanceMatrix[i][j]
        print(f"This turn found points({cur_pt}) has the shorted distance {cur_min_distance}")

        clustered_pt = None
        for item in cur_pt:
            if searchinCluster(cluster_reseult,item):
                cur_pt.remove(item)
                #Keep linkage point for find related cluster later
                #Miss handling for mutliple linkage point
                clustered_pt = item
        numCluster += len(cur_pt)
        if (not(clustered_pt)):
            #If not clustered point, append as a new cluster
            cluster_reseult.append(cur_pt)
        else:
            #If there is clustered point, find out the related cluster and merge with them.
            i = 0
            while (not(searchinCluster(cluster_reseult[i], clustered_pt))):
                i +=1
            cluster_reseult[i] = [cluster_reseult[i]]+ cur_pt
            print(f"point {clustered_pt} has been cluster in previous round, {cur_pt} will be grouped as {cluster_reseult[i]}")

            #For complete linkage and average linkage, update the distance matrix for new added cluster



    return cluster_reseult




distanceMatrix = [[0,0.95, 0.1, 0.45, 0.15],
                  [0.95, 0, 1.05, 0.5, 0.8], 
                  [0.1, 1.05, 0, 0.55, 0.25], 
                  [0.45, 0.5, 0.55, 0, 0.3], 
                  [0.15, 0.8, 0.25, 0.3 , 0]]

print(agglomerativeClustering(distanceMatrix))