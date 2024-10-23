venv for git bash terminal:
    To create a new venv: python3.12 -m venv chudgetingENV

    To activate the venv: source chudgetingENV/Scripts/activate
    To deactivate the venv (yes, this is it): deactivate

Running and stop Django Server:
    change directory to 'backend'
    migrate changes: python manage.py migrate
    
    Run the server: python manage.py runserver
    Stop the server: CTRL+C

Making and using requirements.txt
    To create the file: pip freeze > requirements.txt
    To use the file: pip install -r requirements.txt
