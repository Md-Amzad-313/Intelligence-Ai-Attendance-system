import streamlit as st
from src.ui.base_layout import style_background_dashboard,style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher_exists,create_teacher,teacher_login

def teacher_screen():
  
  style_background_dashboard()
  style_base_layout()
  
 
  if "teacher_data" in st.session_state:
    teacher_dashboard()
  elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
    teacher_screen_login()
  elif st.session_state.teacher_login_type=="register":
    teacher_screen_register()
  
def teacher_dashboard():
   teacher_data=st.session_state.teacher_data
   st.header(f"""Welcome , { teacher_data['name']}""")


def login_teacher(username,password):
  if not username or not password:
    return False
  
  teacher=teacher_login(username,password)
  
  if teacher:
    st.session_state.userrole="teacher"
    st.session_state.teacher_data=teacher
    st.session_state.is_logged_in=True
    return True 
    
    
    return False
  
  
def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home",type='secondary',key='loginbackbtn',shortcut='control+backspace'):
          st.session_state['login_type']=None
          st.rerun()
        
        
        
    st.header('login using password',text_alignment='center')
    st.space()
    st.space()
    
    techer_username=st.text_input("Enter Username",placeholder='Amzad Shaikh')
    teacher_password=st.text_input("Unter Password",type='password',placeholder="Enter password")
    
    st.divider()
    
    btnc1,btnc2=st.columns(2)
    with btnc1:
      if st.button('Login',icon=':material/passkey:',shortcut='control+enter',width='stretch'):
        if login_teacher(techer_username, teacher_password):
          st.toast("Welcome back!",icon="👋")
          import time 
          time.sleep(1)
          st.rerun()
          
        st.error("Invalid username and password combo")
    
    with btnc2:
          if st.button('Register Instead',icon=':material/passkey:',width='stretch',type='primary'):
            st.session_state.teacher_login_type='register'
    
    footer_dashboard()
    
    
def register_teacher(teacher_userame,teacher_name,teacher_pass,teacher_pass_confirm):
   if not teacher_userame or not teacher_name or not teacher_pass:
     return False,"All fields are require"
   
   if check_teacher_exists(teacher_userame):
     return False, "Username already taken"
   
   if teacher_pass !=teacher_pass_confirm:
     return False,"password don't match"
   
   try:
     create_teacher(teacher_userame,teacher_pass,teacher_name)
     return True,"Susseccfully created! Login Now"
   except Exception as e:
     return False,"Unexpected Error"
     
       
def teacher_screen_register():
    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home",type='secondary',key='loginbackbtn',shortcut='control+backspace'):
          st.session_state['login_type']=None
          st.rerun()
        
        
        
    st.header('register your teacher profile')
    st.space()
    st.space()
        
    techer_username=st.text_input("Enter Username",placeholder='amzadshaikh')
    techer_name=st.text_input("Enter name",placeholder='Amzad Shaikh')
    teacher_password=st.text_input("Enter Password",type='password',placeholder="Enter password")
    teacher_password_confirm=st.text_input("Confirm your Password",type='password',placeholder="Confirm password")
        
    st.divider()
        
    btnc1,btnc2=st.columns(2)
    with btnc1:
      if st.button('Register Now',icon=':material/passkey:',shortcut='control+enter',width='stretch'):
        success, message = register_teacher(
    techer_username,
    techer_name,
    teacher_password,
    teacher_password_confirm
    )
        if success:
          st.success(message)
          import time
          time.sleep(2)
          st.session_state.teacher_login_type="login"
          st.rerun()
        else:
          st.error(message)
          
    with btnc2:
      if st.button('login Instead',icon=':material/passkey:',width='stretch',type='primary'):
        st.session_state.teacher_login_type='login'
        
    footer_dashboard()