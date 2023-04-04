import pickle
from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np

import streamlit_authenticator as stauth

# --- Authentication ---
names = ["Peter Parker", "Bruce Wayne", "Clark Kent", "Tony Stark"]
usernames = ["spiderman", "batman", "superman", "ironman"]

# Load hashed passwords from file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status,usernames = authenticator.login("เข้าสู่ระบบ","main")

if authentication_status == False:
    st.error("คุณไม่ได้รับอนุญาตให้เข้าถึงหน้านี้")

if authentication_status == None:
    st.warning("กรุณาเข้าสู่ระบบ")

if authentication_status == True:
    st.success("ยินดีต้อนรับคุณ {}".format(name))


    # --- sidebar ---
    authenticator.logout("ออกจากระบบ","sidebar")
    st.sidebar.title(f"Welcome {name}")
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'คุณต้องการติดต่อช่องทางใด',
        ('เบอร์โทรศัพท์', 'อีเมล์', 'เฟสบุ๊ค')
    )


    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'เลือกช่วงของข้อมูล',
        0.0, 100.0, (25.0, 75.0)
    )


    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('คลิกที่นี่')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'หมวกเลือกบ้านใด',
            ('Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'))
        st.write('คุณเลือกบ้าน', chosen)

    







