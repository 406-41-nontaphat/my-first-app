import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:
    st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
    st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:
    st.session_state.ans10_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans7_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.ans8_val = ""  # เคลียร์ค่าช่องข้อ 8
    st.session_state.ans9_val = ""  # เคลียร์ค่าช่องข้อ 9
    st.session_state.ans10_val = ""  # เคลียร์ค่าช่องข้อ 10
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()
    u_ans8 = ans8.strip().lower()
    u_ans9 = ans9.strip().lower()
    u_ans10 = ans10.strip().lower()


    if u_ans1 == "สเตียรอยด์":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    if u_ans2 == "เป็นแหล่งสร้างพลังงานให้เซลล์ โดยเปลี่ยนพลังงานจากสารอาหารเป็น ATP ผ่านกระบวนการหายใจระดับเซลล์":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
 
    if u_ans3 == "มีโครงสร้างหลักเป็นฟอสโฟลิพิดสองชั้นและโปรตีน ทำหน้าที่ห่อหุ้มเซลล์ ควบคุมการผ่านเข้า–ออกของสาร และรับส่งสัญญาณระหว่างเซลล์":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "DNA มีน้ำตาลดีออกซีไรโบส (deoxyribose) ส่วน RNA มีน้ำตาลไรโบส (ribose)":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
  
    if u_ans5 == "อะดีนีน (A), ไทมีน (T), ไซโทซีน (C) และกวานีน (G)":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")


    if u_ans6 == "อะดีนีนจับคู่กับไทมีน (A–T) ด้วยพันธะไฮโดรเจน 2 พันธะ และไซโทซีนจับคู่กับกวานีน (C–G) ด้วยพันธะไฮโดรเจน 3 พันธะ":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

    if u_ans7 == "ประกอบด้วยน้ำตาลเพนโทส 1 โมเลกุล หมู่ฟอสเฟต 1 หมู่ และเบสไนโตรเจน 1 ชนิด":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")


    if u_ans8 == "ยูราซิล (Uracil; U) โดยใน RNA ยูราซิลจะจับคู่กับอะดีนีน (A) แทนไทมีน":
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")
  
    if u_ans9 == "เป็นองค์ประกอบหลักของเยื่อหุ้มเซลล์ โดยเรียงตัวเป็นชั้นคู่ หัวที่ชอบน้ำหันออกสู่ของเหลวทั้งภายในและภายนอกเซลล์ ส่วนหางที่ไม่ชอบน้ำหันเข้าหากัน จึงช่วยเป็นกำแพงเลือกผ่านและควบคุมการเคลื่อนที่ของสาร":
        st.success("✅ ข้อ 9: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")

    if u_ans10 == "พันธะฟอสโฟไดเอสเทอร์ (phosphodiester bond)":
        st.success("✅ ข้อ10: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")


    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 10:
        st.success("🎉 You win!")
    elif score >= 7:
        st.info("✨nice!")
    elif score >= 5:
        st.warning("⚠close")
    elif score >= 3:
        st.error("failed,do better")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(180 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: คอเลสเตอรอลจัดเป็นลิพิดชนิดใด",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: เพราะเหตุใดไมโทคอนเดรียจึงถูกเรียกว่าเป็นแหล่งสร้างพลังงานของเซลล์",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: เยื่อหุ้มเซลล์มีโครงสร้างและหน้าที่สำคัญอะไรบ้าง",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: DNA และ RNA มีความแตกต่างกันในเรื่องชนิดของน้ำตาลอย่างไร",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: เบสไนโตรเจนที่พบใน DNA มีอะไรบ้าง",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6: การจับคู่ของเบสในโมเลกุล DNA เป็นอย่างไร",
    value=st.session_state.ans6_val,
)
ans7 = st.text_input(
    "ข้อ 7: นิวคลีโอไทด์ประกอบด้วยองค์ประกอบใดบ้าง",
    value=st.session_state.ans7_val,
)
ans8 = st.text_input(
    "ข้อ 8: เบสไนโตรเจนชนิดใดพบใน RNA แต่ไม่พบใน DNA",
    value=st.session_state.ans8_val,
)
ans9 = st.text_input(
    "ข้อ 9: ฟอสโฟลิพิดมีบทบาทสำคัญอย่างไรต่อโครงสร้างของเยื่อหุ้มเซลล์",
    value=st.session_state.ans9_val,
)
ans10 = st.text_input(
    "ข้อ 10: พันธะที่เชื่อมระหว่างนิวคลีโอไทด์ในสาย DNA หรือ RNA เรียกว่าอะไร",
    value=st.session_state.ans10_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans1_val = ans3
st.session_state.ans2_val = ans4
st.session_state.ans1_val = ans5
st.session_state.ans2_val = ans6
st.session_state.ans1_val = ans7
st.session_state.ans2_val = ans8
st.session_state.ans1_val = ans9
st.session_state.ans2_val = ans10


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)

st.divider()
st.write("กลุ่มที่8 ห้อง4/6")


