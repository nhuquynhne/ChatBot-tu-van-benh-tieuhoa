import pandas as pd
import mysql.connector
from mysql.connector import MySQLConnection, Error

from connectDB import connectDB
from checkAttibute import checkAttibute

from filter import filterByLoaiDau, filterByKhuVucDau, filterByThoiDiemDau, filterByDayHoi, filterByO, filterByNon, filterByAnUong, filterByDiVeSinh, filterByBieuHienBenNgoai, filterBySot

def result(idx):
    df = pd.read_sql("SELECT tenbenh, dieutri FROM dieutri INNER JOIN chandoan ON (chandoan.mabenh = dieutri.mabenh and chandoan.mabenh = '"+idx+"');",db) #dataframe
    # db.close()
    pd.DataFrame(data=df)
    # print(df)
    return df

db = connectDB()
print("Chatbot hỗ trợ tư vấn bệnh tiêu hóa (dạ dày, ruột non, đại tràng, gan, mật, tụy tạng\n")
print("Q: Bạn đau ở vị trí nào? \n1.Không biểu hiện\n2.Đau bụng vùng rốn\n3.Đau vùng thượng vị\n4.Đau tức ngực\n5.Đau lan ra sau lưng phải\n6.Đau cơ khớp\n7.Đau bụng vùng hạ sườn phải\n8.Đau lan lên vai phải\n9.Co cứng thành bụng\n10.Đau bụng vùng nửa khung đại tràng trái\n11.Đau dọc theo khung đại tràng\n12.Đau bụng vùng hai hố chậu\n13.Đau bụng trên\n14.Đau bụng dưới\n15.Ấn môn vị đau\n------------------------------------------------------")
ans1 = input("A: ") #4
# ans1 = "dau tuc nguc"
k = []
v = []
vt = []
df, k, v = filterByKhuVucDau(ans1, k, v)#dataframe #"1"
vt.append("1")
cf = df
check = True
temp = [1]
while(check) :
    # print("Lan thu: ", check)
    cf = df
    #ans = input()
    # print(df)
    if (len(df)==0):
        print("Vui long nhap lai")
        check = False
        break
    # print("do dai df: ", len(df))
    idx = checkAttibute(cf.to_numpy(), temp) 
    # print(type(idx))
    # print("idx la: ", idx)
    if (type(idx) == str or idx<0): 
        rs = result(idx)
        print("\n\n\n Ket Thuc")
        print("Chẩn đoán: ", rs.to_numpy()[0][0])
        print("Điều trị: ", rs.to_numpy()[0][1])
        # mabenh = ["b1.txt", "b2.txt", "b3.txt", "b4.txt", "b5.txt", "b6.txt", "b7.txt", "b8.txt", "b9.txt", "b10a.txt", "b10b.txt", "b10c.txt", "b11a.txt", "b11b.txt", "b12.txt", "b13a.txt", "b13b.txt", "b14.txt"]
        # for i in mabenh:
        #     if(idx in i):
        #         f = open(i, 'r', encoding='UTF-8')
        #         dt = f.read()
        #         print(dt)
        check = False
        break

    else:  
        key = df.keys()[idx] #madivesinh
        # print(type(key))
        # print("key la: ", key)
        ma = ["maloaidau", "makhuvucdau", "mathoidiemdau", "madayhoi", "mao", "manon", "maanuong", "madivesinh", "mabieuhienbenngoai", "masot"]
        cnt = -1
        for i in range(0, len(ma)):
            if (ma[i] == key):
                cnt = i
                temp.append(i)
                vt.append(i)
        # print("temp la: ", temp)
        # print("cnt la: ",cnt) #0
        if (cnt == 0):
            print("Q: Bạn đau như thế nào? VD:đau âm ỉ, đau có chu kỳ, đau dữu dội...")
            # print(k, v)
            ans = input("A: ")
            # ans = "dau am i"
            df, k, v = filterByLoaiDau(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
            # print(k, v)
        elif(cnt == 2):
            print("Q: Bạn đau vào thời điểm nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = "khong bieu hien"
            df, k, v = filterByThoiDiemDau(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 3):
            print("Q: Biểu hiện đầy hơi của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = "day hoi"
            df, k, v = filterByDayHoi(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 4):
            print("Q: Biểu hiện ợ của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = ""
            df, k, v = filterByO(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 5):
            print("Q: Biểu hiện nôn của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = "non mua"
            df, k, v = filterByNon(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 6):
            print("Q: Biểu hiện ăn uống của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = ""
            df, k, v = filterByAnUong(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 7):
            print("Q: Biểu hiện đi vệ sinh của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = "tieu chay"
            df, k, v = filterByDiVeSinh(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 8):
            print("Q: Biểu hiện bên ngoài của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = ""
            df, k, v = filterByBieuHienBenNgoai(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break
        elif(cnt == 9):
            print("Q: Biểu hiện sốt của bạn như thế nào?")
            # print(k, v)
            ans = input("A: ")
            # ans = "co, kem theo on lanh"
            df, k, v = filterBySot(ans, k, v, vt) 
            if(k==0 and v==0): 
                check = False
                break