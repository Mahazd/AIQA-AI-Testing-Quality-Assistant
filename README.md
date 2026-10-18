AIQA AI Testing & Quality Assistant

Where AI Meets Quality Engineering

A personal proof-of-concept exploring how Retrieval-Augmented Generation (RAG), user feedback, and human-in-the-loop review can support software testing knowledge and AI response quality.

Project Showcase: This repository presents AIQA through its documentation, demonstration, screenshots, and selected source code examples. The complete application source code remains private.

Overview

AIQA is a locally running AI assistant designed to answer software testing questions using a curated knowledge base.

Beyond traditional question answering, AIQA incorporates feedback collection, quality monitoring, and human review to support the assessment and continuous improvement of AI-generated responses.

Key Features

Knowledge-Grounded Q&A — Uses RAG to generate responses informed by a local software testing knowledge base.

User Feedback Collection — Captures helpful and not helpful ratings, feedback reasons, and optional comments.

Quality Insights Dashboard — Visualizes answer helpfulness, feedback trends, and pending reviews.

Human-in-the-Loop Review — Supports manual review, issue classification, and documentation of findings.

Local-First Architecture — Uses a locally hosted language model and vector database.

Code Highlights

AIQA combines Generative AI with Software Quality Engineering practices to support continuous quality improvement.

Selected source code examples demonstrate:

Feedback Monitoring: Tracking user ratings and answer helpfulness.

Quality Insights: Analyzing negative feedback and identifying areas requiring attention.

Human Review Workflow: Classifying potential issues and recording review outcomes.

📁 [examples/quality_monitoring.py]

The published examples demonstrate selected implementation concepts and do not represent the complete application. User feedback does not automatically retrain the AI model.

Technology Stack
| Area | Technology |
|---|---|
| Application Interface | Python, Streamlit |
| RAG Orchestration | LangChain |
| Local Model Runtime | Ollama |
| Language Model | Llama 3.2 |
| Embeddings | nomic-embed-text |
| Vector Database | Chroma |
| Feedback Tracking | CSV-based prototype storage |

Demonstration

Watch AIQA in action, from knowledge-grounded question answering to feedback collection, quality insights, and human review.

🎬 [https://github.com/Mahazd/AIQA-AI-Testing-Quality-Assistant/releases/download/v1.0/AIQA.mp4]



Project Screenshots


![AIQA Assistant](aiqa-assistant.png)


![Quality Insights](quality-insights.png)


![Human Review](Human-review.png)

Quality Engineering Focus

AIQA explores more than generating answers. Its quality-focused design includes:

Grounding responses in a curated knowledge base.

Capturing explicit user feedback about answer usefulness.

Monitoring feedback trends through a quality dashboard.

Supporting human assessment of responses requiring review.

Classifying potential issues to inform future improvements.

Prototype Scope: Current metrics reflect submitted user feedback and manual review activity. They are not independently validated measures of model accuracy, retrieval quality, or production readiness.

Future Improvements

Build structured evaluation datasets with expected answers.

Introduce retrieval and response-quality evaluation metrics.

Expand automated regression testing for AI responses.

Enhance feedback analysis and reporting.

Expand knowledge coverage.

Evaluate security, deployment, and data-governance requirements.

Project Status

Personal Proof of Concept — Ongoing Development

AIQA is an independent learning and portfolio project using general software testing knowledge. It is not intended to expose organizational systems or confidential information.

Author:
Maha Alshalahi
Software Quality Engineer | ISTQB CT-GenAI Certified

Exploring the intersection of Software Quality Engineering, Generative AI, and Human-Centered AI Evaluation.
