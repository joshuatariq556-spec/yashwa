#pip install streamlit 

import streamlit as st

page_by_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url ("http://eskipaper.com/images/background-images-5.jpg");
    background-size: cover;
    background-repeta: on-repeta;
    background-attachedment: fixed;
}    

[data-testid="stHeder"]{
    background: rgba(0,0,0,0);
}    

[data-testid ="stToolbar"]{
    right: 2rem;
}
</style>
"""

st.markdown(page_by_img, unsafe_allow_html=True)




tab1, tab2, tab3 = st.tabs(['Home','junior','senior'])
