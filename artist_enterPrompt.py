#!/usr/bin/env python3

randomNumber = 0
randomPromptStr = ''
with open('prompts/currentPrompt.txt', 'r') as file:
  randomNumberStr = file.readline()
  randomNumber = randomNumberStr.split('=')[1]
  randomPromptStr = file.readline()
  randomPrompt = bytes(randomPromptStr.split('=')[1], "utf-8").decode("unicode_escape")

htmlContent = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Enter Your Prompt</title>
</head>
<body>
    <h1>Prompt: {randomPrompt}</h1>
    <font size=20>
        <form action="artist_genArt.py" method="post">
        <label for="userPrompt">Enter Your Prompt below:</label>
        <br>
        <textarea rows="10" cols="80" id="userPrompt" name="userPrompt">
        </textarea>
<br><br>
        <input type="submit" value="Submit">
	<input id="sendNumber" type="hidden" name="promptNumber" value={randomNumber}>
	<input id="sendPrompt" type="hidden" name="prompt" value="{randomPrompt}">
        </form>
    </font>
    <h2>Masterpieces may take up to 30 seconds to generate</h2>
    <a href="../promptbattle/artist_home.html">Click here to go back to battler home</a><br></br>
</body>
</html>
''' 

print("Content-type: text/html\n")
print(htmlContent)
