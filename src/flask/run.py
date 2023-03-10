# import random
# import pandas as pd
# import numpy as np
# from RandomForest import RandomForest
# import mysql.connector
# from mysql.connector import MySQLConnection, Error


# def compute_tp_tn_fn_fp(y_test, predictions):
# 	'''
# 	True positive - actual = 1, predicted = 1
# 	False positive - actual = 1, predicted = 0
# 	False negative - actual = 0, predicted = 1
# 	True negative - actual = 0, predicted = 0
# 	'''
# 	tp = sum((y_test == 1) & (predictions == 1))
# 	tn = sum((y_test == 0) & (predictions == 0))
# 	fn = sum((y_test == 1) & (predictions == 0))
# 	fp = sum((y_test == 0) & (predictions == 1))
# 	return tp, tn, fp, fn


# def compute_accuracy(tp, tn, fn, fp):
# 	'''
# 	Accuracy = TP + TN / FP + FN + TP + TN
# 	'''
# 	return ((tp + tn) * 100)/ float( tp + tn + fn + fp)


# def compute_precision(tp, fp):
# 	'''
# 	Precision = TP  / FP + TP 
# 	'''
# 	return (tp  * 100)/ float( tp + fp)


# def compute_recall(tp, fn):
# 	'''
# 	Recall = TP /FN + TP 
# 	'''
# 	return (tp  * 100)/ float( tp + fn)


# def compute_f1_score(y_true, y_pred):
#     # calculates the F1 score
#     tp, tn, fp, fn = compute_tp_tn_fn_fp(y_true, y_pred)
#     precision = compute_precision(tp, fp)/100
#     recall = compute_recall(tp, fn)/100
#     f1_score = (2*precision*recall)/ (precision + recall)
#     return f1_score*100


# def train_test_split(X, y, train_size):
#     indexList = [i for i in range(len(y))]
#     random.shuffle(indexList)
#     sizeTrain = round(len(y)*train_size)
#     trainIndex = [indexList[i] for i in range(sizeTrain)]
#     testIndex = [indexList[i] for i in range(sizeTrain, len(indexList))]
#     X_train = X.iloc[trainIndex, :]
#     y_train = pd.Series([y[i] for i in trainIndex])
#     X_test = X.iloc[testIndex, :]
#     y_test = pd.Series([y[i] for i in testIndex])
#     return X_train, X_test, y_train, y_test


# # def insertResultData(actual_list, predict_list):
# #     query = ("CREATE TABLE result (`id` INT, `actual` INT, `predict` INT)")
# #     sql = "INSERT INTO result(actual, predict) VALUES(%s,%s)"
# #     # sql = "UPDATE result SET `actual` = %s, `predict` = %s, `recall` = %s, `f1` = %s WHERE `id` = 0"
# #     try:
# #         # conn = connect()
# #         cursor = db.cursor()
# #         for i, j in zip(actual_list, predict_list):
# #             data = (int(i), int(j))
# #             cursor.execute(query, data)
# #         print("Thanh cong")

# #         db.commit()
# #     except Error as error:
# #         print(error)
# #     finally:
# #         # ????ng k???t n???i
# #         cursor.close()
# #         db.close()

# def insertEvaluateData(arr):
#     # query = ("CREATE TABLE evaluatescratch (`id` INT, `acc` FLOAT, `precision_` FLOAT, `recall` FLOAT, `f1_score` FLOAT)")
#     # sql = "INSERT INTO evaluatescratch (`id`, `acc`, `precision_`, `recall`, `f1_score`) VALUES(%s, %s, %s, %s, %s)"
#     sql = "UPDATE evaluatescratch SET `acc` = %s, `precision_` = %s, `recall` = %s, `f1_score` = %s WHERE `id` = 1"
#     try:
#         # conn = connect()
#         cursor = db.cursor()
#         data = tuple(arr)
#         print(data)
#         # cursor.execute(query)
#         cursor.execute(sql, data)
#         print("Thanh cong")
#         db.commit()
#     except Error as error:
#         print(error)
#     finally:
#         # ????ng k???t n???i
#         cursor.close()
#         db.close()

# # df = pd.read_csv("D:\\Hoc Ky 1_2022\\IOT\\AA\\1.csv")
# try:
#     # Ket noi MySQL voi Python bang ham mysql.connector.connect()
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="123456",
#         database="btliot"
#     )
#     print("Ket noi thanh cong!")
# except: # Truong hop co loi khi ket noi
#     print("Kiem tra lai thong tin ket noi!")

# df = pd.read_sql("SELECT * FROM test15k ",db)
# # db.close()
# pd.DataFrame(data=df)
# # print(df)

# X = df.drop(labels=['HeartDiseaseorAttack',],axis=1)
# y = df['HeartDiseaseorAttack']

# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3)
# X_train = X_train.to_numpy()
# X_test = X_test.to_numpy()
# y_train = y_train.to_numpy()
# y_test = y_test.to_numpy()

# # print(X_train, "\n\n\n",X_test, "\n\n\n",y_train, "\n\n\n",y_test)

# def accuracy(y_true, y_pred):
#     accuracy = np.sum(y_true == y_pred) / len(y_true)
#     return accuracy

# clf = RandomForest(n_trees=20)
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
# result = pd.DataFrame({'Actual': y_test, 'Predict': predictions})

# # acc = accuracy(y_test, predictions)
# # print(acc)

# tp_rf, tn_rf, fp_rf, fn_rf = compute_tp_tn_fn_fp(y_test, predictions)
# # print('TP for Random Forest :', tp_rf)
# # print('TN for Random Forest :', tn_rf)
# # print('FP for Random Forest :', fp_rf)
# # print('FN for Random Forest :', fn_rf)

# acc = compute_accuracy(tp_rf, tn_rf, fn_rf, fp_rf)
# precision_ = compute_precision(tp_rf, fp_rf)
# recall = compute_recall(tp_rf, fn_rf)
# f1_score = compute_f1_score(y_test, predictions)
# print('Accuracy for Random Forest :', acc)
# print('Precision for Random Forest :', precision_)
# print('Recall for Random Forest :', recall)
# print('F1 score for Random Forest :', f1_score)
# arr=[acc, precision_, recall, f1_score]
# insertEvaluateData(arr)


i = "b2"
p = i+".txt"
f = open(p, 'r', encoding='UTF-8')
dt = f.read()
print(dt)
