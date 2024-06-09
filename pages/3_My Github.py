import streamlit as st

st.write("# Here's the link to my GitHub profile :)")

st.image('https://avatars.githubusercontent.com/u/92550537?s=400&u=065eef8f39cf937a2a75eff0c66a63205e872485&v=4')

st.link_button("Go to my GitHub", "https://github.com/aaeeii16", help=None, type="secondary", disabled=False, use_container_width=False)