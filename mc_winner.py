#!/usr/bin/env python3
import sqlite3
import urllib.parse

print("Content-type: text/html\n")
print()

con = sqlite3.connect('db/votes.db') 
cur = con.cursor()

randomNumber = 0
randomPromptStr = ''
with open('prompts/currentPrompt.txt', 'r') as file:
  randomNumberStr = file.readline()
  randomNumber = randomNumberStr.split('=')[1]
  randomPromptStr = file.readline()
  randomPrompt = bytes(randomPromptStr.split('=')[1], "utf-8").decode("unicode_escape")

def findWinner():
  cur.execute(f"SELECT image, COUNT(*) FROM votes WHERE promptNumber = {randomNumber} GROUP BY image ORDER BY COUNT(*) DESC")
  rows = cur.fetchall()
  for image in rows:
    id, vote = image
    path = f"../../promptbattle/results/{randomNumber}/{id}"
    print(f"<img src=\"{path}\">")
    print(f"<h1>{vote} Vote(s)</h1>")
  return(len(rows))

con.commit()

print("<html>")
print("<body>")
if findWinner() == 0:
  print("<h1>No votes yet</h1>")
print('<a href="../promptbattle/mc_home.html">Click here to go back to MC home</a><br></br>')
print("</body>")
print("</html>")
