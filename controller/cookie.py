import streamlit as st
import json
from streamlit_js_eval import get_cookie
from langchain_core.messages import HumanMessage, AIMessage  # Định dạng tin nhắn

# Giả sử bạn đã import hoặc định nghĩa lớp HumanMessage và AIMessage ở đâu đó:
# from your_module import HumanMessage, AIMessage

def serialize_history(history):
    """
    Chuyển list các đối tượng (HumanMessage, AIMessage) thành JSON string.
    """
    serializable_history = []
    for msg in history:
        if hasattr(msg, 'content'):
            # Xác định loại của message để lưu lại
            msg_type = 'HumanMessage' if msg.__class__.__name__ == 'HumanMessage' else 'AIMessage'
            msg_dict = {
                'type': msg_type,
                'content': msg.content,
                'additional_kwargs': msg.additional_kwargs,
                'response_metadata': msg.response_metadata,
                'id': msg.id,
            }
            serializable_history.append(msg_dict)
        else:
            raise ValueError("Đối tượng không hợp lệ trong history")
    return json.dumps(serializable_history)

def deserialize_history(json_str):
    """
    Chuyển chuỗi JSON (đã được lưu trong cookie) trở lại thành list các đối tượng HumanMessage/AIMessage.
    """
    data = json.loads(json_str)
    history = []

    for item in data:
        msg_type = item.get('type')
        if msg_type == 'HumanMessage':
            # Khởi tạo đối tượng HumanMessage
            msg = HumanMessage(
                content=item['content'],
                additional_kwargs=item.get('additional_kwargs', {}),
                response_metadata=item.get('response_metadata', {}),
                id=item.get('id')
            )
        elif msg_type == 'AIMessage':
            # Khởi tạo đối tượng AIMessage
            msg = AIMessage(
                content=item['content'],
                additional_kwargs=item.get('additional_kwargs', {}),
                response_metadata=item.get('response_metadata', {}),
                id=item.get('id')
            )
        else:
            raise ValueError("Loại message không được hỗ trợ")
        history.append(msg)
    return history


def get_cookie_data():
    # Đọc cookie và load vào session_state khi ứng dụng khởi động
    user_info_cookie = get_cookie("user_info")
    agent_history_cookie = get_cookie("agent_history")
    id_session_cookie = get_cookie("id_session")

    if user_info_cookie:
        try:
            st.session_state.user_info = json.loads(user_info_cookie)
        except Exception as e:
            st.error(f'Lỗi khi lấy cookie user_info: {e}')

    if agent_history_cookie:
        try:
            st.session_state.agent_history = deserialize_history(agent_history_cookie)
        except Exception as e:
            st.error(agent_history_cookie)

    
    if id_session_cookie:
        try:
            id_session_dict = json.loads(id_session_cookie)
<<<<<<< HEAD
            st.session_state.botID = id_session_dict['botID']
            st.session_state.userID = id_session_dict['userID']
            st.session_state.conversationID = id_session_dict['conversationID']
=======
            st.session_state.bot_id = id_session_dict['bot_id']
            st.session_state.user_id = id_session_dict['user_id']
            st.session_state.chat_id = id_session_dict['chat_id']
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
            st.session_state.dialog_display = id_session_dict['dialog_display']
        except Exception as e:
            st.error(f'Lỗi khi lấy cookie id_session: {e}')

        