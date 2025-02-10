#enviroment variables

import os

#get user enviroment variable
user = os.getenv("USER")

#get home path enviroment variable
home = os.getenv("HOME")

#get path for conda
conda = os.getenv("CONDA_EXE")

#create enviroment variable
os.environ["passkey"] = "Am I the only one I know"

passkey = os.getenv("passkey")

print(passkey)
