import subprocess
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.7,
)


# =====================
# Kubernetes Tools
# =====================

@tool
def get_pods() -> str:
    """
    Lists all pods in the Kubernetes cluster.
    """
    result = subprocess.run(
        ["kubectl", "get", "pods", "-A"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


@tool
def get_pod_logs(
    pod_name: str,
    namespace: str = "default"
) -> str:
    """
    Get logs of a Kubernetes pod.
    """
    result = subprocess.run(
        ["kubectl", "logs", pod_name, "-n", namespace],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


# =====================
# Docker Tools
# =====================

@tool
def get_docker_containers() -> str:
    """
    Get running Docker containers.
    """
    result = subprocess.run(
        ["docker", "ps"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


@tool
def get_docker_logs(
    container_name: str,
    tail: int = 100
) -> str:
    """
    Get logs of a Docker container.
    """
    result = subprocess.run(
        ["docker", "logs", "--tail", str(tail), container_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


@tool
def restart_docker_container(
    container_name: str
) -> str:
    """
    Restart a Docker container.
    """
    result = subprocess.run(
        ["docker", "restart", container_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


@tool
def docker_stats() -> str:
    """
    Show Docker CPU and memory usage.
    """
    result = subprocess.run(
        ["docker", "stats", "--no-stream"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


# =====================
# System Tools
# =====================

@tool
def get_disk_usage() -> str:
    """
    Show disk usage.
    """
    result = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


@tool
def get_memory_usage() -> str:
    """
    Show memory usage.
    """
    result = subprocess.run(
        ["free", "-h"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


agent = create_agent(
    model=llm,
    tools=[
        get_pods,
        get_pod_logs,
        get_docker_containers,
        get_docker_logs,
        restart_docker_container,
        docker_stats,
        get_disk_usage,
        get_memory_usage
    ],
    system_prompt="""
You are a DevOps assistant.

You can:
- List Kubernetes pods
- Show Kubernetes pod logs
- List Docker containers
- Show Docker logs
- Restart Docker containers
- Show Docker resource usage
- Show disk usage
- Show memory usage

Use tools whenever required.
"""
)

while True:
    question = input("Ask your agent: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = agent.invoke(
        {"messages": [("user", question)]}
    )

    print("\nAgent:")
    print(response["messages"][-1].content)
    print()
