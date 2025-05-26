# Multiple LLM CLI

A Python CLI to interact with multiple LLMs via the OpenRouter API. Select a model, ask questions, and maintain conversation history.

## Prerequisites

- Python 3.12+
- `uv` (install from uv docs)
- OpenRouter API key

## Getting an API Key

1. Create an account on OpenRouter.
2. Go to the API Keys section.
3. Generate a new API key and copy it.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd openrouter
   ```

2. Set up virtual environment:

   ```bash
   uv venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   uv sync
   ```

4. Add API key to `.env`:

   ```bash
   OPENROUTER_API_KEY=your-api-key-here
   ```

## Usage

Run the CLI:

```bash
uv run main.py
```

- Select a model using arrow keys.
- Enter queries; type `quit` to exit.
- View conversation history on exit.

Example:

```
Select any model: deepseek-v3-0324:free
Ask LLM (type 'quit' to exit): What's the capital of France?
The capital of France is Paris.
Ask LLM (type 'quit' to exit): quit
Exiting...

Conversation History:
1. Query: What's the capital of France?
   Response: The capital of France is Paris.
```

## Dependencies

- `python-dotenv`
- `inquirer`
- `requests`

## Notes

- Keep `.env` out of version control.
- History resets per session and is sent to the LLM for context.
- Check OpenRouter API token limits.

## Troubleshooting

- Verify API key in `.env`.
- Ensure Python 3.12+ and `uv sync` success.
