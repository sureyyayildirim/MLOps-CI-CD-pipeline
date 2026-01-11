# MLOps CI/CD Pipeline Project

This repository demonstrates an end-to-end **MLOps-oriented CI/CD pipeline** for a machine learning prediction service.  
The system ensures that every code change is automatically tested, validated, packaged, and verified before being considered deployable.

The pipeline follows the **Stop-the-Line** principle:  
if any validation step fails, the deployment process is immediately halted.

---

##  System Overview

The system consists of a FastAPI-based prediction service, automated testing, Docker-based packaging, and a GitHub Actions CI/CD pipeline.

Key features:
- Unit & component testing
- Static code analysis (linting)
- Docker image packaging
- End-to-end smoke testing
- Automated failure prevention (stop-the-line)

---

##  A. Component Diagram — System Architecture

The following diagram illustrates the main components of the system and how they interact.

```mermaid
flowchart LR
    A[Git Repository<br/>(Source Code & Tests)]
    B[CI Pipeline<br/>(GitHub Actions)]
    C[Docker Image<br/>(Build Artifact)]
    D[Prediction Service<br/>(FastAPI Container)]

    A -->|git push / PR| B
    B -->|docker build| C
    C -->|docker run| D

```
Component Descriptions
- Git Repository:
  Central location containing application code, tests, Dockerfile, and pipeline configuration.
- CI Pipeline (GitHub Actions):
  Automates testing, linting, packaging, and validation on every code change.
- Docker Image:
  Packaged, deployable artifact built after successful validation.
- Prediction Service:
  Running FastAPI service providing health check and prediction endpoints.

## B. Sequence Diagram — Workflow Execution & Stop-the-Line Logic
This diagram shows the time-ordered execution flow of the CI/CD pipeline, highlighting the stop-the-line mechanism.

sequenceDiagram
    participant Dev as Developer
    participant CI as CI Pipeline
    participant Env as Container Environment

    Dev->>CI: git push
    CI->>CI: Run Unit Tests
    CI->>CI: Run Lint (Static Analysis)

    alt Tests or Lint Fail
        CI-->>Dev: Pipeline Failed (Stop the Line)
    else Tests & Lint Pass
        CI->>CI: Build Docker Image
        CI->>Env: Run Container
        CI->>Env: Smoke Test (/health, /predict)

        alt Smoke Test Fail
            CI-->>Dev: Pipeline Failed (Stop the Line)
        else Smoke Test Pass
            CI-->>Dev: Deployment Successful
        end
    end

## Why This Matters

This sequence explicitly demonstrates that:

- Code is not packaged or deployed without passing validation
- Failures are detected early
- Deployment is treated as a result of verification, not just container startup

This addresses the common misconception that “a workflow that only builds and runs is sufficient.

## Testing Strategy 

**Unit Tests**

- Validate deterministic feature engineering logic
- Fast, isolated, and dependency-free

**Component Tests**

- Validate interaction with file system resources
- Simulate real-world data dependencies

**Smoke Tests**

- Validate the running container via real HTTP requests
- Ensure service availability and correct responses

## Stop-the-Line Principle
The pipeline enforces a strict stop-the-line policy:

- ❌ Test or lint failure → pipeline stops
- ❌ Smoke test failure → pipeline stops
- ✅ Only fully validated builds are considered deployable

This approach prevents broken or unstable models from reaching production environments.

## Technologies Used
- Python 3.11
- FastAPI
- Pytest
- flake8
- Docker
- GitHub Actions

## Conclusion
This project demonstrates a complete and production-inspired MLOps CI/CD pipeline.
By combining automated validation, containerization, and strict execution order, the system ensures reliability, reproducibility, and deployment safety.