# LM-Studio-Voice-Conversation

Welcome to the LM Studio Local Server setup guide. This guide will walk you through the process of running a local server with LM Studio, enabling you to use Hugging Face models on your PC without an internet connection and without needing an API key. The repository includes six Python (.py) files. For comprehensive functionality, focus on `lmst_inline.py` and `lmst_ext.py`. You only need to run one of these files to start the local server.

## Getting Started
Here's how to get the project up and running on your local machine.

### Prerequisites
- **Anaconda**: Download it from [Anaconda's official site](https://www.anaconda.com/).
- **LM Studio**: Available at [LM Studio's website](https://lmstudio.ai/).

### Setting Up Your Python Environment
1. **Install Anaconda**: Follow the installation instructions for your OS from the Anaconda website.

2. **Create a New Conda Environment** (recommended):
   ```bash
   conda create -n myenv python=3.9.18
   ```
   Replace `myenv` with a name of your choice for the environment.

3. **Activate the Environment**:
   ```bash
   conda activate myenv
   ```

### Clone the Repository
Clone the LM-Studio-Voice-Conversation repository:
```bash
git clone https://github.com/VideotronicMaker/LM-Studio-Voice-Conversation
```

4. **Install Required Packages**:
   Navigate to the cloned directory and install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
- **LLM Python Script (`speak.py`)**: Main script for the language model.

To run the script, execute this command in your terminal:
```bash
python speak.py

# How to Run `run_script.bat`

1. **Open Command Prompt**: Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

2. **Navigate to the Directory**: If you're not already in the directory where the `run_script.bat` file is located, use the `cd` command to navigate to the directory where your code is stored. Replace `<code_directory>` with the actual path to your code directory:

   ```batch
   cd /d <code_directory>

```
   Make sure to replace the path with the actual path to the directory containing the run_script.bat file.

1- Run the Batch Script: Once you are in the correct directory, simply execute the run_script.bat file by typing its name and pressing Enter:

   `run_script.bat`

2- Activate Conda Environment: The batch script will attempt to activate the Conda environment named python.

3- Check Directory Change: It will check if the directory change was successful. If it encounters an issue and cannot find the specified path, it will display an error message: "The system cannot find the path specified."

4- Run Python Script: If the directory change is successful, it will proceed to run the Python script named speak.py.

5- Completion and Pause: After executing the Python script, the batch script will pause, allowing you to review any output or messages displayed by the Python script.

You should see the output of the Python script in the Command Prompt window. If there are any issues with the script or its execution, error messages will be displayed in the Command Prompt, helping you identify and address any problems.


You can copy and paste this Markdown code into your documentation or README file as needed.


## Development Environment Setup

For detailed instructions on setting up and using Visual Studio Code with this project, please see [VSCode Instructions](VSCodeSetup.md).



## Need More Help?
If you're new to using command line interfaces for tasks like navigating directories, creating folders, or managing Python environments, resources like ChatGPT or Gemini Pro can provide detailed, step-by-step guidance.
