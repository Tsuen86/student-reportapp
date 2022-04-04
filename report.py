import streamlit as st 
from PIL import Image
        
st.header('BOOKWORM\'S PREP SCHOOL:')
st.subheader('Report Check')

image = Image.open('report.png')
if image.mode != 'RGB':
    img = image.convert('RGB')
st.image(img)

st.sidebar.write("""
This is a web app to check the pass/ fail outcome of your report card marks.
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
y = 50 # minimum passing score

st.subheader("Please submit your marks for pass/ fail check:\n\n")

mark = st.text_input('Enter the mark here', '50')

try:
    val = float(mark)
         
    if (val > 100 or val < 0):
        st.write("\nPlease enter a valid mark.\n")
                
    elif val == y:
        st.write("\nYou've just made the passing grade.\n"
                 "\nYou can do better next time!\n")
        
    elif val > y:
        st.write("\nYou passed your exam. Keep it up!\n")
       
    else:
        st.write("\nUnfortunately, you failed your exam.\n" 
                 "\nPlease work harder, you can make it!\n")

            
except ValueError:
    st.write("\nPlease enter a number.\n")
