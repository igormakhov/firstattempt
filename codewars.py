def spinning_rings(inner_max, outer_max):
    inner_list = []
    outer_list = []
    for a in range(0, inner_max+1):
        inner_list.append(a)
    print(inner_list)
    for b in range(0, outer_max+1):
        outer_list.append(b)
    outer_list.reverse()
    print(outer_list)
    i = inner_list[1]
    j = outer_list[0]
    print(i, j)
    while i == j:

    print(i, j)
spinning_rings(5, 7)
