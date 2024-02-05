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
```
## Development Environment Setup

For detailed instructions on setting up and using Visual Studio Code with this project, please see [VSCode Instructions](VSCodeSetup.md).



## Need More Help?
If you're new to using command line interfaces for tasks like navigating directories, creating folders, or managing Python environments, resources like ChatGPT or Gemini Pro can provide detailed, step-by-step guidance.
