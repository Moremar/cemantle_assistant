# Cemantle Assistant

Script for the Cemantle word game that enters an initial list of common words.

Cemantle website : https://cemantle.certitudes.org/

The game is great, but entering initially the same common words every day is tedious and repetitive.  
This tool allows to automatically check a few common words to get an initial direction.  
It displays the score of the words of the list from best to worst, with their percentile if they are in the top 1000.

If you give it a try, please do not use it maliciously to DoS the Cemantle website.  
It is a free game that everyone can enjoy, please respect it.


## Usage

The `cemantle_assistant.py` Python script has a dependency on the `colorama` and `requests` Python modules.  
They can be installed with the `pip` package manager.

```shell
./cemantle_assistant.py --lang en --wordlist ./words_en.txt --max_rows 10
```

The `run_ubuntu.sh` Bash script provides an example of setup from scratch to run the Python script on Ubuntu.  
It creates a Python venv, installs the Python dependencies in it and executes the Python script.
