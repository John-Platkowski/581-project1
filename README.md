## How to setup the app

1. Configure a Python virtual environment if you wish

2. Make sure python and pip are properly installed on your system

### Option 1

3. Run **`python3 run.py`**

Should this option fail fallback to option 2

### Option 2

3. Run **`pip install -r requirements.txt`** in the project's root directory

4. After doing so you should be able to run **`python3 -m uvicorn main:app --reload`**, this should launch the server

5. To access the app go to a browser and type **`http://localhost:8000/`** into the search bar
