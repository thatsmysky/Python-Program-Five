# Python-Program-Five
This program was intended to take the input of a file on rainfall by month and average them.  THIS PROGRAM DOES NOT RUN CORRECTLY.  The output is only for one year, it should be for as many years as you want.  This is because the month is read as a string, not an integer.

Program 5 Algorithm

Input: Ask user what file they would like to open

    Try/Except:

        Try to open the file to read.

        If that does not work because the file does not exist: 

        Tell user it doesn’t exist, ask again

            If the file won’t read because it is empty:

                Tell user it is empty, ask again

            If it fails for any other reason:

                Tell the user it failed, ask to try again

Second input: Ask user what file they would like to output to

    Try/Except:

        Try to open the file to write

        If that doesn’t work because the file is a directory:

            Tell the user it won’t work, ask again

        If the file won’t write for any other reason:

            Tell the user it didn’t work, ask again

Iterate through the csv file line by line

Split line into 2 strings; ‘date’, ‘amount of rain’

For each day in a month, add the precipitation, and divide it by how many days in the month rain was measured for

if there is no data for a date; N/A:

    skip the line

Once you have gone through the entire month, write the month and average precipitation in the Output file

Repeat for every month until the end of the file. 

Iterate through the Output file line by line

Split line into 2 strings; ‘date’, ‘avg precip’

Change format of month to say name of month instead of number

Ask user if they would like to see a graph:

    If Yes, produce graph 

Output once program has run should look like 2 columns; Month and Avg Precip, underlined.  Below those should be the data.
