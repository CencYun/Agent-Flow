\# MimoAgent-Flow: Multi-Agent Collaboration Framework



\## 1. 项目简介 / Project Overview

本项目是一个基于长链推理设计的 AI Agent 协作框架，旨在解决复杂软件开发任务中的自动化闭环问题。

This project is a multi-agent collaboration framework based on long-chain reasoning, designed to create an automated closed-loop for complex software development tasks.



\## 2. 核心特性 / Core Features

\- \*\*Task Decomposition\*\*: 将模糊的自然语言需求拆解为结构化的子任务图谱。

\- \*\*Agent Collaboration\*\*: 检索 Agent、开发 Agent 与评审 Agent 协同工作。

\- \*\*Self-Correction\*\*: 多轮对话上下文共享与自动化代码审查。



\## 3. 技术架构 / Architecture

\- \*\*Language\*\*: Python 3.9+

\- \*\*Core Engine\*\*: LLM (Planned to integrate MiMo Token Plan for deep reasoning)

\- \*\*Workflow\*\*: Orchestrator -> \[Searcher -> Developer] -> Reviewer -> Outcome



\## 4. 快速启动 / Quick Start

```bash

pip install -r requirements.txt

python demo\_workflow.py

