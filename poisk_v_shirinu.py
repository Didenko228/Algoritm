from collections import deque


    
graph = {}
graph['me'] = ['alisa','yana','katy']
graph['alisa'] = ['bory','vova']
graph['yana'] = ['nady']
graph['katy'] = ['vasy','kristina']
graph['bory'] = []
graph['nady'] = []
graph['vasy'] = []
graph['kristina'] = []
graph['vova'] = []
q = deque()

def poysc(name):
    if name == 'vasy':
        return True
    else:
        return False


q += graph['me']
while q :
    person = q.popleft()
    if poysc(person):
        print(str(person) + "eeeeee.jq")
    else:
        q += graph[person]

