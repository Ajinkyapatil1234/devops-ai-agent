DevOps AI Agent

A local AI-powered DevOps assistant built with Python, LangChain, Ollama, Docker, and Kubernetes.

This project uses a local LLM running through Ollama and LangChain tool-calling to perform common DevOps tasks through natural language.

Features

Kubernetes

* List all pods in the cluster
* View pod logs
* Monitor Kubernetes resources

Docker

* List running containers
* View container logs
* Restart containers
* View container resource usage

System Monitoring

* Check disk usage
* Check memory usage

AI Capabilities

* Natural language interface
* Tool-calling agent architecture
* Local execution using Ollama
* No cloud APIs required

⸻

Tech Stack

* Python
* LangChain
* Ollama
* Qwen 3 0.6B
* Docker
* Kubernetes
* Linux / WSL

⸻

Project Architecture

User Query
↓
LangChain Agent
↓
Ollama LLM
↓
Tool Selection
↓
Docker / Kubernetes / Linux Commands
↓
Response Generation

⸻

Installation

Clone Repository

git clone https://github.com/YOUR_USERNAME/devops-ai-agent.git
cd devops-ai-agent

Create Virtual Environment

python -m venv .venv
source .venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Install Ollama

Make sure Ollama is installed and running.

Pull the model:

ollama pull qwen3:0.6b

Verify Tools

Docker:

docker ps

Kubernetes:

kubectl get pods -A

⸻

Run the Agent

python agent.py

Example:

Ask your agent: show running docker containers
Ask your agent: show disk usage
Ask your agent: restart nginx container
Ask your agent: show kubernetes pods

To exit:

exit

⸻

Example Questions

Docker

Show running docker containers
Show logs for nginx
Restart the nginx container
Show docker stats

Kubernetes

Show all pods
Get logs for pod xyz
List pods across namespaces

System

Show disk usage
Show memory usage

⸻

Screenshots

Add screenshots here after running the agent.

Examples:

* Listing Docker containers
* Viewing container logs
* Checking Kubernetes pods
* System resource monitoring

⸻

Learning Outcomes

This project helped me learn:

* LangChain agents
* Tool calling
* Local LLM deployment with Ollama
* Docker administration
* Kubernetes operations
* Linux system monitoring
* AI-powered automation

⸻

Future Improvements

* Docker container inspection
* Kubernetes pod description
* Deployment restart support
* CPU monitoring
* Conversation memory
* Streamlit web interface
* Authentication and safety controls

⸻

License

MIT License
