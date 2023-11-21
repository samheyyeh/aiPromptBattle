#!/usr/bin/env python3
import random
import sqlite3
import shutil  
import os

filePath = "prompts/prompts.txt"

with open(filePath, 'r') as file:
  prompts = file.read().splitlines()

randomNumber = random.randint(0, len(prompts) - 1)
randomPrompt = prompts[randomNumber]

newFilePath = "prompts/currentPrompt.txt"

with open(newFilePath, 'w') as newFile:
  newFile.write("randomNumber={}\n".format(randomNumber))
  newFile.write("randomPrompt='{}'\n".format(randomPrompt))

con = sqlite3.connect('db/votes.db')
cur = con.cursor()
cur.execute(f'''DELETE FROM votes WHERE promptNumber = {randomNumber}''')
con.commit()
con.close()

resultsPath = '/var/www/html/promptbattle/results'
if os.path.isdir(f'{resultsPath}/{randomNumber}'):
  shutil.rmtree(f'{resultsPath}/{randomNumber}')

print('Content-type: text/html\n')
print()
print('<html><body><title>Current Prompt</title>')
print('<h1>Using the following prompt:</h1>')
print(f'<h1>{randomPrompt}</h1>')
print('<a href="../promptbattle/mc_home.html">Click here to go back to MC home</a><br></br>')
print('</body></html>')
