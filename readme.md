# pdf-merger for windows os
A pdf merger for windows with instruction on setting up a virtual environment 

## requirements 
python 

## instructions 

### In your project folder:
python -m venv venv  # Creates virtual environment in 'venv' folder
.\venv\Scripts\activate  # Activates the environment
pip install -r requirements.txt  # Installs dependency ONLY in the virtual environment

### Now run your script (will use the virtual environment's packages)
python merge_and_compress.py

### When done, deactivate and remove the environment:
deactivate
rmdir /s /q venv  # Removes all temporary packages