import re
import sys
import warnings
import streamlit as st
from crew import CompetitorAnalyst
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

st.set_page_config(page_title="Multi-Agent Competitor Analysis", layout="centered")

# Used to stream sys output on the streamlit frontend
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'blue', 'green', 'orange']  
    
    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        # Check if the text contains the specified phrase and apply color
        for idx, term in enumerate(["Input Metadata Specialist", 
                                     "Competitor Data Aggregation Specialist",
                                     "NLP Insights and Data Transformation Specialist", 
                                     "Risk Assessment Analyst",
                                     "Competitive Feature Analysis Specialist",
                                     "Competitor SWOT Framework Specialist", 
                                     "Competitor Analysis Report Specialist"]):
            cleaned_data = cleaned_data.replace(term, f":{self.colors[idx%len(self.colors)]}[{term}]")
        self.buffer.append(cleaned_data)
        if "\n" in data:
            styled_content = f'<div style="font-size: 14px;">{"".join(self.buffer)}</div>'
            self.container.markdown(styled_content , unsafe_allow_html=True)
            # self.container.markdown(''.join(self.buffer) , unsafe_allow_html=True)
            self.buffer = []

def run():
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
run()