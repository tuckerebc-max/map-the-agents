# Helm App Deployment with OPA Verification and AI-Assisted Fixes

This repository contains a simple Helm chart for deploying a "Hello World" Nginx application, along with Open Policy Agent (OPA) rules for verification and an AI-assisted mechanism to fix policy violations.

## Prerequisites

- Helm 3+
- OPA
- Python 3+
- OpenAI API key (for ChatGPT integration)

## Helm Chart

The Helm chart in the `helm/` directory deploys a simple Nginx server with a "Hello World" page.

## OPA Verification
The OPA policies in the opa/ directory verify the Helm chart against predefined rules. To run the verification:

This script will:

Detect OPA policy violations
Use ChatGPT to suggest fixes
Apply the fixes to the relevant files
Create a new branch with the changes
Push the branch and create a pull request
