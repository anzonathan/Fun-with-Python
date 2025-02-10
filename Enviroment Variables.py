#enviroment variables

import os

#get user enviroment variable
user = os.getenv("USER")

#get home path enviroment variable
home = os.getenv("HOME")

#get path for conda
conda = os.getenv("CONDA_EXE")

print(conda)
