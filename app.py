#%% packages
from table_rag import rag, sql_table_info
import streamlit as st
#%%
st.title("Kaffee-Verkauf Chatbot")

# Initialize chat history in session state if not present
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display all previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(name=msg["role"]):
        st.write(msg["content"])

# Chat input
user_query = st.chat_input(placeholder="Was willst du wissen?")
if user_query is not None:
    # Add user message to history
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.chat_message(name="user"):
        st.write(user_query)
    # Get assistant response
    bot_answer = rag(user_query=user_query, sql_table_info=sql_table_info)
    # Add assistant message to history
    st.session_state["messages"].append({"role": "assistant", "content": bot_answer})
    with st.chat_message(name="assistant"):
        st.write(bot_answer)
