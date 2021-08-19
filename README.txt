This file is a README file for the dissertation project:
Implementing an efficient randomized algorithm for testing equality of integers succinctly represented by arithmetic circuits with addition and multiplication.
By: Pierluigi Giulivi

This zip file contains the dissertation pdf and two folders, data and code.


Data contains all the datasets for each test and the R code necessary to create the graphs. 
The only missing information is in the "divisors" test, as the dataset was around 9GB. You can still find the R code and the corresponding graph.


Code contains all the python code needed to generate the data.

EquSLP.py is the algorithm itself ready to be used.

EquSLPData is a modified version of EquSLP where the algorithm needs the random integer for input because we have other functions in the same file that will choose the random integer from different ranges to perform tests and calculate failure probabilities.

Test.py creates an extensive set of arithmetic circuits to be compared depending on some selected variables. It uses EquSLPData to compare the circuits it generates.

Divisors.py calculates the distribution of divisors of integers depending on the number of bits of the divisors.

EquSLPTest.py is used to test the EquSLP algorithm run time depending on the input size or the number of bits used for the random integer.