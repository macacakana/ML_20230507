import pandas as pd
import numpy as np
import streamlit as st

st.title("測試頁面")
st.write("AAAA")

a = 100
st.write(a)
st.write("-----------------\n")
st.write("表格")
df = pd.DataFrame({"F1":[1,2,3,4],"F2":[11,22,33,44]})
st.write(df)

st.write("-----------------\n")
st.write("核取方塊")
cb = st.checkbox("是否外送?")
if cb:
  st.info("外送")

st.write("-----------------\n")
st.write("選項按鈕")
gender = st.radio("性別:",('男生','女生','無'))
st.write(gender)
st.success(gender)

st.write("-----------------\n")
st.write("下拉選單")
option = st.selectbox("最喜歡的水果?",('蘋果','香蕉','鳳梨','荔枝'))
st.write(option)
st.success(option)

st.write("-----------------\n")
st.write("進度條")
import time
'''
aa = st.empty
bar = st.progress(0)
for i in range(100):
  aa.text(f"目前進度:{i+1}%")
  bar.progress(i+1)
  time.sleep(0.1)
'''

st.write("-----------------\n")
st.write("按鈕")
def AA():
  st.text("fuction")
btn = st.button("確定")
if btn:
  st.info("已確認")
  AA()

st.write("-----------------\n")
st.write("滑桿")
num = st.slider("請選擇數量:",1,20)
"num=",num

st.write("-----------------\n")
st.write("檔案上傳")
loader = st.file_uploader("請選擇CSV檔:")

if loader is not None:
  df2 = pd.read_csv(loader, header=None)
  st.dataframe(df2)
  st.table(df2.iloc[:2])

st.write("-----------------\n")
st.write("隱藏欄位(文字)")
hidden = st.expander("按下後展開")
hidden.write("hi hi hi")

st.write("-----------------\n")
st.write("圖片上傳+圖片展示")
img = st.file_uploader("請選擇圖檔:",type=['png','jpg','jpeg'])
if img is not None:
  st.image(img)

st.write("-----------------\n")
st.write("側邊攔")
side01 = st.sidebar.button("Click me")
side02 = st.sidebar.checkbox("OK?")

st.write("-----------------\n")
st.write("分欄")
lafe , right = st.columns(2)
lafe.write("btn3")
right.write("BBBBB")