import streamlit as st
from VisionMate import speak_text

# Title and Subheader
st.markdown("<h1 style='text-align: center; color: green;'>Vision Mate</h1>", unsafe_allow_html=True)
st.markdown("<h3 style = 'text-align: center; '>Empowering every vision...</h3", unsafe_allow_html=True)

# Display an Image 
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.image("vision.jpg")


if "opened_home" not in st.session_state:
    st.session_state.opened_home = True
    speak_text("Opening VisionMate...")

# Custom CSS for Styling Buttons
st.markdown(
    """
    <style>
    /* Style the default Streamlit button */
    div.stButton button {
        color: #bbe7fc;
        background-color: rgba(100,255,255,0.2); /* Light transparent white background */
        height: 205px;
        width: 300px;
        margin: 10px;
        border-color: white;
        border-radius: 10px;
        font-size : 200px;
        transition: all 0.3s ease;
    }
    /* On hover */
    div.stButton button:hover {
        color: white;
        border-color: gray;
        box-shadow: inset 3px 3px 10px rgba(255, 255, 255, 0.5);
        width: 290px;
        height: 190px;
    }

       /* On active (click) */
    div.stButton button:active {
        background-color: green; /* Change background to green when clicked */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Button Layout
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Camera"):
            st.switch_page("pages/Camera.py")
    with col2:
        if st.button("Upload Image"):
            st.switch_page("pages/Upload.py")

# Centered "About" Button

with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2: 
        if st.button("About"):
            st.write("""
    **Vision Mate** is an AI-powered accessibility tool designed to analyze and describe scenes in real-time. By combining computer vision and advanced AI models, it empowers individuals with enhanced visual understanding.
    """)

st.markdown(
    """
    <style>
    .bottom-text {
        position: fixed;
        bottom: 10px; 
        left: 50%; 
        transform: translateX(-50%);  
        font-size: 18px;
        color: #bbe7fc;  
    </style>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <hr>
    <footer style="text-align:center;">
        <p>Powered by <strong>Google Gemini API </strong> | Shabeena </p>
    </footer>
    """,
    unsafe_allow_html=True,
)