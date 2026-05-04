import streamlit as st

st.title("📫 Contact Me")

name = st.text_input("Ross-an Mahusay")
email = st.text_input("rossanmahusay8@gmail.com")
message = st.text_area("Message")

if st.button("Send") :
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill all fields.")

st.markdown("### 🌐 Social Link")
st.write("- Github: https://github.com/rossanmahusay8-cmyk")
st.write("- Facebook: https://www.facebook.com/rose.ann.mahusay.995952")