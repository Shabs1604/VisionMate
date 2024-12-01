# Importing necessary libraries
import streamlit as st
import cv2
import time 
import base64
from VisionMate import generate_response,speak_text,stop_reading

# Initialize session state to track image and capturing state
if "captured_image" not in st.session_state:
    st.session_state.captured_image = None
if "capturing" not in st.session_state:
    st.session_state.capturing = True
if "response" not in st.session_state:
    st.session_state.response = None

# Video capturing using openCv
video = cv2.VideoCapture(0) 

# Placeholder for video frames
frame_placeholder = st.empty()

capture = st.button(":green[Capture]")

if capture:
    st.session_state.capturing = True
    start_time = time.time()

#Timer start
start_time = time.time()
captured_image  = None


# Loop to capture and display video frames
if st.session_state.capturing:
    ret, frame = video.read()

    if not ret:
        st.warning("Unable to access the camera.")
    else:   
         # Convert the frame from BGR (OpenCV default) to RGB (for Streamlit display)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in the Streamlit app
        frame_placeholder.image(frame, channels = "RGB")

        if capture or time.time() - start_time >= 5:
            cv2.imwrite("captured_image.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            st.session_state.captured_image = frame
            st.session_state.capturing = False
       

video.release()
cv2.destroyAllWindows()   

# Convert captured image to base64 for LangChain
if st.session_state.captured_image is not None:
     # Check if the response is already generated
    if "response" not in st.session_state or st.session_state.response is None:
        _, encoded_image = cv2.imencode('.jpg', cv2.cvtColor(st.session_state.captured_image, cv2.COLOR_RGB2BGR))
        img_base64 = f"data:image/jpeg;base64,{base64.b64encode(encoded_image).decode('utf-8')}"
    
        # Generate description for the image
        response = generate_response(img_base64)
        st.session_state.response = response

    response = st.session_state.response
    
    st.markdown(
    """
    <style>
    /* Style the default Streamlit button */
    div.stButton button {
        color: #bbe7fc;
        background-color: #4CAF50; 
        width : 150px;
        padding: 10px;
        border-color: white;
        border-radius: 10px;
        font-size : 100px;
        transition: all 0.3s ease;
    }
    /* On hover */
    div.stButton button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
    if response:

        # Displaying the response
        st.markdown(response)
       
        col1, col2, col3, col4 = st.columns(4)
        
        with col2:
            if st.button("Voice Assitant",  key="voice_button"):
                if st.session_state.captured_image is not None:
                    speak_text(response)

        with col3:
            if st.button("Stop Reading", key="stop-button"):
                stop_reading()
                st.success("Text-to-Speech has been stopped.")

    
