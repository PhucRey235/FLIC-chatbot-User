# controller/chat_controller.py
import streamlit as st  # Dùng để hiển thị giao diện và xử lý input
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage  # Định dạng tin nhắn
import time  # Tạo hiệu ứng gõ chữ
from model.database import save_message_to_firebase  # Import hàm lưu tin nhắn
from streamlit_js_eval import set_cookie
from controller.cookie import serialize_history

# Hệ thống prompt hướng dẫn chatbot
instruction_prompt = (
    "Bạn là trợ lý ảo của Trung tâm Tiếng Anh FLIC. "
    "Nhiệm vụ của bạn là cung cấp thông tin chính xác và hữu ích về trung tâm, bao gồm các khóa học, kỳ thi CNTT và TOEIC, "
    "lịch thi, lệ phí, thủ tục đăng ký, nội dung đào tạo, ưu đãi và các dịch vụ khác. "
    "Nếu người dùng hỏi về thông tin về bài thi A1, A2, B1, B2, C1, C2 thì hãy trả lời rằng: "
    "Hiện tại, trung tâm chỉ cung cấp khóa học và tổ chức kỳ thi TOEIC phối hợp với IIG Việt Nam, chưa có chương trình dành cho kỳ thi 'mà người dùng hỏi'. "
    "Nếu bạn quan tâm đến luyện thi TOEIC, chúng tôi có các khóa học phù hợp và hỗ trợ đăng ký thi chính thức."
    "Chứng chỉ CNTT, Công nghệ Thông tin, Tin học đều là 1. "
    "Khuyến khích người dùng khi đăng ký các khóa học sẽ đăng ký theo nhóm bạn thay vì đăng ký cá nhân"
    "Nếu không có thông tin cụ thể, hãy hướng dẫn người dùng cách liên hệ với FLIC để được hỗ trợ thêm."
)

<<<<<<< HEAD
def handle_user_input(agent_history, agent_executor, userID, botID, conversationID, db):
=======
def handle_user_input(agent_history, agent_executor, user_id, bot_id, chat_id, db):
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
    """
    Xử lý input từ người dùng và điều phối giữa Model và View.
    - agent_history: Lịch sử chat.
    - agent_executor: Agent xử lý câu hỏi.
<<<<<<< HEAD
    - userID: ID người dùng.
    - botID: ID chatbot.
    - conversationID: ID cuộc trò chuyện.
=======
    - user_id: ID người dùng.
    - bot_id: ID chatbot.
    - chat_id: ID cuộc trò chuyện.
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
    - db: Firestore client.
    """    
    # Tạo ô nhập liệu và lấy input từ người dùng
    if user_input := st.chat_input("Hãy hỏi tôi về Trung tâm Tiếng Anh FLIC!"):
        if 'name' not in st.session_state:
            return
<<<<<<< HEAD
        
        # Thêm tin nhắn người dùng vào lịch sử
        agent_history.append(HumanMessage(content=user_input))
        
=======
        # Thêm tin nhắn người dùng vào lịch sử
        agent_history.append(HumanMessage(content=user_input))
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
        # Hiển thị tin nhắn người dùng (xử lý xuống dòng)
        message_xuong_dong = user_input.replace("\n", "  \n")
        st.chat_message("human").markdown(message_xuong_dong)

        with st.spinner("Vui lòng chờ trong giây lát..."):  # Hiển thị spinner khi xử lý
            start_time = time.time()
<<<<<<< HEAD
            
            # Chuẩn bị tin nhắn gửi cho agent
            summarized_message = [SystemMessage(content=instruction_prompt)]
            summarized_message.extend(agent_history)
            
=======
            # Lưu tin nhắn người dùng vào Firebase
            # Chuẩn bị tin nhắn gửi cho agent
            summarized_message = [SystemMessage(content=instruction_prompt)]
            summarized_message.extend(agent_history)
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
            # Gọi agent để lấy phản hồi
            start_time = time.time()
            output = agent_executor.invoke({"messages": summarized_message})
            response = output["messages"][-1].content  # Lấy phản hồi cuối cùng
<<<<<<< HEAD
            

            
            # Lưu tin nhắn bot vào Firebase
            save_message_to_firebase(db, botID, response, userID, user_input, conversationID, agent_history)
            
=======
            # Lưu tin nhắn bot vào Firebase
            save_message_to_firebase(db, bot_id, response, user_id, user_input, chat_id, agent_history)
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
            # Hiển thị phản hồi với hiệu ứng gõ chữ
            response_time = time.time() - start_time
            
            with st.chat_message("assistant"):
                # if response_time < 1:  # Nếu nhanh hơn 2 giây, hiển thị ngay
                #     text_container.markdown(response)
                # else:  # Hiển thị hiệu ứng gõ chữ
<<<<<<< HEAD
                messages_split = response.split(' ')
                full_response = ""
                text_container = st.markdown("")
                
                for word in messages_split:
                    full_response += word + " "
                    text_container.markdown(full_response)
                    time.sleep(0.005)  # Delay 0.02 giây giữa các từ

=======
                    messages_split = response.split(' ')
                    full_response = ""
                    text_container = st.markdown("")
                    for word in messages_split:
                        full_response += word + " "
                        text_container.markdown(full_response)
                        time.sleep(0.005)  # Delay 0.02 giây giữa các từ
>>>>>>> 73b7bcfb1188c72d1622bb91b10209f1618087cf
            # Thêm phản hồi bot vào lịch sử
            agent_history.append(AIMessage(content=response))
            set_cookie(
                name = "agent_history", 
                value = serialize_history(st.session_state.agent_history), 
                duration_days = 1/24, 
            )

