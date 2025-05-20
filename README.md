# Chatpot - AI Chat Application

A modern chat application that uses AI to generate responses, built with FastAPI backend and Streamlit frontend.

## Project Structure

```
Chatpot_grad_project/
├── Chatpot/                    # Backend directory
│   ├── api.py                 # FastAPI application
│   └── chat_arch/             # Chat architecture
│       └── chat.py            # ChatBot implementation
├── notebooks/                  # Jupyter notebooks
│   └── try_chat.ipynb         # Testing and development notebook
├── frontend.py                # Streamlit frontend application
├── Pipfile                    # Pipenv dependencies
├── Pipfile.lock              # Locked dependencies
└── .env                      # Environment variables (not tracked in git)
```

## Features

- 🤖 AI-powered chat responses using Hugging Face models
- 🚀 FastAPI backend for efficient API handling
- 💻 Streamlit frontend for a clean user interface
- 📝 Chat history tracking
- 🔒 Environment variable management for API keys

## Prerequisites

- Python 3.10 or higher
- pipenv (for dependency management)
- Hugging Face API token

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Chatpot_grad_project
```

2. Install dependencies using pipenv:
```bash
pipenv install
```

3. Create a `.env` file in the root directory:
```
MY_TOKEN=your_huggingface_token_here
```

4. Activate the virtual environment:
```bash
pipenv shell
```

## Running the Application

1. Start the FastAPI backend:
```bash
uvicorn Chatpot.api:app --reload
```

2. In a new terminal, start the Streamlit frontend:
```bash
streamlit run frontend.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Development

- The backend API is available at `http://localhost:8000`
- API documentation is available at `http://localhost:8000/docs`
- Use the notebooks in the `notebooks/` directory for testing and development

## Project Components

### Backend (FastAPI)
- Handles chat requests
- Integrates with Hugging Face models
- Provides RESTful API endpoints

### Frontend (Streamlit)
- User-friendly chat interface
- Real-time message display
- Chat history management

### ChatBot Class
- Manages model interactions
- Handles API key management
- Processes user messages

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

[Add your license here]

## Contact

[Add your contact information here]
