import streamlit as st

# Tiêu đề của ứng dụng
st.title("Ứng dụng với Sidebar và Nút")

# Tạo các button trong sidebar
button_1 = st.sidebar.button("Nút 1")
button_2 = st.sidebar.button("Nút 2")
button_3 = st.sidebar.button("Nút 3")

# Hiển thị nội dung tương ứng với nút được nhấp

def b1() -> None:
    st.write("Nội dung của Nút 1")
if button_1:
    b1()
elif button_2:
    st.write("Nội dung của Nút 2")
elif button_3:
    st.write("Nội dung của Nút 3")
