import streamlit as st
from auth.signup import show_signup_page 
from auth.login import show_login_page 
st.title("📘NoMoreCheat")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Login"

# Sidebar Navigation
page = st.sidebar.selectbox("Select Page", ["Signup", "Login", "Exam", "Result"])
index = ["Signup", "Login", "Exam", "Result"].index(st.session_state.page)

# ------------ Signup --------------
if page == "Signup":  
    show_signup_page()
    
#-------------Login------------------    
elif page=="Login":
    show_login_page()
    
elif page=="Exam":
    if not st.session_state.het("logged in",False):
        st.error("⚠️ Please login first to access the exam.")
    
    else:
        st.header("📝 Exam Page")
        st.write(f"welcome **{st.session_state.username}**!")
    

    
