import streamlit as st

def show_login_page():
    st.header("Login Page")
    username=st.text_input("Username/E-mail")
    password=st.text_input("Password",type="password")
    btn=st.button("Login")
    
    if username=="" or password=="":
        st.error("⚠️ Username and Password required! to Login")
        
    else:
        st.success(f"✅ Account created for {username} (demo)")
    