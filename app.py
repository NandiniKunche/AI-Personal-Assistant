import streamlit as st
from chatbot.llm import get_ai_response
from chatbot.speech import listen

st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Personal Assistant")

st.markdown("""
<style>

.chat-container{
    max-width:900px;
    margin:auto;
}

.user-msg{
    display:flex;
    justify-content:flex-end;
    margin:12px 0;
}

.user-bubble{
    background:#2b7cff;
    color:white;
    padding:12px 18px;
    border-radius:18px;
    max-width:75%;
    font-size:16px;
}

.ai-msg{
    display:flex;
    justify-content:flex-start;
    margin:12px 0;
}

.ai-bubble{
    background:#f1f3f5;
    color:black;
    padding:12px 18px;
    border-radius:18px;
    max-width:75%;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "waiting_for_response" not in st.session_state:
    st.session_state.waiting_for_response = False

# -------------------------
# Display Chat
# -------------------------

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-msg">
                <div class="user-bubble">
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="ai-msg">
                <div class="ai-bubble">
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Voice Button
# -------------------------

voice_prompt = None

if st.button("🎤"):

    with st.spinner("Listening..."):

        voice = listen()

    if voice:
        voice_prompt = voice
    else:
        st.error("Couldn't understand. Please try again.")

# -------------------------
# Text Input
# -------------------------

text_prompt = st.chat_input("Ask me anything...")

# Decide which prompt to use
prompt = voice_prompt if voice_prompt else text_prompt

# -------------------------
# Add User Message
# -------------------------

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    st.session_state.waiting_for_response = True

    st.rerun()

# -------------------------
# Generate AI Response
# -------------------------

if (
    st.session_state.waiting_for_response
    and len(st.session_state.messages) > 0
    and st.session_state.messages[-1]["role"] == "user"
):

    with st.spinner("Thinking..."):

        response = get_ai_response(
            st.session_state.messages
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.session_state.waiting_for_response = False

    st.rerun()