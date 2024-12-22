#!/usr/bin/env python
import streamlit as st
import sys
import warnings
from crew import CompetitorAnalyst
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'https://www.daraz.com.bd'
    }
    CompetitorAnalyst().crew().kickoff(inputs=inputs)
run()
