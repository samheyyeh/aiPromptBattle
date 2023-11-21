#!/usr/bin/env python3

import cgi
import os
import requests

PATH_RESULTS = "/var/www/html/promptbattle/results"

def downloadImage(url, localDir):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      filename = os.path.basename(url)
      localPath = os.path.join(localDir, filename)
      with open(localPath, 'wb') as file:
        file.write(response.content)
    else:
        print(f'Failed to download the image {response.status_code}')
  except Exception as e:
    print(f"An error occurred: {e}")

print('Content-type: text/html\n\n');
print('<html><body>')

print('<h1>You chose the picture below. Good luck!</h1>')
print('<br>')

form = cgi.FieldStorage()

if 'url' in form:
  url = form.getvalue('url')
  print(f'<img src="{url}">')

promptNumber = 0
if 'promptNumber' in form:
  promptNumber = form.getvalue('promptNumber')

localDir = os.path.join(PATH_RESULTS, promptNumber)

try:
  os.mkdir(localDir)
except FileExistsError as err:
  pass

downloadImage(url, localDir)

print('<br></br><a href="../promptbattle/voter_home.html">Click here to go back to voter home</a><br></br>')
print('</body></html>')
