# 🤖 Chatbot Soạn Giáo Án – CTGDPT 2018

Dự án cung cấp chatbot hỗ trợ giáo viên:
- Soạn giáo án đúng cấu trúc CTGDPT 2018
- Sinh yêu cầu cần đạt (3 mức)
- Tự sinh năng lực chung + năng lực đặc thù mỗi môn
- Xuất nội dung rõ ràng, dễ sử dụng

## Cách chạy trên Streamlit Cloud
1. Tải 3 tệp: app.py, requirements.txt, README.md
2. Tạo repo GitHub mới và tải 3 tệp lên
3. Vào https://streamlit.io/cloud → Deploy app → Chọn repo
4. Thêm API Key vào *Secrets*:
```
OPENAI_API_KEY = "your_key_here"
```

App sẽ hoạt động tự động trên liên kết dạng:
```
https://your-app-name.streamlit.app
```
