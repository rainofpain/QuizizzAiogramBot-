# Quizizz Telegram Bot

## About


## Navigation
- [Installation](#installation) 

## Installation

1. Clone the repository
```
git clone https://github.com/rainofpain/QuizizzAiogramBot-.git
```
2. Choose main directory of the project
```
cd QuizizzAiogramBot-
```
3. Create virtual environment
```
python -m venv venv
```
4. Activate virtual environment
* Activation for **Git Bash**
```
source venv/Scripts/activate
```
* Activation for **Windows Powershell**  
     
1. Allow execution of local scripts
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
2. Activate **venv**
```
venv\Scripts\Activate.ps1 
```

* Activation for **Windows cmd**
```
call venv/Scripts/activate
```
* Activation for **MacOS** / **Linux**
```
source venv/bin/activate
```
5. Install all required packages
```
pip install -r requirements.txt
```
6. Create your own `.env` in main directory

7. Fill your `.env` with the information required for the **bot** as in the `.env-sample` file in main directory

8. Run the project (run `main.py`)
```
python main.py
```
