def algoritm_vibor(lis):
    new_mas =[]
    while lis !=[]:

        def lil_elem(lis):
            li = lis[0]
            lil_element_idi = 0
            for i in range(1,len(lis)):
                if li > lis[i]:
                    li = lis[i]
                    lil_element_idi = i
            return lil_element_idi
        litl = lil_elem(lis)
        new_mas.append(lis.pop(litl))


    return new_mas


mas = [3,4,5,1,2,5,6,7,10,8,9]
print(algoritm_vibor(mas))