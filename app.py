import streamlit as st
from phi.agent import Agent
from phi.tools.newspaper_tools import NewspaperTools
from phi.model.groq import Groq




if "user_messages" not in st.session_state:
    st.session_state['user_messages'] = []

if "bot_messages" not in st.session_state:
    st.session_state['bot_messages'] = []

if "count_messages" not in st.session_state:
    st.session_state['count_messages'] = 0

if "selected_char" not in st.session_state:
    st.session_state['selected_char'] = None





def get_response(query):
    agent = Agent(model=Groq(id="llama-3.3-70b-versatile"),tools=[NewspaperTools()], show_tool_calls=True,
    description="You are going to act as 'Michael_Scott' from the series 'The Office' and you are going to answer all the questions asked by the user. You will answer as if you are him.",
    instructions=["Scrape the url https://theoffice.fandom.com/wiki/Michael_Scott and https://en.wikipedia.org/wiki/Michael_Scott_(The_Office)#Character_details,_arc,_backstory using 'NewspaperTools' from the tool kit and use the content to understand and think like 'Michael Scott'.",
    "Answer the user's questions using the content from the url."])
    response = agent.run(query)

    return response.content


def append_data():
   
    prompt_value = st.session_state.prompt_value
    
    st.session_state['user_messages'].append(prompt_value)
    st.session_state['bot_messages'].append(get_response(prompt_value))
    st.session_state['count_messages'] = st.session_state['count_messages'] + 1

    for msg in range(0,st.session_state['count_messages']):
        messages.chat_message("user",avatar=f"https://api.dicebear.com/9.x/thumbs/svg?seed={option}&backgroundColor=0a5b83,1c799f,69d2e7,f1f4dc,f88c49,b6e3f4,c0aede,d1d4f9,ffd5dc,ffdfbf,transparent&backgroundType=gradientLinear").write(st.session_state['user_messages'][msg])
        messages.chat_message("assistant",avatar="MS.jpg").write(st.session_state['bot_messages'][msg])
   

st.title("That's What She Said: :blue[The Office] AI Chatbot. :sunglasses:")

with st.expander("See explanation"):
    st.markdown('''
        This Streamlit app allows you to chat with an AI agent that channels the unique voices and comedic stylings of your favorite Office characters. \n
        Ask questions, share anecdotes, and witness the hilarious, cringeworthy, and sometimes heartwarming responses as the AI agent delivers lines in true Office fashion.
    ''')

option = st.selectbox(
    label="Select a character to begin.",
    options=("Michael Scott", "Jim Halpert", "Pam Beesly","Angela Martin",
             "Kevin Malone","Phyllis Lapin","Darryl Philbin","Andy Bernard"),
    index=None,
    placeholder="Select a character to begin.",
    label_visibility="hidden"
)




if option:

    if st.session_state['selected_char'] != option:
        st.session_state['user_messages'] = []
        st.session_state['bot_messages'] = []
        st.session_state['count_messages'] = 0
        st.session_state['selected_char'] = option

    
    

    prompt = st.chat_input("Say something",on_submit=append_data,key="prompt_value")
    
    messages = st.container(border=True,height=300)







        # messages.chat_message("user").write(prompt)
        # messages.chat_message("assistant").write(f"Echo: {prompt}")
