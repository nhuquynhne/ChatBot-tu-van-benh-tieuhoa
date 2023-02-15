def checkAttibute(df, temp):
    idx = -1
    if(len(df)==1):
        mabenh = df[0][len(df[0])-1]
        idx = mabenh    

    else:
        max = -1
        # print("vt la: ", temp)
        
        for i in range(0, len(df[0])-1): #len(df[0]) = 10
            check = True
            for j in temp: #những vị trí đã xét rồi
                if (i == int(j)):
                    check = False
                    break
            if (check):
                # print(i)
                arr = []
                cnt = 0
                for j in range(0, len(df)): 
                    arr.append(df[j][i])
                    arr = list(set(arr))
                    cnt = len(arr)
                # print("lan ",i,":", arr, "and", cnt)
                if (cnt>max): 
                    max = cnt
                    idx = i
        # print(max, "and", idx)
    return idx  #trẩ về vị trí của thuộc tính tiếp theo =7