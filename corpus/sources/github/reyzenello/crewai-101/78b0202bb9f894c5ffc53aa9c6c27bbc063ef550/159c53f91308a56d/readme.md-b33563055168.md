# CrewAI-101
Testing around framework using multi-agent using CrewAI

Steps to try out the CrewAI on Windows:

First step is to crete a system environment variable on Windows by using the following steps: Method 1: Through the Control Panel Open the Control Panel:
Press the Windows key and type "Control Panel", then open the application. Go to System and Security:

Click on "System and Security", then "System". Advanced System Settings:

In the left panel, click on "Advanced system settings". Environment Variables:

In the window that opens, click on "Environment Variables". Add the Variable:

Under "System variables", click "New". Variable name: OPENAI_API_KEY Variable value: your_openai_api_key (replace with your actual API key) Click "OK" to close all windows. Method 2: Through the Command Prompt Open Command Prompt as Administrator:

Press the Windows key, type "cmd", right-click on "Command Prompt" and select "Run as administrator". Set the Environment Variable:

cmd setx OPENAI_API_KEY "your_openai_api_key" /M /M means that the variable will be set at the system level (for all users). Method 3: Through PowerShell Open PowerShell as Administrator:

Press the Windows key, type "PowerShell", right-click on "Windows PowerShell" and select "Run as administrator". Set the Environment Variable:

powershell [System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your_openai_api_key", "Machine") Method 4: Using a .env Configuration File You can use a .env configuration file to set environment variables. This method is especially useful for projects using a virtual environment or specific frameworks like Django or Flask.

Create a .env File in Your Project Directory:

makefile OPENAI_API_KEY=your_openai_api_key Load the .env File in Your Python Script:

python from dotenv import load_dotenv import os

load_dotenv() # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY") Ensure you install the python-dotenv package:

bash pip install python-dotenv Method 5: Modifying the Registry (Advanced) Note: Modifying the registry can be risky. Proceed with caution and, if possible, back up the registry before making changes.

Open the Registry Editor:

Press Windows + R, type regedit, and press Enter. Navigate to the Appropriate Key:

Go to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment. Add a New Environment Variable:

Right-click on "Environment", select "New" -> "String Value". Name: OPENAI_API_KEY Double-click the new entry and enter your API key as the value. By using one of these methods, you can set the OPENAI_API_KEY environment variable on Windows.

Once you have already configured and set the utils.py by adding the OPENAI_API_KEYS you can download the repo and perform the following commands to testing out AutoGen:
pip install crewAI utils
python CrewAI-task.py

Here are the result:
![image](https://github.com/Reyzenello/CrewAI-101/assets/43668563/84eaf09d-cca4-4b1d-acb7-8d4e1a6e3fbf)

