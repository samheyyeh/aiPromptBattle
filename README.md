# Project Description
Check out this exciting AI Prompt Battle project I've been working on. Users can unleash their creativity, generating unique images through DALL-E, and then battle them out on our platform powered by Flask. Join the fun, showcase your artistic flair, and compete with others in this innovative and visually captivating experience! 

# Technologies and Architecture
- Backend: Python using the flask library
- Image Generation: DALLE
- Frontend: jinja

# Setup Instructions
1. Install Python: Ensure Python is installed on your computer. Download it from the Python website
2. Clone the Repository: Download the project code to your local machine. 
3. Create a Virtual Environment (optional but recommended):
    - Navigate to the project directory.
    - Run ``` python3 -m venv venv ``` to create a virtual environment named 'venv'.
    - Activate the virtual environment:
      - Windows: ``` venv\Scripts\activate ```
      - macOS/Linux: ```  source venv/bin/activate ```
4. .env File Setup:
    - Ensure you have a ``` .env ``` file in the same directory. The file should contain:
    - ``` OPENAI_API_KEY = 'OpenAI api key goes here' ```
5. Install Dependencies:
    - Ensure the virtual environment is active.
    - Run ``` pip install -r requirements.txt ``` to install required packages.
6. Start the Flask Server:
    - Run ``` flask run ``` to start the server.
    - Access the application at ``` localhost:5000 ```

# Running the event
1. After correctly running the project, you can start the event!
2. Pick 4-6 audience members to be battlers (this is due to image generation limits)
    - Everyone else will be voting in the crowd 
3. Organizer will be the MC
    - Navigate to ``` localhost:5000/mc/genPrompt ``` for the first screen 
    - MC’s computer will be projected onto a screen
    - Click ``` Generate Prompt ``` and now wait for the battlers to generate
5. As the image generator:
    - Navigate to ``` localhost:5000/artist/enterPrompt ```
    - They will read the general prompt, then enter in theirs
    - Ex:
      - General prompt: Blend your favorite NBA player with a superhero
      - Battler’s prompt: Create a realistic image of Lebron James dunking, but flying through the air to a 50 ft tall hoop with a superman cape and costume
    - After writing the prompt, click the “submit” button
    - Battlers should wait around 30 seconds for images to generate, please do not click submit multiple times
    - After generation, click on the image the battler chooses to submit
7. As the crowd member:
    - Navigate to ``` localhost:5000/voter/choices ```
    - May need to refresh to see images
    - Voters will click on their favorite image!

# Important Reminders 
- This project uses a ``` .env ``` file, so remember to set this up correctly with your OpenAI API key
- Navigate to ``` localhost:5000 ``` for the home screen
- When running an event, be careful of rate limits
- Send any feedback to ``` samheyyeh@gmail.com ```
