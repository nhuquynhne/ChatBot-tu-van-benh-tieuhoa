# from flask import Flask, render_template, request
# # from chatterbot import ChatBot
# # from chatterbot.trainers import ChatterBotCorpusTrainer

# # import mysql.connector
# # from mysql.connector import Error
# #
# # try:
# #     connection = mysql.connector.connect(host='localhost',
# #                                          database='btlhtdttt',
# #                                          user='root',
# #                                          password='123456')
# #     if connection.is_connected():
# #         db_Info = connection.get_server_info()
# #         print("Connected to MySQL Server version ", db_Info)
# #         cursor = connection.cursor()
# #         cursor.execute("select database();")
# #         record = cursor.fetchone()
# #         print("You're connected to database: ", record)
# #
# # except Error as e:
# #     print("Error while connecting to MySQL", e)
# # finally:
# #     if connection.is_connected():
# #         cursor.close()
# #         connection.close()
# #         print("MySQL connection is closed")

# app = Flask(__name__)

# # english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# # trainer = ChatterBotCorpusTrainer(english_bot)
# # trainer.train("chatterbot.corpus.english")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     print(userText)
#     str = "xin chao"
#     return str
#     # return str(english_bot.get_response(userText))


# if __name__ == "__main__":
#     app.run()


def tinh(a, b):
    return a+b