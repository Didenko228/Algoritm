
def qwicli_sort(ls):

    if len(ls)<2:
        return ls
    pivot = ls[0]
    low = []
    hect = []
    for i in range(1,len(ls)):
        if pivot > ls[i]:
            low.append(ls[i])
        if pivot < ls[i]:
            hect.append(ls[i])

        
    return qwicli_sort(low) + [pivot] + qwicli_sort(hect)


mas = [1,2,4,6,3,0,9,7,8]
print(qwicli_sort(mas))