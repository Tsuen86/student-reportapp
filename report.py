import streamlit as st 
from PIL import Image

st.title('TAR Prep School Report')
image = Image.open('report21.gif')
st.image(image)

st.sidebar.write("""
This is a web app to check the outcome of your report card scores
""")

readme = st.sidebar.checkbox("README First")

if readme:

    st.sidebar.write("""
        **Critical information for this web app demo are shown below:**
        \n * Author: [Lim Huei Tsuen](https://www.linkedin.com/in/huei-tsuen-lim-89225536/)
        \n * Co-author: [Dr. Yong Poh Yu](https://www.linkedin.com/in/yong-poh-yu/)
        \n * Host & Libraries: [Streamlit](https://streamlit.io/)
        \n * Code Repository: [Github](https://github.com/Tsuen86/student-reportapp/)
        """)
y = 50

st.header("Please enter the score you obtained.")

st.subheader("To stop the algorithm, enter x .\n\n")

mark = st.text_input('Enter the mark here', '50')

try:
    val = float(mark)
            
    if (val > 100 or val < 0):
        st.write("\nPlease enter a valid mark.\n")
                
    elif val >= y:
        st.write("\nYou passed your exam. Keep it up!\n")
       
    else:
        st.write("\nUnfortunately, you did not pass your exam. Work harder. You can make it.\n")

            
except ValueError:
    st.write("\nPlease enter a number.\n")
