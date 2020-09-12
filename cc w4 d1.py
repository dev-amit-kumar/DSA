def Sort_marks(new_list): 
    l = len(new_list) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (new_list[j][0] > new_list[j + 1][0]): 
                tempo = new_list[j] 
                new_list[j] = new_list[j + 1] 
                new_list[j + 1] = tempo 
    return new_list 
  
item = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
item = Sort_marks(item)
st = item[0][0]
maxi = []
out = []
for i in item:
    print(i)
    if(i[0] == st):
        maxi.append(i[1])
    else:
        maxi.sort(reverse = True)
        total = (maxi[0] + maxi[1] + maxi[2] + maxi[3] + maxi[4])//5
        b = [st, total]
        print(b)
        b.clear()
        maxi.clear()
        maxi.append(i[1])
        st = i[0]

