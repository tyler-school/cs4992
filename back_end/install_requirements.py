#!/usr/bin/env python3
import os
par_dir = os.path.join(os.path.dirname(__file__), os.pardir)
os.system('pip install --upgrade pip')
os.system(f'cd {par_dir}; ls')
os.system(f'pip install {par_dir}')
from nltk import download
download('all-corpora')
main_path = os.path.join(par_dir, 'back_end')
os.system(f'cd {main_path}; uvicorn main:app --reload')