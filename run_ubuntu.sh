#!/usr/bin/env bash

#
# The python script depends on the colorama and requests module, that can be installed with pip.
# This is an example setup script for Debian-based distributions (Debian/Ubuntu).
# It creates a venv, installs the python dependencies in it and runs the python script.
# For other distributions, adapt this script to use your package manager.
#
# Usage :    ./run_ubuntu.sh                          # run in english
#            ./run_ubuntu.sh fr ./words_fr.txt        # run in french
#

# install the package required to create a python venv
sudo apt install python3.10-venv

# create a venv
python3 -m venv myenv

# activate the venv
source ./myenv/bin/activate

# install python modules
pip3 install colorama
pip3 install requests

# start the Cemantle assistant script
lang=${1:-"en"}
wordlist=${2:-"./words_en.txt"}
sudo ./cemantle_assistant.py "--lang" "$lang" "--wordlist" "$wordlist"