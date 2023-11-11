import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np
from modules.magic import getRoots, load_css

st.set_page_config(
    page_title = 'Roots of Unity',
    layout = 'centered'
)

load_css()
st.title("Find i-th roots of r")

url = "https://github.com/DarkMortal/Jupyter-Notebooks/blob/main/DSA/Mathematics/Recursive%20Trigonometric%20Functions.ipynb"
st.markdown("### Check out this [Jupyter Notebook](%s)" % url)

i = st.number_input("Enter i",min_value = 1, max_value = 10)
r = st.number_input("Enter r",min_value = 1, max_value = 100)
p = st.number_input("Enter precision",min_value = 1, max_value = 7, value = 3)
gird_lines = st.checkbox("Show grid lines", value = True)

if st.button("Generate roots"):
    roots = getRoots(i, float(r), p)
    st.caption("## Roots")
    for l in range(len(roots)):
        root = str(roots[l])[1:-1]
        if i > 1:
            st.latex("\sqrt["+str(i)+"]{"+str(r)+"}\cos\\big(\\frac{"+str(2*l)+"\pi}{"+str(i)+"}\\big)+\sqrt["+str(i)+"]{"+str(r)+"}\sin\\big(\\frac{"+str(2*l)+"\pi}{"+str(i)+"}\\big)j = "+root)
        else:
            st.latex("\sqrt["+str(i)+"]{"+str(r)+"}\cos("+str(2*l)+"\pi)+\sqrt["+str(i)+"]{"+str(r)+"}\sin("+str(2*l)+"\pi)j = "+root)
        
    roots = np.array(roots)
    x = roots.real 
    # extract imaginary part using numpy array 
    y = roots.imag 

    # plot the complex numbers 
    plt.plot(x, y, 'g*')
    plt.ylabel('Imaginary') 
    plt.xlabel('Real')
    plt.grid(gird_lines)
    st.caption("## Graph")
    st.pyplot(plt)

st.markdown('<hr/>', unsafe_allow_html = True)
