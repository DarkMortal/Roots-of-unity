import streamlit as st
import matplotlib.pyplot as plt 
import numpy as np
from modules.magic import getRoots, load_css, cleaned

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

# graph config
is_circle = st.checkbox("Show circle", value = True)
gird_lines = st.checkbox("Show grid lines", value = False)

if st.button("Generate roots"):
    mag, roots = getRoots(i, float(r), p)
    st.caption("## Roots")
    for l in range(len(roots)):
        root = cleaned(roots[l])
        if i > 1:
            if r == 1:
                st.latex("\cos\\big(\\frac{"+str(2*l)+"\pi}{"+str(i)+"}\\big)+\sin\\big(\\frac{"+str(2*l)+"\pi}{"+str(i)+"}\\big)i = "+root)
            else:
                st.latex("\sqrt["+str(i)+"]{"+str(r)+"}\cos\\big(\\frac{"+str(2*l)+"\pi}{"+str(i)+"}\\big)+\sqrt["+str(i)+"]{"+str(r)+"}\sin\\big(\\frac{"+str(2*l)+"\pi}{"+str(i)+"}\\big)i = "+root)
        else:
            if r == 1:
                st.latex("\cos("+str(2*l)+"\pi)+\sin("+str(2*l)+"\pi)i = "+root)
            else:
                st.latex("\sqrt["+str(i)+"]{"+str(r)+"}\cos("+str(2*l)+"\pi)+\sqrt["+str(i)+"]{"+str(r)+"}\sin("+str(2*l)+"\pi)i = "+root)
        
    roots = np.array(roots)
    x = roots.real 
    y = roots.imag 

    plt.ylabel('Imaginary') 
    plt.xlabel('Real')
    plt.grid(gird_lines)
    plt.gca().set_aspect(1)

    if is_circle:
        circle = plt.Circle((0.0, 0.0), mag , fill = False )
        plt.gca().add_patch(circle)
    plt.plot(x, y, 'o')

    st.caption("## Graph")
    st.pyplot(plt)

st.markdown('<hr/>', unsafe_allow_html = True)
