# view/interface.py
import streamlit as st  # Dùng để tạo giao diện
from langchain_core.messages import AIMessage  # Định dạng tin nhắn
import json
from streamlit_js_eval import set_cookie
<<<<<<< HEAD
import re
=======
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf

def setup_page():
    """
    Cấu hình trang web cơ bản:
    - Đặt tiêu đề trang, icon và layout (wide).
    """
    st.set_page_config(
        page_title="FLIC Chatbot",   # Tiêu đề hiển thị trên tab trình duyệt
        page_icon="https://res.cloudinary.com/day4wv1aw/image/upload/v1741313942/flic_chatbot/OIP-removebg-preview_vrvzha.png",              # Icon trên tab
        layout="centered", # Giao diện rộng
        initial_sidebar_state="auto" # ("auto", "expanded", or "collapsed")
    )

def setup_sidebar():
    st.sidebar.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741313942/flic_chatbot/OIP-removebg-preview_vrvzha.png" 
            width="150">
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Thêm CSS tùy chỉnh để căn giữa tiêu đề trong sidebar
    st.markdown(
        """
        <style>
            /* Căn giữa tiêu đề trong sidebar */
            [data-testid="stHeading"] {
                text-align: center;
            }
            
            /* Xóa khoảng trống trên cùng cho sidebar */
            [data-testid="stSidebarHeader"] {
                height: 50px;  /* Giảm chiều cao */
                padding: 20px;  /* Xóa padding để thu gọn hơn */
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.subheader("")
    # Tạo tiêu đề trong sidebar
    st.sidebar.header("GIỚI THIỆU")
    
    st.sidebar.markdown(
        'FLIC (Trung tâm Ngoại ngữ - Tin học), trực thuộc Trường Đại học Kinh tế Đà Nẵng, '
        'có nhiệm vụ cung cấp dịch vụ đào tạo và đánh giá năng lực ngoại ngữ, công nghệ thông tin cho sinh viên.'
    )
    st.sidebar.subheader("")
    st.sidebar.subheader("")
    st.sidebar.header("THÔNG TIN LIÊN HỆ")

    # HTML và CSS để hiển thị icon trên một hàng
    st.sidebar.markdown("""
        <style>
            .icon-container {
                display: flex;
                justify-content: center;
                gap: 20px;
            }
            .icon-container a img {
                width: 40px;
                height: 40px;
            }
        </style>
        <div class="icon-container">
            <a href="https://maps.app.goo.gl/SNVJgcejAN1hF2p68" target="_blank">
                <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741413156/flic_chatbot/Marker_w6ugns.png">
            </a>
            <a href="https://zalo.me/84901951616" target="_blank">
                <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741535249/flic_chatbot/Zalo_jjbd9c.png">
            </a>
            <a href="https://flic.due.udn.vn/" target="_blank">
                <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741413155/flic_chatbot/Globe_czih80.png">
            </a>
            <a href="https://www.facebook.com/FLIC.DUE.UDN.VN" target="_blank">
                <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741412988/flic_chatbot/Facebook_owyz2s.png">
            </a>
        </div>
    """, unsafe_allow_html=True)

def setup_chat_interface():
    """
    Thiết lập giao diện chat chính:
    - Hiển thị tiêu đề, caption và lịch sử chat.
    - Nếu chưa có lịch sử, khởi tạo với lời chào mặc định.
    - Hiển thị tin nhắn của bot và người dùng theo định dạng thích hợp.
    """
    st.markdown(
        """
        <style>
            .centered {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
        </style>
        <div class="centered">
            <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741313942/flic_chatbot/OIP-removebg-preview_vrvzha.png" width="200">
            <h1>FLIC Chatbot</h1>
            <p style="font-size: 16px; color: gray; max-width: 450px;">
                Giúp bạn giải đáp mọi thắc mắc về khóa học, lịch học, học phí và nhiều thông tin khác một cách nhanh chóng, chính xác
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Nếu chưa có lịch sử chat cho agent, khởi tạo với lời chào mặc định của bot
    if "agent_history" not in st.session_state:
        st.session_state.agent_history = [
            AIMessage(content="Tôi có thể giúp gì cho bạn?")
        ]
    
    if "display_history" not in st.session_state:
        st.session_state.display_history = False
    
    # Giả sử num_messages_display được định nghĩa trước đó
    num_messages_display = 10

    # Nếu lịch sử nhiều hơn num_messages_display tin và chưa bật chế độ hiển thị đầy đủ,
    # ban đầu chỉ hiển thị num_messages_display tin nhắn cuối.
    if len(st.session_state.agent_history) > num_messages_display and not st.session_state.display_history:
        display_history_data = st.session_state.agent_history[-num_messages_display:]
        
        # Hiển thị nút "Xem thêm lịch sử" nếu chưa hiển thị toàn bộ lịch sử
        if st.button("Xem thêm lịch sử"):
            st.session_state.display_history = True
    else:
        display_history_data = st.session_state.agent_history
        
    # Hiển thị lịch sử chat theo định dạng của streamlit chat message
    for msg in display_history_data:
        if isinstance(msg, AIMessage):
            st.chat_message("assistant").write(msg.content)
        else:
            # Chuyển đổi các dòng mới cho phù hợp với định dạng markdown
            message_xuong_dong = msg.content.replace("\n", "  \n")
            st.chat_message("human").markdown(message_xuong_dong)
            
    return st.session_state.agent_history

@st.fragment
@st.dialog(" ", width="small")
def setup_dialog():
    st.markdown(
        """
        <style>
            /* Lớp overlay che phủ toàn bộ trang */
            [data-baseweb="modal"] {
            background: transparent; /* Nền mờ */
            }
            /* Lớp overlay che phủ toàn bộ trang */
            [data-baseweb="modal"] > div {
            background: transparent; /* Nền mờ */
            backdrop-filter: blur(5px); /* Làm mờ nền */
            }

            /* Nền của dialog */
            [aria-label="dialog"] {
                background: linear-gradient(to top, #E1F5FE, #FFFFFF);
            }

            /* Nút đóng dialog */
            [aria-label="Close"] {
            display: none;
            }
            [aria-label="dialog"] > div:first-child {
                display: none !important;
            }

            /* Xóa khung của Form */
            [data-testid="stForm"] {
                border: none;
            }

            /* Ô nhập Text_input */
            [data-baseweb="input"],
            [data-baseweb="input"] * {
                background-color: #FFFFFF; /* Màu nền */
                color: #333; /* Màu chữ xám đậm */
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Thêm hiệu ứng bóng đổ */
            }
            /* Khi nhấn vào hộp nhập liệu, đổi viền ngoài thành đen */
            [data-baseweb="input"]:focus-within,
            [data-baseweb="input"] *:focus-within{
                border-color: #999999 !important;
                background-color: #FBF8FB; /* Màu nền */
                color: #333; /* Màu chữ xám đậm */
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Thêm hiệu ứng bóng đổ */
            }     
            
            [role="radiogroup"] {
                display: flex;
                justify-content: center;
                gap: 50px;
            }

            /* Cảnh báo */
            [aria-label="dialog"][data-baseweb="notification"]{
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Thêm hiệu ứng bóng đổ */
                background-color: rgb(249 240 172); /* Màu nền */
            }
                
            /* Nút gửi */
            [data-testid="stFormSubmitButton"]{
                display: flex;
                justify-content: center;
            }
            [data-testid="stBaseButton-secondaryFormSubmit"]{
                padding: 0.4em 1em;
            }   
<<<<<<< HEAD
            
            [data-testid="stDialog"] > div {
                padding: 0 !important;
            }
=======
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
        </style>    
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
            .centered {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
        </style>
        <div class="centered">
            <img src="https://res.cloudinary.com/day4wv1aw/image/upload/v1741313942/flic_chatbot/OIP-removebg-preview_vrvzha.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )
<<<<<<< HEAD
    
    def is_valid_phone(phone):
        return re.fullmatch(r"\d{10,11}", phone) is not None  # SĐT phải có 10-11 chữ số

    def is_valid_email(email):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None  # Định dạng email cơ bản

=======
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
    with st.form(key='user_info_form'):
        # Nhập tên (bắt buộc)
        name = st.text_input("Tên của bạn (bắt buộc):", value="", placeholder="Nhập tên của bạn")
        name_warning = st.empty()
        # Nhập số điện thoại
        phone = st.text_input("Số điện thoại:", value="", placeholder="Nhập số điện thoại của bạn")
<<<<<<< HEAD
        phone_warning = st.empty()
        
        # Nhập email
        email = st.text_input("Email:", value="", placeholder="Nhập email của bạn")
        email_warning = st.empty()
        
=======
        
        # Nhập email
        email = st.text_input("Email:", value="", placeholder="Nhập email của bạn")

>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
        # Chọn nghề nghiệp
        job = st.radio("Nghề nghiệp (bắc buộc):", options=["Sinh viên", "Khác"], index=None, horizontal = True)
        job_warning = st.empty()
        # Nút gửi
        submit_button = st.form_submit_button(label='Gửi')
        
        if submit_button:
<<<<<<< HEAD
            has_error = False
        
            if not name:
                name_warning.warning("Vui lòng nhập tên của bạn.")
                has_error = True
            
            if not job:
                job_warning.warning("Vui lòng chọn nghề nghiệp.")
                has_error = True

            if phone and not is_valid_phone(phone):
                if "prev_phone" not in st.session_state:
                    phone_warning.warning("Số điện thoại không hợp lệ. Vui lòng nhập lại đúng định dạng hoặc nhấn Gửi để bỏ qua")
                    st.session_state.prev_phone = phone  
                    has_error = True
                else:
                    if st.session_state.prev_phone != phone:
                        phone_warning.warning("Số điện thoại không hợp lệ. Vui lòng nhập lại đúng định dạng hoặc nhấn Gửi để bỏ qua")
                        st.session_state.prev_phone = phone  
                        has_error = True
                    else:
                        phone = None

            if email and not is_valid_email(email):
                if "prev_email" not in st.session_state:
                    email_warning.warning("Email không hợp lệ. Vui lòng nhập lại đúng định dạng hoặc nhấn Gửi để bỏ qua")
                    st.session_state.prev_email = email  
                    has_error = True
                else:
                    if st.session_state.prev_email != email:
                        email_warning.warning("Email không hợp lệ. Vui lòng nhập lại đúng định dạng hoặc nhấn Gửi để bỏ qua")
                        st.session_state.prev_email = email
                        has_error = True
                    else:
                        email = None
            
            if not has_error:
=======
            if not name:
                name_warning.warning("Vui lòng nhập tên của bạn.")
            elif not job:
                job_warning.warning("Vui lòng chọn nghề nghiệp.")
            else:
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
                # Để có thể gửi tin nhắn và thoát khỏi vòng lặp Login
                st.session_state.name = name
                
                # Lưu thông tin vào session_state
                st.session_state.user_info = {
                    'name': name,
                    'phone': "" if phone == None else phone,
                    'email': "" if email == None else email,
                    'job': "" if job == None else job
                }
                
                set_cookie(
                    name = "user_info",
                    value = json.dumps(st.session_state.user_info),
                    duration_days = 1/24,
                )
                # Đặt dialog_display thành False để ngăn dialog hiển thị lại
                st.session_state.dialog_display = False
                st.rerun() 