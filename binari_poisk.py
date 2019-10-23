def bynari_poysc(lis,item):
    low = 0
    heht = len(lis)-1
    while low < heht:
        mid = (low+heht)//2
        if lis[mid] < item:
            low = heht+1
        elif lis[mid] > item:
            heht = low-1
        elif lis[mid] == item:
            return mid

mas = ['a','b','c','d','e','f','g','h','k','l','z']
print(bynari_poysc(mas,'f'))
