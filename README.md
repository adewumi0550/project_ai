# Waste Management Customer Support Agent

This project contains a Google ADK (Agent Development Kit) agent designed to act as a customer support agent for waste management inquiries.

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone <repository_url>
cd project_ai # Replace project_ai with the actual directory name if different
```

### 2. Create and Activate a Python Virtual Environment

It is highly recommended to use a Python virtual environment to manage dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If you are on Windows, use:
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the `google-adk` package:

```bash
.venv/bin/python3 -m pip install google-adk
```

### 4. Obtain a Gemini API Key

This agent uses the Gemini API. You will need to obtain an API key from Google AI Studio.

1.  Go to [Google AI Studio](https://aistudio.google.com/apikey).
2.  Sign in with your Google account.
3.  Create a new API key or use an existing one.

### 5. Configure Your API Key

Create a `.env` file in the `customer_support` directory (if it doesn't already exist) and add your Gemini API key to it:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```
**Important**: Replace `your_gemini_api_key_here` with the actual API key you obtained. Ensure that this `.env` file is included in your `.gitignore` to prevent committing your API key to version control.

## Running the Agent

You can run the agent in two modes: Terminal (CLI) or Web UI (Playground).

### Terminal Mode (CLI)

For a quick chat interface in your terminal:

```bash
# Make sure your virtual environment is active
cd customer_support
/Users/adewumi0550/Desktop/project_ai/.venv/bin/adk run .
```

### Web UI (Playground)

For a visual interface to test and debug your agent, with a chat interface and real-time traces:

```bash
# Make sure your virtual environment is active
/Users/adewumi0550/Desktop/project_ai/.venv/bin/adk web
```
After running this command, open your browser to `http://127.0.0.1:8000`.

## Code Overview

The core logic of the agent is defined in `customer_support/agent.py`.

## Developing with Gemini CLI

This project is designed to be easily managed and developed with the assistance of the Gemini Command Line Interface (CLI). The Gemini CLI provides interactive assistance for coding tasks, documentation, and more.

### Installation

If you do not have the Gemini CLI installed, you can find installation instructions [here](https://geminicli.com/).

### Usage

The Gemini CLI can help you with various development tasks within this project, such as:

*   **Code Generation:** Generate new code or modify existing code based on natural language prompts.
*   **Refactoring:** Assist in refactoring code for better structure and readability.
*   **Documentation:** Generate documentation for your code.
*   **Debugging:** Help understand and fix issues in your code.

To interact with the Gemini CLI, simply describe your task or ask questions in your command line terminal.
