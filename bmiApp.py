import streamlit as st

st.markdown("# :green[แอปพลิเคชันคำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักปละส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

if st.button("คำนวณค่า BMI"):
  height_m = hight_cm / 100
  bim = weight / (height_m **2)

 st.write("---")
 st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
if bmi < 18.5:
  st.writing("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (แห้ง)")
elif 18.5 <= bmi < 23.0:
  st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
  st.info("คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
  st.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องงูจงอางระหว่างกินข้าว🐍❗❗")

st.divider()
st.write("นายนนทพัทธ์ สุยะเพี้ยง เลขที่41 ม.4/6")
