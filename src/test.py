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
    result = CompetitorAnalyst().crew().kickoff(inputs=inputs)
    print(result)
run()
