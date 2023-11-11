from streamlit import markdown as md
from modules.recursive import sine as sin, cosine as cos, to_radians, root

def getRoots(i:int, r:float, precision = 3) -> []:
    div = 360.0 / i
    
    mag = root(r, i)
    roots = []

    for n in range(i):
        angle = to_radians(div * n)
        real = mag * cos(angle)
        img = mag * sin(angle)
        roots.append(complex(round(real, precision),round(img, precision)))

    return (mag, roots)

def load_css(filepath = "./styles/styles.css"):
    with open(filepath) as file:
        md(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def cleaned(c:complex) -> str:
    if c.imag == 0 and c.real == 0:
        return "0"
    if c.imag == 0:
        return str(c.real)
    if c.real == 0:
        return f"{str(c.imag)}i"
    return str(c).replace('(','').replace(')','').replace('j','i')