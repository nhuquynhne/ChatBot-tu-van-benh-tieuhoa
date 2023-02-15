# import random
import pandas as pd
# import numpy as np
# import mysql.connector
# from mysql.connector import MySQLConnection, Error

from connectDB import connectDB
from mysql.connector import  Error

# db = connectDB()
# sql = "SELECT maloaidau, makhuvucdau, mathoidiemdau, madayhoi, mao, manon, maanuong, madivesinh, mabieuhienbenngoai, masot FROM chandoan"
# df = pd.read_sql(sql,db) #dataframe
# pd.DataFrame(data=df)
# cf = df.to_numpy()
# print(cf[0])
# print(cf)
# arr = cf[0][1].split(",")
# print(arr)
# ld = 2
# kv = 1

# k = ["makhuvucdau", "madivesinh", "maloaidau"]
# v = ["4", "2", "1"]
# vt = ["1", "7", "0"]
# cnt = 2 #thoidiemdau
# brr = []
# for i in range(0, len(df)):
#     arr = cf[i][cnt].split(",")
#     for j in range(0, len(arr)):
#         if(int(arr[j])==7): 
#             brr.append(i) #3,8,12,16
#             # print(i) 
# brr.sort()
# crr = brr.copy()
# for x in range(0, len(k)): #2
#     brr.clear()
#     for m in crr: #3
#         arr = cf[int(m)][int(vt[x])].split(",") 
#         print("gia tri arrtai hang ", m, ", cot ", vt[x], ": ", arr)
#         print("do dai arr: ", len(arr))
#         for j in range(0, len(arr)): #1
#             if(int(arr[j])==int(v[x])): 
#                 print(int(arr[j]), int(v[x]))
#                 brr.append(m)
#                 brr.sort() #3
#                 # print(m) #3
#     crr = brr.copy()
# print(brr)
k = ["1", "2"]
k = 0
print(k)