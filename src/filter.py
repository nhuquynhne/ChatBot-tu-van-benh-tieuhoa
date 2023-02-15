import pandas as pd
from connectDB import connectDB

db = connectDB()

def getAllChanDoan():
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot FROM chandoan"
    df = pd.read_sql(sql,db) #dataframe
    pd.DataFrame(data=df)
    cf = df.to_numpy()
    return cf

def filterByLoaiDau(ans, k, v, vt):
    ma = pd.read_sql("SELECT maloaidau FROM loaidau WHERE loaidau.loaidau = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    # sql = "SELECT machandoan, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][0].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    cnt = 0
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)

    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("maloaidau")
    v.append(code)
    # print(df)
    return df, k, v

def filterByKhuVucDau(ans1, k, v):
    ma = pd.read_sql("SELECT makhuvucdau FROM khuvucdau WHERE khuvucdau.khuvucdau = '"+ans1+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0]) #4
    # df = pd.read_sql("SELECT maloaidau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN khuvucdau ON (khuvucdau.makhuvucdau = chandoan.makhuvucdau and khuvucdau.makhuvucdau = '"+code+"')",db) #dataframe
    cf = getAllChanDoan()
    sql = "SELECT maloaidau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    cnt = 0
    for i in range(0, len(cf)):
        arr = cf[i][1].split(",") #cf[0][1]= ["1,2"] = ["1", "2"]
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                cnt = cnt+1
                s2 = "chandoan.machandoan = "+ str(i)
                sql = sql + s2
                if (cnt>0): sql = sql + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)

    # db.close()
    pd.DataFrame(data=df)
    k.append("makhuvucdau")
    v.append(code) #4
    return df, k, v


def filterByThoiDiemDau(ans, k, v, vt):
    ma = pd.read_sql("SELECT mathoidiemdau FROM thoidiemdau WHERE thoidiemdau.thoidiemdau = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    #sql = "SELECT machandoan, maloaidau, makhuvucdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN thoidiemdau ON (thoidiemdau.mathoidiemdau = chandoan.mathoidiemdau and thoidiemdau.mathoidiemdau = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][2].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, madayhoi, mao, maanuong, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)
    
    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("mathoidiemdau")
    v.append(code)
    # print(df)
    return df, k, v

def filterByDayHoi(ans, k, v, vt):
    ma = pd.read_sql("SELECT madayhoi FROM dayhoi WHERE dayhoi.dayhoi = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    #sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN dayhoi ON (dayhoi.madayhoi = chandoan.madayhoi and dayhoi.madayhoi = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][3].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)
    
    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("madayhoi")
    v.append(code)
    # print(df)
    return df, k, v

def filterByO(ans, k, v, vt):
    ma = pd.read_sql("SELECT mao FROM o WHERE o.bieuhien = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    #sql = "SELECT machandoan, maloaidau, makhuvucdau, mathoidiemdau, madayhoi, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN o ON (o.mao = chandoan.mao and o.mao = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][4].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()

    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("mao")
    v.append(code)
    return df, k, v

def filterByNon(ans, k, v, vt):
    ma = pd.read_sql("SELECT manon FROM non WHERE non.bieuhien = '"+ans+"'",db)
    print(ma)
    code = str(ma.to_numpy()[0][0])
    # sql = "SELECT machandoan, maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN non ON (non.manon = chandoan.manon and non.manon = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][5].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)

    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("manon")
    v.append(code)
    # print(df)
    return df, k, v

def filterByAnUong(ans, k, v, vt):
    ma = pd.read_sql("SELECT maanuong FROM anuong WHERE anuong.bieuhien = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    #sql = "SELECT machandoan, maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN anuong ON (anuong.maanuong = chandoan.maanuong and anuong.maanuong = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][6].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)

    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("maanuong")
    v.append(code)
    return df, k, v

def filterByDiVeSinh(ans, k, v, vt):
    ma = pd.read_sql("SELECT madivesinh FROM divesinh WHERE divesinh.bieuhien = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0]) #8
    #sql = "SELECT machandoan, maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN divesinh ON (divesinh.madivesinh = chandoan.madivesinh and divesinh.madivesinh = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][7].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()

    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, mabieuhienbenngoai, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)

    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("madivesinh")
    v.append(code)
    # print(df)
    return df, k, v

def filterByBieuHienBenNgoai(ans, k, v, vt):
    ma = pd.read_sql("SELECT mabieuhienbenngoai FROM bieuhienbenngoai WHERE bieuhienbenngoai.bieuhien = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    #sql = "SELECT machandoan, maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, masot, mabenh FROM chandoan INNER JOIN bieuhienbenngoai ON (bieuhienbenngoai.mabieuhienbenngoai = chandoan.mabieuhienbenngoai and bieuhienbenngoai.mabieuhienbenngoai = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][8].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, masot, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)
    
    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("mabieuhienbenngoai")
    v.append(code)
    return df, k, v

def filterBySot(ans, k, v, vt):
    ma = pd.read_sql("SELECT masot FROM sot WHERE sot.bieuhien = '"+ans+"'",db)
    # print(ma)
    code = str(ma.to_numpy()[0][0])
    #sql = "SELECT machandoan, maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, mabenh FROM chandoan INNER JOIN sot ON (sot.masot = chandoan.masot and sot.masot = '"+code+"'"
    
    cf = getAllChanDoan()
    brr = []
    for i in range(0, len(cf)):
        arr = cf[i][9].split(",")
        for j in range(0, len(arr)):
            if(int(arr[j])==int(code)): 
                brr.append(i) #3,8,12,16
                # print(i) 
    brr.sort()
    crr = brr.copy()
    for x in range(0, len(k)): #2
        brr.clear()
        for m in crr: #3
            arr = cf[int(m)][int(vt[x])].split(",") 
            # print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
            # print("do dai arr: ", len(arr))
            for j in range(0, len(arr)): #1
                if(int(arr[j])==int(v[x])): 
                    # print(int(arr[j]), int(v[x]))
                    brr.append(m)
                    brr.sort() #3
                    # print(m) #3
        crr = brr.copy()
    if (len(brr)==0): 
        print ("biểu hiện này không thể chẩn đoán. Yêu cầu nhập lại")
        return 0, 0, 0
    sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, mabenh FROM chandoan where ("
    for n in brr:
        s2 = "chandoan.machandoan = "+ str(n)
        sql = sql + s2 + " or "
    sql = sql[:-3]+ ")"
    df = pd.read_sql(sql,db)
    
    # for i in range (0, len(k)):
    #     s2 = " and "+"chandoan."+k[i]+" = "+v[i]
    #     sql = sql + s2
    # sql = sql + ")"
    # df = pd.read_sql(sql,db) #dataframe
    # df = pd.read_sql("SELECT mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot, mabenh FROM chandoan INNER JOIN loaidau ON (loaidau.maloaidau = chandoan.maloaidau and loaidau.maloaidau = '"+code+"')",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    k.append("masot")
    v.append(code)
    # print(df)
    return df, k, v