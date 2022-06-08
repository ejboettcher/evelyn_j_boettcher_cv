"""
This script reads in a pandas dataframe (df).

Author: Evelyn J. Boettcher
Date: 2022

"""

import argparse
import pandas as pd
import time
import helpers.lg_csv as lg_csv

def UserInputs():
    # List of inputs.
    parser  = argparse.ArgumentParser()
    parser.add_argument("-c","--cat", type=int, help="User Categories to read in: c=1 is true, default false",required=False, default=0)
    parser.add_argument("-f","--file", type=str, help="csv file to read in",required=False, default="My_Awesome.csv")
    parser.add_argument("-d","--day", type=str, help="Day of week to pull out", required=False,default="")
    parser.add_argument("-r", "--random", type=int, help="Read in file with random string", default=1)
    args = parser.parse_args()
    return args

def main(args):
    use_categories = args.cat
    tic = time.time()
    strcol = ["HELLO",'Locations','Days',"HELLO_c",'Locations_c','Days_c']
    if arg.file == "My_Awesome.csv":
        rancol = ['Random_String']
    else:
        rancol = []
    datafile = args.file
    if use_categories == 0:
        print("Not using categories for any columns")
        df = lg_csv.lg_csv_read(datafile, [],[],[],strcol+rancol)
    else:
        print("USING CATEGORIES for columns that make sense.")
        df = lg_csv.lg_csv_read(datafile, strcol,[],[],rancol)
    toc = time.time()
    print("_____"*10)
    print("")
    print('It took this many seconds to read in the csv file %.2f' % (toc-tic))
    print("_____"*10)
    print('Now lets look at size')
    print("Memory of Df is: ",lg_csv.df_mem_usage(df))
    print("Top 4 rows of data")
    print(df[1:5])
    return df


if __name__=='__main__':
    print('Starting')
    arg = UserInputs()
    if arg.random != 1:
        arg.file = "./My_Awesome_cat.csv"
        print(arg.file)
    df = main(arg)
    if len(arg.day) > 0:
        tic = time.time()
        df_d = df['Days'][df['Days']==arg.day]
        toc = time.time()
        print(df_d[1:4])
        print("_____" * 10)
        print("")
        print('It took this many seconds %.3f to find ' % (toc-tic),  arg.day)
        print("_____" * 10)
