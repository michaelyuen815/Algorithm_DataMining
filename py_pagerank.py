#class point setup 
class point:
    def __init__(self, name, outlink = None):
        self.name = name
        if outlink is None:
            self.outlink = []
        else:
            if isinstance(outlink, list):
                self.outlink = []
                for _outlink in outlink:
                    if _outlink not in self.outlink:
                        self.outlink.append(_outlink)
                        _outlink.addInlink(self)
            else:
                self.outlink = [outlink]
                outlink.addInlink(self)
        self.inlink = []
    
    def get_name(self):
        return self.name
    
    def get_outlink(self):
        return self.outlink
    def get_inlink(self):
        return self.inlink
    
    def get_outlink_names(self):
        if not (self.outlink):
            return []
        return [outlink.get_name() for outlink in self.outlink]
    def get_inlink_names(self):
        if not (self.inlink):
            return []
        return [inlink.get_name() for inlink in self.inlink]

    def addOutlink(self, outlink):
        if isinstance(outlink, list):
            for _outlink in outlink:
                if _outlink not in self.outlink:
                    self.outlink.append(_outlink)
                    _outlink.addInlink(self)
        else:
            if outlink not in self.outlink:
                self.outlink.append(outlink)
                outlink.addInlink(self)
        return self

    def addInlink(self, inlink):
        if isinstance(inlink, list):
            self.inlink.extend(inlink)
        else:
            self.inlink.append(inlink)
        return self

#function 1(utlimate version) return 1. a list of node name(n) and 2. n x n pagerank matrix with 
# inputting 1. a dictionary flow model where each node with format 
#                   {name: value, 
#                   outlink: list of pointer to other node, 
#                   inlink: list of pointer to other node}

#version a
# return pagerank matrix with inputting a list of point class (length n)
def getPageRankMatrix_simple(lpoint):
    n = len(lpoint)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        outlink = lpoint[i].get_outlink()
        for j in range(n):
            if lpoint[j] in outlink:
                matrix[j][i] = 1 / len(outlink)
    return matrix

#version b(final version)
def getPageRankMatrix(lpoint):
    return





#fundtion 2 return a stationary distribution after max n iterations 
# inputting 1. pagerank matrix, 
#           2. initial station distribution(default unitform distributed), 
#           3. max_iteration(n),
#           4. tolerence level to stop(e),
#           5. random walk factor(beta)
def pagerankiteration(matrix, init_sd = None, max_iter = 10, e = 0.1, beta = 1):
    n = len(matrix)

    #setup unitform distributed for initial stationary distribution if it's not setup
    if init_sd is None:
        init_sd = [1/n for _ in range(n)]

    cur_sd = init_sd
    

    for i in range(max_iter):
        prev_sd = cur_sd
        cur_sd = []
        for sd_vector in matrix:
            indiv_sd = 0
            for j in range(n):
                indiv_sd += sd_vector[j] * prev_sd[j]
            #adjust beta (random walk factor)
            indiv_sd = beta*indiv_sd + (1-beta)/n
            cur_sd.append(indiv_sd)

        
        #compare the discrepancies with previous stattionary distritbution
        total_error = 0
        for j in range(n):
            total_error += abs(prev_sd[j] - cur_sd[j])
        print(f"{i + 1}th round: current sd = {[round(sd,2) for sd in cur_sd]}, prev sd = {[round(sd,2) for sd in prev_sd]}, total_error = {round(total_error, 4)}" )
        if (total_error <= e):
            print(f"current stattionar distribution is similar to previous distribution within toerlenace level {e}, iteration stop at {i + 1}th round.")
            return cur_sd
    
    print(f"current stattionar distribution ({[round(sd,2) for sd in cur_sd]}) found after running {max_iter} iterations")
    return cur_sd


#function 3 return calculated pagerank vector with inputting pagerank matrix where r = Mr and sum(r) = 1


P1 = point("P1")
P3 = point("P3", P1)
P2 = point("P2", [P1, P3])
P1 = P1.addOutlink(P2)
M = [[0,0.5, 1], [1, 0, 0], [0, 0.5, 0]]

pagerankiteration(M, None, beta = 0.8)
print(getPageRankMatrix_simple([P1,P2,P3]))



del P1
del P2
del P3
