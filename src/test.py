import sys
import warnings
from crew import CompetitorAnalyst
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(query):
    """
    Run the crew.
    """
    inputs = {
        'topic': str(query)
    }
    result = CompetitorAnalyst().crew().kickoff(inputs=inputs)
    print(result)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Product/Company name or website")

    args = parser.parse_args()

    run(args.query)
