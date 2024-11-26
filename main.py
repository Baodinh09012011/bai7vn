import streamlit as s

name = "Chua chon ban"
tuoi = "Chua chon ban"
sothich = "Chua chon ban"
s.title("thong tin ban")
col1,col2,col3 = s.columns(3)
with col1:
  a1 = s.button("Ban A")
with col2:
  a2 = s.button("Ban B")
with col3:
  a3 = s.button("Ban C")
if a1:
  name = "Nguyen Van A"
  tuoi = 12
  sothich = "choi game"
if a2:
  name = "Nguyen Van B"
  tuoi = 14
  sothich = "danh cau long"
if a3:
  name = "Nguyen Van C"
  tuoi = 17
  sothich = "da bong"
with s.expander("Thong tin ban"):
  s.write(f"Ten : {name}")
  s.write(f"Tuoi : {tuoi}")
  s.write(f"so thich : {sothich}")

  