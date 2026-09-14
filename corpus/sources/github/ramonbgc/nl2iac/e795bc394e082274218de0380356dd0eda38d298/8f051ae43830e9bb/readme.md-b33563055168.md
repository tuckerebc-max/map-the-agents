# nl2iac
AI agent for IaC deployments

## installation
1. It's recommended to create and use a python virtual environment (not mandatory):
```sh
virtualenv YourOwnEnvName
cd YourOwnEnvName
source bin/activate
```

2. download/clone the repo 
3. install requirements:
```sh
pip install -r requirements.txt
```
4. add the following lines and fill the values in **.streamlit/secrets.toml**:

```sh
GOOGLE_APPLICATION_CREDENTIALS = "PathToYourServiceAccountJSONFile"
REGION = "GCPProjectRegion"
PROJECT_ID = "YourGCPProjectId"
GOOGLE_MODEL_ID = "gemini-1.5-flash" #default Google Model
MULTIPROVIDER = "False"
LANGCHAIN_API_KEY = "YourLangChainApiKey" # leave it blank if not in use
LANGCHAIN_PROJECT = "YourLangChainProjectName" # leave it blank if not in use
OPENAI_API_KEY = "YourOpenAIApiKey" # leave it blank if not in use
OPENAI_MODEL_ID = "gpt-4o" #default OpenAI Model
```