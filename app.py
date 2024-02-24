import random
import string
import os
import urllib.parse
import requests
import sqlite3
from dotenv import load_dotenv
from flask import Flask
from flask import render_template
from flask import request
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def home():
  htmlString = render_template('home.html')
  return htmlString

@app.route('/mc/genPrompt')
def genPrompt():
  filePath = "prompts/prompts.txt"

  with open(filePath, 'r') as file:
    prompts = file.read().splitlines()

    randomPromptId = random.randint(0, len(prompts) - 1)
    randomPrompt = prompts[randomPromptId]

    newFilePath = "prompts/currentPrompt.txt"

  with open(newFilePath, 'w') as newFile:
    newFile.write("promptId={}\n".format(randomPromptId))
    newFile.write("randomPrompt='{}'\n".format(randomPrompt))

  htmlString = render_template('genPrompt.html', randomPrompt = randomPrompt)
  return htmlString

def getPromptIndexAndPrompt():
  randomPromptIndex = 0
  randomPromptStr = ''

  with open('prompts/currentPrompt.txt', 'r') as file:
    randomPromptIndexStr = file.readline().strip()
    randomPromptIndex = randomPromptIndexStr.split('=')[1]
    randomPromptStr = file.readline()
    randomPrompt = bytes(randomPromptStr.split('=')[1], "utf-8").decode("unicode_escape")

  return (randomPromptIndex, randomPrompt)

@app.route('/artist/enterPrompt', methods=['GET', 'POST'])
def enterPrompt():
  (randomPromptIndex, randomPrompt) = getPromptIndexAndPrompt()

  htmlString = render_template('enterPrompt.html', randomPrompt = randomPrompt, randomPromptIndex = randomPromptIndex)
  return htmlString

@app.route('/artist/genArt', methods=['GET', 'POST'])
def genArt():
  IMAGE_SIZE = '512x512'
  NUM_OUTPUTS = 2

  load_dotenv()
  openApiKey = os.getenv('OPEN_API_KEY')

  (randomPromptIndex, randomPrompt) = getPromptIndexAndPrompt()

  if request.method == 'POST':
    userPrompt = request.form.get('userPrompt', '')

  client = OpenAI(api_key=openApiKey)

  imageURLs = []

  try:
    response = client.images.generate(
      model="dall-e-2",
      prompt=userPrompt,
      size=IMAGE_SIZE,
      quality="standard",
      n=NUM_OUTPUTS,
    )
    for image in response.data:
      imageURLs.append(image.model_dump()["url"])

  except Exception as e:
    print(f'error: {e}')

  encodedURLs = []
  for i, url in enumerate(imageURLs):
    encodedURLs.append(urllib.parse.quote(url))

  htmlString = render_template('genArt.html', randomPrompt = randomPrompt, userPrompt = userPrompt, randomPromptIndex = randomPromptIndex, encodedURLs = encodedURLs, imageURLs = imageURLs)
  return htmlString

@app.route('/artist/pick', methods=['GET', 'POST'])
def pick():
  PATH_RESULTS = "static/images"

  (randomPromptIndex, randomPrompt) = getPromptIndexAndPrompt()
  url = ''
  if request.method == 'GET':
    url = request.args.get('url')

  localDir = os.path.join(PATH_RESULTS, randomPromptIndex)

  try:
    os.mkdir(localDir)
  except FileExistsError:
    pass
  except Exception as e:
    print(f"An error occurred while created the directory: {e}")

  downloadImage(url, localDir)

  htmlString = render_template('pick.html', url = url)
  return htmlString

def downloadImage(url, localDir):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      filename = os.path.basename(url)
      localPath = os.path.join(localDir, filename)
      with open(localPath, 'wb') as file:
        file.write(response.content)
    else:
      return f'Failed to download image {response.status_code}'
  except Exception as e:
    print(f"An error occurred: {e}")

@app.route('/voter/choices', methods=['GET', 'POST'])
def choices():
  (randomPromptIndex, randomPrompt) = getPromptIndexAndPrompt()

  path = f'static/images/{randomPromptIndex}'

  imagePaths = []
  imageIds = []
  if os.path.isdir(path):
    imageIds = os.listdir(path)
    for imageId in imageIds:
      imageId = urllib.parse.quote(imageId)
      imagePaths.append(f"../../static/images/{randomPromptIndex}/{imageId}")

  htmlString = render_template('choices.html', imagePaths = imagePaths, imageIds = imageIds)
  return htmlString

@app.route('/voter/vote', methods=['POST', 'GET'])
def vote():
  (randomPromptIndex, randomPrompt) = getPromptIndexAndPrompt()

  id = ''
  if request.method == 'POST':
    id = request.form.get('id', '')
    id = urllib.parse.quote(id)

  # instead of absolute path can do this trick
  sqlitePath = os.path.dirname(os.path.realpath(__file__))
  con = sqlite3.connect(os.path.join(sqlitePath, "votes.db"))
  cur = con.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS votes(id INTEGER PRIMARY KEY, image TEXT NOT NULL, vote INTEGER NOT NULL, promptNum INTEGER NOT NULL)''')
  cur.execute('INSERT INTO votes(image, vote, promptNum) VALUES(?,?,?)', (id,1,randomPromptIndex))
  con.commit()

  path = f'../../static/images/{randomPromptIndex}/{id}'

  htmlString = render_template('vote.html', path = path)
  return htmlString

@app.route('/mc/winner', methods=['POST', 'GET'])
def winner():
  (randomPromptIndex, randomPrompt) = getPromptIndexAndPrompt()

  sqlitePath = os.path.dirname(os.path.realpath(__file__))
  con = sqlite3.connect(os.path.join(sqlitePath, "votes.db"))
  cur = con.cursor()
  cur.execute(f"SELECT image, COUNT(*) FROM votes WHERE promptNum = {randomPromptIndex} GROUP BY image ORDER BY COUNT(*) DESC")
  rows = cur.fetchall()
  paths = []
  votes = []
  for row in rows:
    image, vote = row
    #image = row[0]
    #vote = row[1]
    paths.append(f'../../static/images/{randomPromptIndex}/{image}')
    votes.append(vote)

  con.commit()

  htmlString = render_template('winner.html', paths = paths, votes = votes)
  return htmlString
