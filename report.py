import streamlit as st 
from PIL import Image

st.title('TAR Prep School Report')
image = Image.open('reportcard.png')
st.image(image)

readme = st.checkbox("README First")

if readme:

    st.write("""
        **Critical information for this web app demo are shown below:**
        \n * Author: [Lim Huei Tsuen]()
        \n * Host & Libraries: [Streamlit](https://streamlit.io/)
        \n * Code Repository: [Github]()
        """)

st.sidebar.write("""
This is a web app to check the outcome of your report card scores
""")

st.sidebar.write("Please enter the score you obtained")

y = 50 # minimum passing score

while True:
  
  x = input("Please enter your mark. To stop the algorithm, enter x .\n\n")
  
  if x=="x":
    print ("\nThank you for using our service.\n")
    break
  else:
    try:
      val = int(x)
      if (val > 100 or val < 0):
            print("\nPlease enter a valid mark.\n")
                
      elif val >= y:
            print("\nYou passed your exam. Keep it up!\n")
      else:
            print("\nUnfortunately, you did not pass your exam. Work harder. You can make it.\n")

    except ValueError:
            print("\nPlease enter a number.\n")
