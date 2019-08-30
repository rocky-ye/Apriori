Python Implementation of Apriori Algorithm 

A listing of files:

1. Apriori.py
2. T10I4D100Kc.txt
3. README(this file)


Usage:

This program should be executable with 3 parameters: the name of the input dataset file, the threshold of minimum support count, and the name of the output file (in that order). 

For example, to run the program with the test file, a support of 500, and the output name of outPutFile.txt:

    python3 Apriori.py T10I4D100K.txt 500 outPutFile.txt
 

This program should output a file that contains all the frequent itemsets together with their support counts. Each line contains a single frequent itemset as a list of items separated by a single space. Its support count is included between a pair of parentheses at the end of the line. For example: 1 2 3 (5) represents an itemset containing items 1, 2, and 3 with a support count of 5. 

Results for the following values of support:  

Support: 

400: 89 seconds

500: 29 seconds

600: 16 seconds
  


