# Philipe Couto challenge

## My anwsers about questions
### 1 - The average complexity, I say average because each method has a complexity, which can vary to treat each file. So the average complexity is o(n) which is a good complexity for handling files. Talking about swaps, I chose loops (avoiding nested loops) for reading the files and create the anwsers files, which generates a linear complexity, but can increase the execution time as the files get bigger.

### 2 - First i will create a function to look all file header and get the columns name (or maybe create a new class to handle with this) and then modify the data processing functions: Update the data processing functions (count_legislator_votes, count_bill_legislators, etc.) to extract the values for the new columns from the CSV files. Modify the CSVHandler class and put the columns in to array with all columns names. And at last i will chage the CSV Generator to handle with new fields.

### 3 - It would make small adjustments to the HandleCSV class for whatever new data type it might be, like lists or stacks. This class handles the data it receives. Perhaps I would also choose a more generic name.

### 4 - To complete this task I spent about 3 hours and 25 minutes.

## Git Hub of final version 
  https://github.com/lipecouto/Quorum-code-Challenge

You can see all branchs in this repository and all commits

## Git Hub execution

git clone `git@github.com:lipecouto/Quorum-code-Challenge.git`


and then

## Code Execution steps:

To execute the code, follow these steps:

1. Make sure you have Python installed on your machine. The code was developed using Python 3.

2. Copy the code into a file with the `.py` extension, for example, `main.py`.

3. Ensure that you have the input CSV files (`bills.csv`, `legislators.csv`, `vote_results.csv`, `votes.csv`) in the same directory as the `main.py` file.

4. Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

5. Run the code by typing the following command in the terminal: `python main.py`.

6. The code will process the CSV files, count the legislator votes and the legislators per bill, and generate the output CSV files.

7. At the end of execution, you will find the generated output CSV files: `legislators-support-oppose-count.csv` and `bills.csv`. These files will contain the requested information from the challenge.

Make sure you have the proper permissions to read and write files in the directory where you are executing the code. Also, double-check the CSV file names and ensure they contain the expected data as described in the challenge.

Note: If you are running the code in an integrated development environment (IDE) like Visual Studio Code, you can directly execute it by pressing the run button provided by the IDE.