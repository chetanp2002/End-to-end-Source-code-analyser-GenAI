# RepoBot AI

![My Image](https://raw.github.com/chetanp2002/images/main/RepoBot%201.png)
![My Image](https://raw.github.com/chetanp2002/images/main/RepoBot%202.png)

RepoBot AI is an innovative AI-powered web application designed to help developers analyze and understand GitHub repositories. By automating repository ingestion, processing and indexing code files using advanced vector search techniques, and providing interactive natural language responses, RepoBot AI transforms static codebases into interactive knowledge hubs.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Automated Repository Ingestion:**  
  Clones GitHub repositories and processes over **500+ code files** automatically for seamless analysis.

- **Vector-Based Code Search:**  
  Splits code into meaningful segments and leverages **Chroma DB** and **HuggingFace Embeddings** for fast semantic search across **300+ code segments**.

- **Interactive Conversational AI:**  
  Integrates **Groq AI** and **LangChain Conversational Retrieval Chains** to enable natural language Q&A sessions, providing real-time insights into codebases.

- **Scalable Data Pipeline:**  
  Automates the entire workflow—from repository ingestion and text chunking to embedding storage—ensuring efficient and scalable code analysis.

## Tech Stack

- **Backend:** Python, Flask
- **AI & NLP:** LangChain, Groq AI, HuggingFace Embeddings
- **Vector Database:** Chroma DB
- **Version Control:** Git, GitPython
- **Utilities:** psutil, python-dotenv
- **Frontend:** HTML, CSS, Bootstrap

## Installation

### Prerequisites

- Python 3.8+
- Git
- pip

### Clone the Repository

```bash
git clone https://github.com/yourusername/RepoBot-AI.git
cd RepoBot-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

*Alternatively, install key dependencies directly:*

```bash
pip install flask langchain chromadb gitpython python-dotenv psutil langchain-huggingface
```

### Environment Variables

Create a `.env` file in the root directory with the following keys:

```dotenv
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

## Usage

### Running the Application

Start the Flask server by running:

```bash
python app.py
```

Open your browser and navigate to `http://0.0.0.0:8080` to access the interface.

### How It Works

1. **Repository Ingestion:**  
   Enter a GitHub repository URL in the UI. The `repo_ingestion()` function (in `src/helper.py`) clones the repository into a local `repo/` folder.

2. **Indexing & Embedding:**  
   The `store_index.py` script loads the cloned repository, splits the code into text chunks, and creates vector embeddings that are stored in a persistent Chroma DB for efficient semantic retrieval.

3. **Interactive Q&A:**  
   Users ask natural language questions about the repository, and the conversational retrieval chain powered by Groq AI returns relevant code insights and responses.

## Project Structure

```
RepoBot-AI/
├── app.py                  # Main Flask application and API endpoints
├── store_index.py          # Script for creating and persisting vector embeddings
├── src/
│   └── helper.py           # Helper functions for repository ingestion, text splitting, and embedding
├── templates/
│   └── index.html          # HTML template for the UI
├── static/                 # Static assets (CSS, JavaScript, images)
├── .env                    # Environment variables (not tracked in Git)
└── requirements.txt        # Python dependencies list
```

## Deployment

RepoBot AI can be deployed on cloud platforms such as [Render](https://render.com). Ensure your deployment environment is configured with the appropriate environment variables and supports ephemeral storage for cloned repositories.

## Contributing

Contributions are welcome! Please fork this repository, make your improvements, and open a pull request. For major changes, open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [LangChain](https://langchain.com)
- [Groq AI](https://groq.ai)
- [Chroma](https://www.trychroma.com)
- [HuggingFace](https://huggingface.co)
- [Flask](https://flask.palletsprojects.com)
- [GitPython](https://gitpython.readthedocs.io)
