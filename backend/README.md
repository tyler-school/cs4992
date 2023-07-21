# How to get the back end running

### Step 1: Navigate to the backend directory (using the cd command)

### Step 2: Create a virtual python enviroment

Run the command:

    python3 -m venv .venv

### Step 3: Activate the virtual environment

make sure that you are in the directory containing the .venv folder

For Mac:
Run the command:

    . .venv/bin/activate

For Windows:
Run the command:

    .venv/Scripts/activate

Now your command line should start with (.venv)

### Step 4: Install necessary packages

To install FastAPI, run the command:

    pip install fastapi

To install uvicorn, run the command:

    pip install "uvicorn[standard]"

### Step 5: Select your virtual environment for the python interpreter in VS Code

Open VSCode, and open main.py. You should have an error ("fastapi could not be resolved") -> If you don't, then you can probably skip this step but no promises

In the file explorer pane on the left side of the screen, copy the path to the python .exe file in the .venv folder. To find the file, it should be in .venv/bin/. Copy the path to the file called "python". The path should look something like this:

    /Users/evangaus/Documents/evan-gaus/school/london/news-feed-folder/git-stuff/cs4992/backend/.venv/bin/python

In VS Code, hit Command + Shift + P to open the commands search, and search for "Python: Select Interpreter"

Select this option, then select the plus button that says "Enter interpreter path..."

Paste in the path to the python file you copied before, and hit enter

Now the error in main.py should be resolved

### Step 6: Use uvicorn to start the backend

Back to the terminal, run the command:
    uvicorn main:app --reload

That should have started the backend! If you navigate to the URL http://127.0.0.1:8000/ in a browser, you should see the message 
    {"Root API call"}

The backend should now be started!