import streamlit as st
import openai
import os

st.set_page_config(page_title="Chatbot Soạn Giáo Án", page_icon="📘")

st.markdown("""
<h1 style='text-align:center; color:#2B5EA4;'>🤖 Chatbot Soạn Giáo Án – CTGDPT 2018</h1>
<p style='text-align:center;'>Hỗ trợ soạn bài, yêu cầu cần đạt, năng lực, phẩm chất và câu hỏi vận dụng.</p>
""", unsafe_allow_html=True)

# Load API key from Streamlit Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

subject = st.text_input("📘 Môn học:")
grade = st.text_input("🎓 Lớp:")
topic = st.text_input("✏️ Chủ đề / Tên bài học:")

btn = st.button("Soạn giáo án")

def generate_lesson(subject, grade, topic):
    prompt = f"""
Bạn là chuyên gia soạn giáo án theo CTGDPT 2018.
Hãy soạn đầy đủ cho bài học sau:

Môn: {subject}
Lớp: {grade}
Bài: {topic}

YÊU CẦU:
1. Viết phần I. YÊU CẦU CẦN ĐẠT theo đúng 3 mức:
- Nhận biết
- Thông hiểu
- Vận dụng (gắn với thực tiễn)

2. Năng lực:
- Gồm năng lực chung
- Năng lực đặc thù môn {subject}

3. Phẩm chất:
- Nhân ái, trách nhiệm, chăm chỉ, trung thực, tự tin

4. Cuối bài:
- Câu hỏi vận dụng gắn với thực tế
"""

    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )

    return response.choices[0].message["content"]

if btn:
    if subject and grade and topic:
        with st.spinner("⏳ Đang soạn bài..."):
            output = generate_lesson(subject, grade, topic)
            st.success("🎉 Hoàn thành!")
            st.write(output)
    else:
        st.error("⚠️ Vui lòng nhập đầy đủ thông tin.")
