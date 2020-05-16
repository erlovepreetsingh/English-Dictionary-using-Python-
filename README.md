# English-Dictionary-using-Python-
These are Python scripts to make an interactive English Dictionary which is very user friendly.    

## Features of this dictionary code-
1. It is very user friendly.
2. It suggests you the simillar word if you enter any wrong word that is not is dictionary.
3. It gives you the one or more meaning as according to the database.

## File in the repositry-
=> There are two types of scripts are present in the repositry.One script named "python_word_dict.py" requires the "data.json" file to execute.That "data.json" file consist of a offline data base for the dictionary which can be edited to expand the dictionary words as user want.


=> Another file named "dictionary_finder_sqlConnect.py" is work the same as 1st one but only difference is that it do not require any offline dictionary database of some kind it works standalone. This script requires an INTERNET CONNECTION to work because it has a online MySQL database.

## Requirements to run the code-
1. Python 3.0 or upper
2. mysql.connector library 

### Note - If mysql.connector library is not installed use cmd command - `pip install mysql.connector`
## How to use-
1. Clone the files in the repositry to your system. Make sure the "data.json" and "python_word_dict.py" should be at same location because these two files work together. File named "dictionary_finder_sqlConnect.py" can work freely do not requires any other files.
2. Run the Pyhton script file using CMD.

