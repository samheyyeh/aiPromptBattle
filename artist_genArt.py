#!/usr/bin/env python3

from openai import OpenAI
import urllib.parse
import cgi

IMAGE_SIZE  = '256x256'
NUM_OUTPUTS = 4

form = cgi.FieldStorage()
prompt = ''
if 'prompt' in form:
  prompt = form.getvalue('prompt')

userPrompt = ''
if 'userPrompt' in form:
  userPrompt = form.getvalue('userPrompt')

promptNumber = 0
if 'promptNumber' in form:
  promptNumber = form.getvalue('promptNumber')

client = OpenAI(api_key='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')

response = client.images.generate(
  model="dall-e-2",
  prompt=userPrompt,
  size=IMAGE_SIZE,
  quality="standard",
  n=NUM_OUTPUTS,
)

#imageURLs = ["http://localhost/1/cava.png"]

imageURLs = []
for image in response.data:
  imageURLs.append(image.model_dump()["url"])

print('Content-type: text/html\n\n');
print('<html><body>')

print(f'<h1>Prompt: {prompt}</h1>')
print(f'<h1>Your Prompt: {userPrompt}</h1>')
print('<br>')
print('<br>')
print('<h1>To submit your entry, click on the image that you like the best.</h1>')
print('<br>')
print('<br>')

for i, url in enumerate(imageURLs):
  encoded = urllib.parse.quote(url)
  print(f'<a href="artist_pick.py?promptNumber={promptNumber}&url={encoded}"><img src="{url}"></a>')
  print('<br>')
  print('<br>')
  print('<br>')

print('</body></html>')
