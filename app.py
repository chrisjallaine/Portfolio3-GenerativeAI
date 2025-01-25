import streamlit as st
from dotenv import load_dotenv
from utils import generate_script

# Load environment variables
load_dotenv()

# Custom CSS for enhanced design with pastel colors
custom_css = """
<style>
/* Global styling */
body {
    font-family: 'Inter', sans-serif;
    background: #F6F6F9; /* Light background color */
    margin: 0;
    padding: 0;
    color: #333;
}

/* Title and Headers */
h1, h2, h3, h4, h5, h6 {
    color: #FFB6C1; /* Soft pastel pink */
    font-weight: 600;
}

/* Sidebar Styling */
.sidebar .sidebar-content {
    background-color: #FADADD; /* Pastel pink for sidebar */
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* Buttons */
.stButton>button {
    background-color: #FFB6C1; /* Soft pastel pink */
    color: white;
    font-size: 16px;
    border-radius: 10px;
    border: none;
    padding: 12px 20px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
}

.stButton>button:hover {
    background-color: #FF9B97; /* Darker pastel pink on hover */
    transform: translateY(-2px);
}

.stButton>button:active {
    transform: translateY(2px);
}

/* Input Fields */
.stTextInput>div>input, .stNumberInput>div>input, .stSlider>div>div>div {
    border-radius: 8px;
    padding: 12px;
    border: 1px solid #ddd;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
}

/* Container for the input fields */
.container {
    background: #ffffff;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

/* Expander Styling */
.stExpander {
    background-color: #FFB6C1; /* Soft pastel pink for the expander */
    padding: 12px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Adjusting radio button labels */
.stRadio>div>label {
    background-color: #FFB6C1; /* Soft pastel pink */
    border-radius: 10px;
    padding: 8px 20px;
    color: #333;
    font-weight: 500;
    margin: 5px;
    transition: background-color 0.3s;
}

.stRadio>div>label:hover {
    background-color: #FF9B97; /* Darker pastel pink on hover */
}

/* Styling the sliders */
.stSlider>div>div>div {
    background-color: #FFB6C1; /* Soft pastel pink */
    border-radius: 10px;
    padding: 8px 15px;
    color: white;
}

/* Input field focus styling */
input:focus, .stSlider>div>div>div:focus {
    border-color: #FFB6C1;
    box-shadow: 0 0 5px rgba(255, 182, 193, 0.5);
}
</style>
"""

# Inject custom CSS into Streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# App title and header
st.title("✨ YouTube Scriptwriting Tool")
st.header("Generate a video script by specifying a topic, length, and creativity level.")

# Sidebar to capture API key
st.sidebar.title("🔐 API Configuration")
st.sidebar.text_input("Enter your OpenAI API key:", type="password", key="api_key")

# Main input fields for the video script
prompt = st.text_input("📝 Provide the topic of the video:")
video_length = st.number_input("⏱️ Specify video length (in minutes):", min_value=1.0, step=0.5)
creativity = st.slider("🎨 Set creativity level:", min_value=0.0, max_value=1.0, value=0.5)

# Button to generate the script
generate_script_button = st.button("🚀 Generate Script")

# When the button is clicked, the script will be generated
if generate_script_button:
    api_key = st.session_state.api_key
    if not api_key:
        st.error("❌ Please provide a valid OpenAI API key.")
    else:
        # Generate the script using the utility function
        title, script, search_data = generate_script(prompt, video_length, creativity, api_key)
        st.success("✅ Script generated successfully!")
        st.subheader(f"📖 Title: {title}")
        st.write(f"Script:\n\n{script}")
        with st.expander("🔍 Show search data used for the script"):
            st.write(search_data)
