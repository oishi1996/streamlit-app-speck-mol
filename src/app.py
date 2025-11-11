import streamlit as st
import glob
from st_speckmol import speck_plot

# Example files path
ex_files = glob.glob("examples/*.xyz")
with st.sidebar:
    example_xyz = st.selectbox("Select a molecule",ex_files)
    f = open(example_xyz,"r")
    example_xyz = f.read()

res = speck_plot(example_xyz)
