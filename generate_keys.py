import pickle
from pathlib import Path

import streamlit_authenticator as stauth 

names = ["Peter Parker", "Bruce Wayne", "Clark Kent", "Tony Stark"]
usernames = ["spiderman", "batman", "superman", "ironman"]
passwords = ["peterparker", "brucewayne", "clarkkent", "tonystark"] # Not secure to store passwords in plain text

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)