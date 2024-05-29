import streamlit as st
import random

# タイトル
st.title("beatmania IIDX DP オプションおみくじ")

# オプションのリスト
options = ["正規", "MIRROR", "RANDOM", "R-RANDOM", "S-RANDOM"]
flip_options = ["FLIP: ON", "FLIP: OFF"]

# ボタンを押すと表示
if st.button("おみくじを引く"):
    selected_options = random.sample(options, 2)
    selected_flip = random.choice(flip_options)
    
    st.write("選ばれたオプション:")
    st.write(f"1P Side")
    st.write(f"{selected_options[0]}")
    st.write(f"2P Side")
    st.write(f"{selected_options[1]}")
    st.write(f"{selected_flip}")

