# main.py
import streamlit as st  # Dùng để chạy ứng dụng
from view.css import load_custom_css  # Tải CSS
from view.interface import setup_page, setup_sidebar, setup_chat_interface, setup_dialog  # Thiết lập giao diện
from model.database import initialize_firebase  # Khởi tạo Firebase
from model.tools import get_llm_and_agent  # Khởi tạo agent
from controller.chat_controller import handle_user_input  # Xử lý input
import uuid  # Tạo ID ngẫu nhiên
import json
from streamlit_js_eval import set_cookie
from controller.cookie import get_cookie_data
import time
<<<<<<< HEAD

COLLECTION_NAME = 'documents'
=======
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf

def main():
    """
    Hàm chính để chạy ứng dụng.
    """      
    setup_page()  # Cấu hình trang
    load_custom_css()  # Tải CSS
    setup_sidebar()  # Thiết lập sidebar
    
    if 'user_info' not in st.session_state:
        get_cookie_data()
    
    if 'dialog_display' not in st.session_state:
        st.session_state.dialog_display = True
    # Hiển thị dialog nếu chưa có
    if st.session_state.get('dialog_display', True):
<<<<<<< HEAD
        setup_dialog()
=======
   
            setup_dialog()
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
    
    # Khởi tạo Firebase nếu chưa có
    if "firebase_db" not in st.session_state:
        st.session_state.firebase_db = initialize_firebase()

    # Khởi tạo agent nếu chưa có
    if "agent_executor" not in st.session_state:
<<<<<<< HEAD
        st.session_state.agent_executor = get_llm_and_agent(collection_name=COLLECTION_NAME)
=======
        st.session_state.agent_executor = get_llm_and_agent(collection_name='test_title')
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
    
    if 'id_session_dict' not in st.session_state:
        st.session_state.id_session_dict = {}    

<<<<<<< HEAD
    # Khởi tạo botID nếu chưa có
    if 'botID' not in st.session_state:
        st.session_state.id_session_dict['botID'] = st.session_state.botID = "chatbotRAG_v1.0.0"
        
    # Khởi tạo userID nếu chưa có
    if 'userID' not in st.session_state:
        st.session_state.id_session_dict['userID'] = st.session_state.userID = f"RAG{uuid.uuid4().hex[:16]}"
        
    # Khởi tạo conversationID nếu chưa có
    if 'conversationID' not in st.session_state:
        st.session_state.id_session_dict['conversationID'] = st.session_state.conversationID = f"RAG{uuid.uuid4().hex[:16]}"
=======
    # Khởi tạo bot_id nếu chưa có
    if 'bot_id' not in st.session_state:
        st.session_state.id_session_dict['bot_id'] = st.session_state.bot_id = "PrLkP6OJKdZ0tbIBChwbENTu4pB3"
    # Khởi tạo user_id nếu chưa có
    if 'user_id' not in st.session_state:
        st.session_state.id_session_dict['user_id'] = st.session_state.user_id = f"RAG_{uuid.uuid4().hex[:16]}"
    # Khởi tạo chat_id nếu chưa có
    if 'chat_id' not in st.session_state:
        st.session_state.id_session_dict['chat_id'] = st.session_state.chat_id = f"RAG_chat_id_{uuid.uuid4().hex[:16]}"
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf

    # Khởi tạo dialog_display nếu chưa có 
    if not st.session_state.get('dialog_display', True):
        set_cookie(
            name = "id_session",
            value = json.dumps(st.session_state.id_session_dict),
            duration_days = 1/24,
        )
    
    st.session_state.agent_history = setup_chat_interface()  # Thiết lập giao diện chat

    # # Giới hạn lịch sử chat
    # if len(st.session_state.agent_history) > 20:
    #     st.session_state.agent_history = st.session_state.agent_history[-10:]


    # Xử lý input người dùng
    handle_user_input(
        st.session_state.agent_history,
        st.session_state.agent_executor,
<<<<<<< HEAD
        st.session_state.userID,
        st.session_state.botID,
        st.session_state.conversationID,
=======
        st.session_state.user_id,
        st.session_state.bot_id,
        st.session_state.chat_id,
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
        st.session_state.firebase_db
    )
    


if __name__ == "__main__":
    main()  # Chạy ứng dụng