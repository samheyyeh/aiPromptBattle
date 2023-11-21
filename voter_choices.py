#!/usr/bin/env python3

import os
import urllib.parse

print("Content-type: text/html\n")
print()

randomNumber = 0
randomPromptStr = ''
with open('prompts/currentPrompt.txt', 'r') as file:
  randomNumberStr = file.readline()
  randomNumberStr = randomNumberStr.strip()
  randomNumber = randomNumberStr.split('=')[1]
  randomPromptStr = file.readline()
  randomPromptStr = randomNumberStr.strip()
  randomPrompt = bytes(randomPromptStr.split('=')[1], "utf-8").decode("unicode_escape")

print("<html>")
print("<body>")
print("<h1>Vote On Your Favorite</h1>")

path = f'/var/www/html/promptbattle/results/{randomNumber}'

if not os.path.isdir(path):
  print("<h2>No art generated yet</h2>")
  print(path)
else:
  imageIds = os.listdir(path)
  for imageId in imageIds:
    imageId = urllib.parse.quote(imageId)
    imagePath = f"../../promptbattle/results/{randomNumber}/{imageId}"
    print('<form action="voter_vote.py" method="post">')
    print(f"<img src=\"{imagePath}\">")
    print(f'<input type="submit" value="Vote">')
    print(f'<input type="hidden" id="sendId" name="id" value="{imageId}">')
    print("</form>")
    print("<br>")
    print("<br>")
    print("<br>")
    print("<br>")

print('<a href="../promptbattle/mc_home.html">Click here to go back to voter home</a><br></br>')
print("</body>")
print("</html>")
