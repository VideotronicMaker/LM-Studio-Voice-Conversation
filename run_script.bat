@echo off
REM Activate the Conda environment
call conda activate python

REM Change to the specific drive and directory
D:
cd /d D:\path\to your project\

REM Check if the directory change was successful
if not exist "%cd%" (
    echo The system cannot find the path specified: D:\path\to your project\
    goto end
)

REM Run the Python script
python speak.py

:end
pause
