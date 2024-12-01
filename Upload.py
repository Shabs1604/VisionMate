import streamlit as st
from PIL import Image
import base64
import io
from VisionMate import generate_response, speak_text, stop_reading

# Initialize session states
if "upload_response" not in st.session_state:
    st.session_state.upload_response = None

if "uploaded_image" not in  st.session_state:
   st.session_state.uploaded_image = None  

if "voice_active" not in st.session_state:
    st.session_state.voice_active = False

if "response_generated" not in st.session_state:
    st.session_state.response_generated = False


# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    if uploaded_image != st.session_state.uploaded_image:
        st.session_state.uploaded_image = uploaded_image
        st.session_state.upload_response = None
        st.session_state.response_generated = False

if st.session_state.uploaded_image is not None:   
    # Open the uploaded image using PIL
    image = Image.open(st.session_state.uploaded_image)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image")

    # Check if response is already generated for this upload
    if not st.session_state.response_generated or st.session_state.upload_response is None:
        # Converting image to bytes for base64 encoding
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()
        img_base64 = f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"

        # Generate response for the image
        st.session_state.upload_response = generate_response(img_base64)
        st.session_state.response_generated = True 

    response = st.session_state.upload_response  
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
        with st.container(height=100, border=False):
            col1, col2, col3, col4 = st.columns(4)
            with col2:
                if st.button("🎤 Voice Assistant", use_container_width=True):
                    st.session_state.voice_active = True
                    speak_text(response)

            with col3:
                if st.button("🛑 Stop Reading", use_container_width=True):
                    st.session_state.voice_active = False
                    stop_reading()
                    st.success("Voice Assistant stopped!")


