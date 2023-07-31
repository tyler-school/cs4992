#!/usr/bin/env python3
import os
import argparse
from threading import Thread
from multiprocessing import Process, freeze_support

parser = argparse.ArgumentParser(description='app starter')

# Declare an argument (`--algo`), saying that the
# corresponding value should be stored in the `algo`
# field, and using a default value if the argument
# isn't given
parser.add_argument('--install', action="store_true", dest='INSTALL', default=False)

root_repo = os.path.join(os.path.dirname(__file__))
front_end_dir = os.path.join(root_repo, 'frontend')
back_end_dir = os.path.join(root_repo, 'back_end')
def run_backend():
    command = f'cd {back_end_dir}; uvicorn main:app --reload'
    os.system(command)
    
def run_frontend():
    os.system(f'cd {front_end_dir}; npm start')

if __name__ == '__main__':
    args = parser.parse_args()
    INSTALL = args.INSTALL
    if INSTALL:
        print("|||||||||||||||||||||||||\n"
              "Starting backend install\n"
              "|||||||||||||||||||||||||\n")
        os.system('pip install --upgrade pip')
        os.system(f'cd {root_repo}; ls')
        os.system(f'pip install {root_repo}')
        from nltk import download
        download('all-corpora')
        print("|||||||||||||||||||||||||||||||\n"
              "Downloaded backend dependencies\n"
              "|||||||||||||||||||||||||||||||\n")


    if INSTALL:
        print("|||||||||||||||||||||||||\n"
              "Starting frontend install\n"
              "|||||||||||||||||||||||||\n")
        os.system(f'cd {front_end_dir}; npm install')
        print("|||||||||||||||||||||||||||||||\n"
              "Downloaded frontend dependencies\n"
                "||||||||||||||||||||||||||||||\n")


    
    
    be_thread = Thread(target=run_backend)
    be_process = Process(target=run_backend)

    
    fe_thread = Thread(target=run_frontend)
    fe_process = Process(target=run_frontend)
    print("|||||||||||||||||\n"
          "STARTING FRONTEND\n"
          "|||||||||||||||||\n")

    fe_process.start()

    print("|||||||||||||||||||||||||||||||\n"
          "STARTING BACKEND\n"
          "|||||||||||||||||||||||||||||||\n")
    be_process.start()


    fe_process.join()
    be_process.join()
