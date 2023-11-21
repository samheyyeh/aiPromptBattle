#!/usr/bin/env python3
import cgi
import sqlite3
import urllib.parse

print("Content-type: text/html\n")
print()

form = cgi.FieldStorage()
id = ''
if 'id' in form:
  id = form.getvalue('id')

randomNumber = 0
randomPromptStr = ''
with open('prompts/currentPrompt.txt', 'r') as file:
  randomNumberStr = file.readline()
  randomNumberStr = randomNumberStr.strip()
  randomNumber = randomNumberStr.split('=')[1]
  randomPromptStr = file.readline()
  randomPromptStr = randomNumberStr.strip()
  randomPrompt = bytes(randomPromptStr.split('=')[1], "utf-8").decode("unicode_escape")

con = sqlite3.connect('db/votes.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS votes(id INTEGER PRIMARY KEY, image TEXT NOT NULL, vote INTEGER NOT NULL, promptNumber INTEGER NOT NULL)''')
cur.execute('INSERT INTO votes(image, vote, promptNumber) VALUES(?,?,?)', (id,1,randomNumber))

path = f"../../promptbattle/results/{randomNumber}/{id}"
print(f"<img src = \"{path}\">")
print("<h1>You voted for this artwork</h1>") 
con.commit()

print("<html>")
print("<body>")
print('<a href="../promptbattle/voter_home.html">Home</a><br></br>')
print("</body>")
print("</html>")
