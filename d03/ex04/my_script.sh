#!/bin/bash
#use source my_script {venv_name} to execute
python3 -m venv $1
source $1/bin/activate
pip3 install -r requirements.txt

