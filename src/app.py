import re
import sys
import warnings
import streamlit as st
from crew import CompetitorAnalyst

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

st.set_page_config(page_title="Multi-Agent CA", layout="centered")

# Used to stream sys output on the streamlit frontend
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'red', 'blue', 'green', 'orange']  
        self.color_index = 0  
    
    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        # Check if the text contains the specified phrase and apply color
        if "Input Identification and Metadata Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("Input Classification and Information Gathering Specialist", f":{self.colors[0]}[Input Classification and Information Gathering Specialistt]")
        if "Competitor Data Aggregation Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("Competitor Data Aggregation Specialist", f":{self.colors[0]}[Competitor Data Aggregation Specialist]")
        if "NLP Insights and Data Transformation Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("NLP Insights and Data Transformation Specialist", f":{self.colors[1]}[NLP Insights and Data Transformation Specialist]")
        if "Competitive Feature Analysis Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("Competitive Feature Analysis Specialist", f":{self.colors[2]}[Competitive Feature Analysis Specialist]")
        if "Competitor SWOT Framework Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("Competitor SWOT Framework Specialist", f":{self.colors[3]}[Competitor SWOT Framework Specialist]")
        if "Competitor Analysis Report Specialist" in cleaned_data:
            cleaned_data = cleaned_data.replace("Competitor Analysis Report Specialist", f":{self.colors[4]}[Competitor Analysis Report Specialist]")
        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer) , unsafe_allow_html=True)
            self.buffer = []


st.header("Competitor Analysis Multi-Agent")
st.subheader("Generate A Competitor Analysis Report!",divider="rainbow",anchor=False)


with st.form("form"):
    search_query=st.text_input("Enter the name/website of the product/startup", key="search_query")
    submitted=st.form_submit_button("Submit")

if submitted:
    with st.status("🤖 **Agents at work...**",expanded=True,state="running") as status:
        with st.container(height=600):
            sys.stdout = StreamToContainer(st)
            #Defining the crew comprising of different agents
            result = CompetitorAnalyst().crew().kickoff(inputs={"topic":search_query})
        status.update(label="✅ Your Report is ready",state="complete", expanded=False) 
    st.subheader("Competitor Analysis Report is ready!", anchor=False, divider="rainbow")
    st.markdown(result)