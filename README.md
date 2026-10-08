
# PromptLab AI

## Prompt Engineering Dashboard

PromptLab AI is an interactive web application built with Python and Streamlit to demonstrate and compare different prompt engineering techniques using Large Language Models (LLMs).

The application allows users to enter a task, select a prompting strategy, configure model settings, and generate AI responses. It also supports comparing multiple prompting strategies to understand how different prompt structures influence model outputs.

---

## Features

- Interactive Streamlit dashboard
- Multiple prompt engineering strategies
- Single-strategy analysis
- Compare multiple strategies
- AI-generated responses
- Adjustable creativity/temperature
- Multiple response detail levels
- Generated prompt preview
- Response generation time
- Clean and professional user interface
- API-based LLM integration
- Modular project structure

---

## Prompt Engineering Techniques

### 1. Zero-Shot Prompting

The model receives a task without any examples.

**Example:**

```text
Explain machine learning in simple terms.
````

Zero-shot prompting is useful when the task is straightforward and the model can understand the instruction directly.

---

### 2. One-Shot Prompting

The model receives one example before solving the actual task.

**Example:**

```text
Example:
Q: What is the capital of France?
A: The capital of France is Paris.

Now answer:
Q: What is the capital of Japan?
A:
```

One-shot prompting provides the model with a basic example of the expected response format.

---

### 3. Few-Shot Prompting

The model receives multiple examples before solving the task.

**Example:**

```text
Q: What is 2 + 2?
A: 4

Q: What is 5 + 5?
A: 10

Q: What is 10 + 10?
A:
```

Few-shot prompting helps guide the model using several demonstrations.

---

### 4. Chain of Thought (CoT)

The task is divided into smaller reasoning steps.

**Example:**

```text
Solve the problem step by step.
Break the problem into smaller parts,
solve each part,
and provide the final answer.
```

Chain of Thought prompting is useful for tasks that require multiple reasoning steps.

---

### 5. Tree of Thought (ToT)

Tree of Thought prompting explores multiple possible approaches before selecting the most suitable solution.

The application asks the model to:

1. Generate multiple approaches
2. Develop each approach
3. Evaluate the approaches
4. Select the best approach
5. Provide the final answer

This technique is useful for complex problems where multiple solutions are possible.

---

## Dashboard Modes

### Single Strategy

Users can select one prompt engineering technique and generate a response.

### Compare Strategies

Users can select multiple techniques and compare the responses generated using different prompting methods.

This makes it easier to understand how prompt design affects LLM outputs.

---

## Model Settings

The dashboard provides configurable model settings.

### Creativity

Controls the temperature of the model.

* Lower value → More deterministic responses
* Higher value → More creative responses

### Response Detail

Users can select:

* Short
* Medium
* Detailed
* Very Detailed

### Show Generated Prompt

Users can enable this option to view the actual prompt constructed by the application before sending it to the LLM.

---

## Technology Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Application development         |
| Streamlit             | Web dashboard                   |
| Large Language Models | AI response generation          |
| Groq API              | LLM inference                   |
| Hugging Face          | Alternative LLM inference       |
| python-dotenv         | Environment variable management |

---

## Project Structure

```text
PromptLab AI/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

### app.py

Contains the Streamlit dashboard, user interface, strategy selection, model settings, and response display.

### llm.py

Handles communication with the configured Large Language Model API and manages model settings.

### prompt_templates.py

Contains the prompt templates and implementations for:

* Zero-Shot
* One-Shot
* Few-Shot
* Chain of Thought
* Tree of Thought

### requirements.txt

Contains all Python dependencies required to run the project.

### .env

Stores API credentials and model configuration.

### .gitignore

Prevents sensitive files such as API keys and virtual environment files from being uploaded to GitHub.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/promptlab-ai.git
```

Move into the project directory:

```bash
cd promptlab-ai
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is not available, install the required packages:

```bash
pip install streamlit python-dotenv groq huggingface_hub
```

---

## API Configuration

Create a `.env` file in the project root directory.

### Using Groq

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

### Using Hugging Face

```env
HF_TOKEN=your_huggingface_token
HF_MODEL=Qwen/Qwen2.5-72B-Instruct
```

Do not upload your API keys to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

```bash
python -m streamlit run app.py
```

After starting the application, open the local URL provided by Streamlit:

```text
http://localhost:8501
```

---

## How the Application Works

The overall workflow is:

```text
User enters a task
        ↓
Selects prompt strategy
        ↓
Prompt template is generated
        ↓
Model settings are applied
        ↓
Prompt is sent to the LLM
        ↓
LLM generates response
        ↓
Response displayed in dashboard
```

For comparison mode:

```text
                    User Task
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
    Zero-Shot      Few-Shot          CoT
        ↓              ↓              ↓
    Response       Response       Response
        └──────────────┼──────────────┘
                       ↓
                 Compare Results
```

---

## Example Use Case

Suppose the user enters:

```text
Explain the difference between Artificial Intelligence,
Machine Learning, and Deep Learning.
```

The application can generate responses using:

```text
Zero-Shot
One-Shot
Few-Shot
Chain of Thought
Tree of Thought
```

The user can then compare the responses and observe how different prompt structures affect the generated output.

---

## Advantages

* Easy to use
* Interactive learning environment
* Demonstrates practical prompt engineering
* Supports multiple prompting strategies
* Allows strategy comparison
* Configurable model behavior
* Modular Python architecture
* Suitable for LLM and Generative AI learning

---

## Learning Outcomes

Through this project, users can understand:

* What prompt engineering is
* How Zero-Shot prompting works
* How One-Shot prompting works
* How Few-Shot prompting works
* How Chain of Thought prompting works
* How Tree of Thought prompting works
* How prompt structure affects LLM responses
* How to integrate LLM APIs with Python
* How to build an AI dashboard using Streamlit

---

## Future Enhancements

Possible future improvements include:

* Prompt history
* Response rating system
* Export responses as PDF
* Download generated prompts
* Response comparison charts
* Token usage tracking
* Response quality evaluation
* BLEU and ROUGE evaluation
* Additional prompting techniques
* Support for multiple LLM providers
* User authentication
* Persistent conversation history

---

## Security

API keys should never be committed to the GitHub repository.

Use environment variables through the `.env` file and include `.env` in `.gitignore`.

Before pushing the project to GitHub, verify that no API keys or other credentials are present in the repository.

---

## Project Purpose

PromptLab AI was developed as an educational project to demonstrate how prompt engineering techniques can influence the behavior and output of Large Language Models.

The project combines prompt engineering concepts with practical LLM API integration and an interactive Streamlit interface.

---

## Author

**Varalakshmi K**

B.Sc Computer Science with Artificial Intelligence

Interested in Machine Learning, Generative AI, Large Language Models, and Prompt Engineering.

---

## License

This project is intended for educational and academic purposes.


```
```
