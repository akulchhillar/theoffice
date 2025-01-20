import streamlit as st
from phi.agent import Agent
from phi.tools.newspaper_tools import NewspaperTools
from phi.model.groq import Groq


characters = {"Michael_Scott":["Scrape the url https://theoffice.fandom.com/wiki/Michael_Scott and https://en.wikipedia.org/wiki/Michael_Scott_(The_Office)",
"MS.jpg"],
"Jim Halpert":["Scrape the url https://theoffice.fandom.com/wiki/Jim_Halpert and https://en.wikipedia.org/wiki/Jim_Halpert","JH.jpg"],
"Pam Beesly":["Scrape the url https://theoffice.fandom.com/wiki/Pam_Beesly and https://en.wikipedia.org/wiki/Pam_Beesly","PB.jpg"],
"Dwight Schrute":["Scrape the url https://theoffice.fandom.com/wiki/Dwight_Schrute and https://en.wikipedia.org/wiki/Dwight_Schrute","DS.jpg"],
"Toby Flenderson":["Scrape the url https://theoffice.fandom.com/wiki/Toby_Flenderson","TF.jpg"],
"Angela Martin":["Scrape the url https://theoffice.fandom.com/wiki/Angela_Martin and https://en.wikipedia.org/wiki/Angela_Martin","AM.jpg"],
"Andy Bernard":["Scrape the url https://theoffice.fandom.com/wiki/Andy_Bernard and https://en.wikipedia.org/wiki/Andy_Bernard","AB.jpg"],
"Kevin Malone":["Scrape the url https://theoffice.fandom.com/wiki/Kevin_Malone and https://en.wikipedia.org/wiki/Kevin_Malone","KM.jpg"]}


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
    description=f"You are going to act as '{option}' from the series 'The Office' and you are going to answer all the questions asked by the user. You will answer as if you are him.",
    instructions=[f"{characters[option][0]} using 'NewspaperTools' from the tool kit and use the content to understand and think like '{option}'.",
    "Answer the user's questions using the content from the urls."])
    response = agent.run(query)

    return response.content


def append_data():
   
    prompt_value = st.session_state.prompt_value
    
    st.session_state['user_messages'].append(prompt_value)
    st.session_state['bot_messages'].append(get_response(prompt_value))
    st.session_state['count_messages'] = st.session_state['count_messages'] + 1

    for msg in range(0,st.session_state['count_messages']):
        messages.chat_message("user",avatar="user.png").write(st.session_state['user_messages'][msg])
        messages.chat_message("assistant",avatar=characters[option][1]).write(st.session_state['bot_messages'][msg])
   

st.title("That's What She Said: :blue[The Office] AI Chatbot. :sunglasses:")

with st.expander("See explanation"):
    st.markdown('''
        This Streamlit app allows you to chat with an AI agent that channels the unique voices and comedic stylings of your favorite Office characters. \n
        Ask questions, share anecdotes, and witness the hilarious, cringeworthy, and sometimes heartwarming responses as the AI agent delivers lines in true Office fashion.
    ''')

option = st.selectbox(
    label="Select a character to begin.",
    options=list(characters.keys()),
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
