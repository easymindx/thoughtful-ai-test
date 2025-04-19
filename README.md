# Thoughtful AI Support Agent

A simple customer support AI agent that provides information about Thoughtful AI's suite of AI-powered automation agents.

## Features

- Terminal-based chat interface for asking questions about Thoughtful AI's agents
- Provides detailed information about EVA, CAM, PHIL, and other Thoughtful AI agents
- Fallback responses for questions outside of the predefined knowledge base
- No external dependencies - uses only Python standard library

## Installation

Just clone this repository - no additional dependencies required!

## Usage

Run the agent with:

```bash
python terminal_agent.py
```

Interact with the agent directly in your terminal.

## How It Works

The agent uses a simple word-matching algorithm to find the best response from a predefined set of questions and answers about Thoughtful AI's products. For questions that don't match any predefined data, it provides a generic response.

In a production environment, a more sophisticated approach using embeddings or a proper NLP pipeline would be recommended. 