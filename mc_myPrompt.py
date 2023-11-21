#!/usr/bin/env python3
import cgi
import sqlite3
import shutil
import os

mcPromptNumber = 1000000
form = cgi.FieldStorage()
mcPrompt = ''
if 'mcPrompt' in form:
  mcPrompt = form.getvalue('mcPrompt')

filePath = "prompts/currentPrompt.txt"
with open(filePath, 'w') as newFile:
  newFile.write(f'randomNumber={mcPromptNumber}\n')
  newFile.write(f"randomPrompt='{mcPrompt}'") 

con = sqlite3.connect('db/votes.db')
cur = con.cursor()
cur.execute(f'''DELETE FROM votes WHERE promptNumber = {mcPromptNumber}''')
con.commit()
con.close()

resultsPath = '/var/www/html/promptbattle/results'
if os.path.isdir(f'{resultsPath}/{mcPromptNumber}'):
  shutil.rmtree(f'{resultsPath}/{mcPromptNumber}')

print('Content-type: text/html\n')
print()
print('<h1>Using the following prompt:</h1>')
print(f'{mcPrompt}</h1>')
