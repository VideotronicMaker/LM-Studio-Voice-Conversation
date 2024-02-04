@echo off
REM Activate the Conda environment
call conda activate python

REM Change to the specific drive and directory
D:
cd /d D:\LLM_Projects\Mistral_7B_Instruct\

REM Check if the directory change was successful
if not exist "%cd%" (
    echo The system cannot find the path specified: D:\LLM_Projects\Mistral_7B_Instruct\
    goto end
)

REM Run the Python script
python speak.py

:end
pause
