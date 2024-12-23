# Multi-Agent Competitor Analysis

This project implements a multi-agent architecture for performing comprehensive competitor analysis. Leveraging modern LLM capabilities, such as the Llama 3.1 8B model via Ollama, it integrates multiple agents to aggregate and analyze data from various sources.

## Features
- **Multi-Agent Design**: Powered by Crewai to coordinate tasks efficiently.
- **Language Model Integration**: Utilizes Ollama with Llama 3.1 8B for natural language processing and insight generation.
- **Customizable Agents and Tasks**: Configure agent roles and workflows via YAML configuration files.
- **API Integration**: Uses SerperDevTool for enhanced search capabilities (requires `SERPER_API_KEY`).

## Project Structure
```
Multi-Agent-Competitor-Analysis/
├── requirements.txt            # Dependencies for the project
├── src/                        # Source code for the project
│   ├── __init__.py             # Package initializer
│   ├── app.py                  # Main application logic
│   ├── crew.py                 # Multi-agent management with Crewai
│   ├── test.py                 # Test cases for validation
│   └── config/                 # Configuration files
│       ├── agents.yaml         # Agent definitions
│       └── tasks.yaml          # Task workflows
└── .env                        # Environment variables (not included by default)
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nahidbrur/Multi-Agent-Competitor-Analysis.git
   cd Multi-Agent-Competitor-Analysis
   ```

2. **Install Dependencies**

   Ensure you have Python 3.12 installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   N.B. You can create a virtual environment with python 3.12 first.

3. **Set Up Environment Variables**

   Create a `.env` file in the project root and add your `SERPER_API_KEY`:
   ```env
   SERPER_API_KEY=<your-api-key>
   ```
   N.B. You can create serper API from [serper.dev](https://serper.dev/)

4. **LLM setup**

   Llama 3.1 8B is a powerful large language model, easily deployed locally via Ollama for efficient 
   and customizable AI interactions. To setup ollama with llama3.1, please follow the below instruction.
   
   1. Download and setup ollama from [here](https://ollama.com/download).
   2. Pull the llama3.1 model by
      ```bash
      ollama pull llama3.1:8b
      ```
   N.B. If you want to use openai please follow [this](https://docs.crewai.com/how-to/llm-connections) instruction, setup openai credentials like api key, api base etc in **.env** file and change the below code snippet of [crew.py](src/crew.py) script.
      ```py
      llm = LLM(
         model='ollama/llama3.1:8b',
         base_url='http://localhost:11434',
	   )
      ```

5. **Run the Application**

   Goto `src` folder by
   ```bash
   cd src
   ```
   Run the test script by passing input query as:
   ```bash
   python test.py --query Apple
   ```
   Launch the streamlit application and navigate to the [url](http://localhost:8501):
   ```bash
   streamlit run app.py
   ```

## Technologies Used
- **[Crewai](https://www.crewai.com/)**: Multi-agent orchestration framework.
- **[Ollama](https://ollama.com/)**: Integration with Llama 3.1 8B for LLM-based tasks.
- **[SerperDevTool](https://serper.dev/)**: API for enhanced web search capabilities.

## License
This project is licensed under [MIT License](LICENSE).
