def sort_sides(l_in):
    l_in.sort(key=lambda i: (i[0]**2 + i[1]**2)  (1/2))
    return l_in

print(sort_sides([(3,4), (1,2), (10,10)]))