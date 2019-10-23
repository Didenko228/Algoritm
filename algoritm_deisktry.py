graph = {}
graph['start'] = {}
graph['start']['a'] = 2 
graph['start']['b'] = 5
graph['a'] = {}
graph['a']['b'] = 6
graph['a']['c'] = 7
graph['b'] = {}
graph['b']['d'] = 4
graph['b']['c'] = 2
graph['d'] = {}
graph['d']['c'] = 6
graph['d']['fin'] = 3
graph['c'] = {}
graph['c']['fin'] = 1
graph['fin'] = {}

inf = float('inf')
cost = {}
cost['a'] = 2
cost['b'] = 5
cost['c'] = inf
cost['d'] = inf
cost['fin'] = inf

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None


def algoritm_deistri(costes,graphh,parentss):
    proverka = []
    inf = float('inf')
    def soam_litel_element(costes):
        litel_element_namb = inf
        litel_element_node = None
        for node in costes:
            if costes[node]< litel_element_namb and node not in proverka:
                litel_element_namb = costes[node]
                litel_element_node = node
        return litel_element_node
    node = soam_litel_element(costes)
    while node is not None:
        heht = graphh[node]
        costs = costes[node]
        for n in heht.keys():
            new_cost = costs + heht[n]
            if costes[n] > new_cost:
                costes[n] = new_cost
                parentss[n] = node
        proverka.append(node)
        node = soam_litel_element(costes)
    print(str(cost.get('fin'))+ " Стоимость пути")
    storage_Keys  = list(parents.keys())
    way = []
    s = storage_Keys[-1]
    while parents is not None:
        try:
            v = parents.pop(s)
            way.append(s)
        except KeyError:
            way.append(v)
            way.reverse()
            return way
        
        for i in storage_Keys:
            if i == v :
                s = v
            

print(algoritm_deistri(cost,graph,parents))


    









    


            


    






    



