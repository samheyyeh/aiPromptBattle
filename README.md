# promptBattleV2
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
    - Run python ''' -m venv venv ''' to create a virtual environment named 'venv'.
    - Activate the virtual environment:
      - Windows: ''' venv\Scripts\activate''' 
      - macOS/Linux: ''' source venv/bin/activate''' 
4. .env File Setup:
    - Ensure you have a .env file in the same directory. The file should contain:
    - ''' OPENAI_API_KEY = 'OpenAI api key goes here' '''



# Instructions for running an event
1. Run project using ''' flask run ''' after correctly setting up the virtual environment
2. Pick 4-6 audience members to be battlers (this is due to image generation limits)
    - Everyone else will be voting in the crowd 
3. Organizer will be the MC
    - MC’s computer will be projected onto a screen
    - On the MC home page, the organizer will either generate a random prompt, or write a custom one into the text box
    - Navigate to the current prompt screen to display the prompt
    - Then, once all generating is done, go back to the MC home page and then to the voting results page for final results
4. As the image generator:
    - Battlers will navigate to the battler home and then see the prompt
    - May need to refresh 
    - They will read the general prompt, then enter in theirs
    - Ex:
      - General prompt: Blend your favorite NBA player with a superhero
      - Battler’s prompt: Create a realistic image of Lebron James dunking, but flying through the air to a 50 ft tall hoop with a superman cape and costume
    - After writing the prompt, click the “submit” button
    - Battlers should wait around 30 seconds for images to generate, please do not click submit multiple times
    - After generation, click on the image the battler chooses to submit
5. As the crowd member:
    - Wait for the MC and Battlers to create finished artwork
    - Navigate to the voter home and click on the button that says “click to see voting choices” 
    - May need to refresh to see images
    - Voters will click on their favorite image! (remember to take the prompt into account)
