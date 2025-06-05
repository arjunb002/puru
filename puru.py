import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Love Gallery", page_icon="❤️", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 15px 25px;
    }
    .stButton>button:hover {
        background-color: #ff1493;
    }
    .message-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffe4e1;
        margin: 10px 0;
    }
    @keyframes floatHearts {
      0% { transform: translateY(0) scale(1);}
      100% { transform: translateY(-300px) scale(1.5);}
    }
    .heart {
      position: fixed;
      bottom: 0;
      left: 50%;
      font-size: 2.5rem;
      color: #ff69b4;
      animation: floatHearts 3s ease-in infinite;
      z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

# Login functionality
def check_password():
    if st.session_state.get('logged_in', False):
        return True
    
    st.markdown("<h1 style='text-align: center; color: #ff69b4;'>❤️ Our Love Gallery ❤️</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    username = col1.text_input("Username")
    password = col2.text_input("Password", type="password")
    
    if col1.button("Login"):
        if username.lower() == "puru" and password.lower() == "puru":
            st.session_state['logged_in'] = True
            st.balloons()  # Show balloons animation on successful login
            return True
        else:
            st.error("Incorrect username or password")
            return False
    return False

if check_password():
    st.markdown("<h1 style='text-align: center; color: #ff69b4;'>Our Beautiful Moments Together ❤️</h1>", 
                unsafe_allow_html=True)
    
    # Create three columns
    col1, col2, col3 = st.columns([1, 1, 1])
    
    # Dictionary of images and their corresponding messages
    image_messages = {
        "1.jpg": "17th Novemeber 2024. It was a lovely day after playing football and you were to watch the match and i was very excited to see you. We had a nice dosa in the old Sri Krishna. ❤️",
        "2.jpg": "14th February 2025. You had a tiring day and when you layed your head in my shoulder I felt really a man. I would love to feel this anyday. Lovers Day. 💑",
        "3.jpg": "4th February 2025. Pongal Day and we had a nice day and a nice dance together. This pic remains so special to me as you are wearing my mom's saree.",
        "4.jpg": "8th March 2025. The day I came when you were sad. You called me and I was there in 20 mins. I love doing all this for you Puru. I love this pic.  🤗",
        "5.jpg": "11th April 2025. IPL day. Your first ever match. KKR won the match. You were happy. I felt really good after seeing you happy. ❤️",
        "6.jpg": "6th May 2025. The day before your flight. A good make out session. Very emotional day. Last time I dropped you at MSE. I love you. 💕",
        "7.jpg": "1st December 2024. The best pic man. Rainy day. Cake cutting that too waffle cake. We had a great time man. I love you 💑"
    }
    
    # Function to display image and message
    def show_image_message(image_path, message, column):
        try:
            column.image(image_path, use_container_width=True)
            if column.button(f"Click to see message 💌", key=image_path):
                column.markdown(f"""
                    <div class='message-box'>
                        <p style='text-align: center; font-size: 18px; color: #ff1493;'>
                            {message}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
        except:
            column.error(f"Unable to load {image_path}")
    
    # Display images in columns
    show_image_message("1.jpg", image_messages["1.jpg"], col1)
    show_image_message("2.jpg", image_messages["2.jpg"], col2)
    show_image_message("3.jpg", image_messages["3.jpg"], col3)
    
    col4, col5, col6 = st.columns([1, 1, 1])
    show_image_message("4.jpg", image_messages["4.jpg"], col4)
    show_image_message("5.jpg", image_messages["5.jpg"], col5)
    show_image_message("6.jpg", image_messages["6.jpg"], col6)
    
    # Last image centered
    col7, col8, col9 = st.columns([1, 1, 1])
    with col8:
        show_image_message("7.jpg", image_messages["7.jpg"], col8)
    
    # Footer
    st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background-color: #ffe4e1; border-radius: 10px;'>
            <h3 style='color: #ff1493;'>Forever Yours ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="heart">❤️</div>
        <div class="heart" style="left:55%;">💖</div>
        <div class="heart" style="left:45%;">💕</div>
    """, unsafe_allow_html=True)
