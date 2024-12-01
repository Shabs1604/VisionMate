# Langchain and Google Generative AI 
import streamlit as st
import pyttsx3
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

tts = pyttsx3.init()
# Function to speak text
def speak_text(text):
    try:
        tts.setProperty('rate', 150)  # Adjust speaking rate
        tts.say(text)
        tts.runAndWait()
    except RuntimeError as e:
        st.error(f"TTS Error: {e}")

# Function to stop reading
def stop_reading():
    try:
        if tts._inLoop:  
            tts.endLoop()
    except RuntimeError:
        pass  

# Load the API key for Google Generative AI
with open(r"C:\\Users\\LENOVO\Desktop\ds\\final_project\key.txt") as f:
    key = f.read().strip() 
    os.environ["GOOGLE_API_KEY"] = key

# Langchain Model
def generate_response(image):
  
    #Initializing Chat Model
    chat_model = ChatGoogleGenerativeAI(google_api_key = key, model="gemini-1.5-flash")

    message = HumanMessage(
        content=[
            {'type': 'text', 'text': '''
             "You are an advanced AI assistant designed to assist visually impaired individuals by providing highly accurate,accessible, and descriptive interpretations of images. Your primary goal is to help users understand their surroundings by analyzing images and providing clear and concise descriptions. Focus on the following tasks:"
    
    **👀🏞️Real-time Scene understanding:** [Describe the environment, location, objects, people, and background elements]
        
    **🧱Objects and Obstacles:** [Describe any obstacles detected in the scene, including relative size, location, and appearance]
     
    **📄Text Recognition and Details:** [If the image contains text (e.g., on signs, labels, or books), transcribe the text and explain its relevance. Provide assistance for task-specific guidance.]

    **⚠️Safety Considerations:** [Highlight any potential safety concerns or hazards visible in the scene]
   
    **📝Overall Summary:** [Provide a summary of the scene with a focus on the overall impression, taking into account all factors]
    
    **🦾Personal Assistance:** [Provide task-specific guidance based on the uploaded image]
                
    Always ensure your descriptions are helpful, accurate, and empowering for visually impaired users. Do not include unnecessary technical details or assumptions about people or contexts unless explicitly clear from the image.
    
    '''
    },
        {'type': 'image_url', 'image_url': image}
        ]
    )

    # Prompting the model for a description of the image (frame)
    try:
        # Get response from the chat model
        with st.spinner(":green[**Generating response...**]"):
            response = chat_model.invoke([message])
            response = response.get('content', 'No description available.') if isinstance(response, dict) else response
            response = response.content.strip()
       
        return response
    
    except Exception as e:
        st.error(f"Error processing image: {e}")
 




