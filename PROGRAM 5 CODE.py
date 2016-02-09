import csv

def try_open(file):
    try:
        opening_file = open(file, 'r')
        return True
    except IOError:
        print("I'm sorry, that file cannot be opened, please try again.")
    except:
        print("Please try again")

def try_output(file):
    try:
        opening_file = open(file, 'a')
        return True
    except IOError:
        print("I'm sorry, that file cannot be opened, please try again.")
    except:
        print("Please try again")

def fill_months(mon, Mon):
    key = str(keys)
    mons = str(mon)
    if mons in key:
        Mon.append(Months[keys])
        return Mon

def Avg_Rain(key,value):
    value = '{:.2f}'.format(value)
    AvgMonths[key] = value
    return AvgMonths


Months = {}
AvgMonths = {}
Jan = []
Feb = []
Mar = []
Apr = []
May = []
Jun = []
Jul = []
Aug = []
Sep = []
Oct = []
Nov = []
Dec = []
lines = []
Open_File = True
while Open_File == True:
    ##Input:
    ##    Ask user what file they would like to open
    File = input("What file would you like to open? ")
    ##    If that does not work because the file does not exist:
    while (".csv") not in File:
        print("That is not a valid file format.")
        File = input("What file would you like to open? ")
    ##    Try/Except:
    try_open(File)
    ##Second input:
    ##    Ask user what file they would like to output to
    Output_File = input("What file would you like to write to?")
    while (".csv") not in File:
        print("That is not a valid file format.")
        Output_File = input("What file would you like to open? ")
    try_output(Output_File)
    Input_File = open(File, 'r')
    ##Iterate through the csv file line by line
    for line in Input_File:
        Line = line.split(',')
        Line[1] = Line[1][:-1]
        if not Line[1].isalpha():
            Month = int(Line[0])
            Months[Month] = float(Line[1])
    for keys in Months:
        key = str(keys)
        if '0001' in key:
            Jan.append(Months[keys])
        fill_months('0001',Jan)
        fill_months('0002',Feb)
        fill_months('0003',Mar)
        fill_months('0004',Apr)
        fill_months('0005',May)
        fill_months('0006',Jun)
        fill_months('0007',Jul)
        fill_months('0008',Aug)
        fill_months('0009',Sep)
        fill_months('0010',Oct)
        fill_months('0011',Nov)
        fill_months('0012',Dec)
    SumJan = sum(Jan)/len(Jan)
    SumFeb = sum(Feb)/len(Feb)
    SumMar = sum(Mar)/len(Mar)
    SumApr = sum(Apr)/len(Apr)
    SumMay = sum(May)/len(May)
    SumJun = sum(Jun)/len(Jun)
    SumJul = sum(Jul)/len(Jul)
    SumAug = sum(Aug)/len(Aug)
    SumSep = sum(Sep)/len(Sep)
    SumOct = sum(Oct)/len(Oct)
    SumNov = sum(Nov)/len(Nov)
    SumDec = sum(Dec)/len(Dec)
    Avg_Rain(200001,SumJan)
    Avg_Rain(200002,SumFeb)
    Avg_Rain(200003,SumMar)
    Avg_Rain(200004,SumApr)
    Avg_Rain(200005,SumMay)
    Avg_Rain(200006,SumJun)
    Avg_Rain(200007,SumJul)
    Avg_Rain(200008,SumAug)
    Avg_Rain(200009,SumSep)
    Avg_Rain(200010,SumOct)
    Avg_Rain(200011,SumNov)
    Avg_Rain(200012,SumDec)
    YearRain = []
    Output_File = open(Output_File, 'a')
    for year, value in AvgMonths.items():
        Output_File.write('{},{}/n'.format(year, value))
    print("Monthly Averages")
    print("=====================")
    for keys in AvgMonths:
        print('{0:<10} {1:>10}'.format(keys, AvgMonths[keys]))