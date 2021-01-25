# to make it live in in replit use uptime robot
# and don't for get to make the flow lines of code in bot.py
# from keep_alive import keep_alive 
# and in befor the api keys insert   keep_alive()
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
