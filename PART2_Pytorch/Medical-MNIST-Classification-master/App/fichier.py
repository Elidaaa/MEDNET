import streamlit as st
from model_fonction import predict_img



st.set_page_config(
    page_title="MedNet",
    page_icon="🖥",
    layout="wide"
)

hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style = 'text-align : center'> MedNet </h1>", unsafe_allow_html=True)

container1 = st.container()

with container1:
    uploaded_files = st.file_uploader(
        "", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])
    
    if uploaded_files is not None:
        liste_image = []
        liste_name = []

        for uploaded_file in uploaded_files:
            liste_image.append(uploaded_file)
            liste_name.append(uploaded_file.name)



container2 = st.container()

with container2:
     col1, col2, col3, col4 = st.columns(4)

     with col1:
        st.markdown("<h3> Images </h3>", unsafe_allow_html=True)
        for image in liste_image:
            st.image(image, width= 150)


     with col2:
        st.markdown("<h3 style = 'text-align : center'> Image Names </h3>", unsafe_allow_html=True)
        for name in liste_name:
            st.markdown(f"<h5 style='color: black; text-align: center; margin-bottom: 70px; margin-top: 50px'> {name} </h5>",
            unsafe_allow_html=True)
     

     with col3:
        st.markdown("<h3 style = 'text-align : center'> XRay Class ID </h3>", unsafe_allow_html=True)
        for image in liste_image:
           test1, test2 = predict_img(image)
           st.markdown(f"<h5 style='color: black; text-align: center; margin-bottom: 70px; margin-top: 50px'> {test2} </h5>",
            unsafe_allow_html=True)



     with col4:
        st.markdown("<h3 style = 'text-align : center'> Detected XRay Class </h3>", unsafe_allow_html=True)
        for image in liste_image:
           test1, test2 = predict_img(image)
           st.markdown(f"<h5 style='color: black; text-align: center; margin-bottom: 70px; margin-top: 50px;'> {test1} </h5>",
            unsafe_allow_html=True)






