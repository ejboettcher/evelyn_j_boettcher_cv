"""
This script builds a pandas dataframe (df) of numbers.
The length of the data frame is (n)
There are columns with and without categories 
The range of numbers is from 1 to r 

Author: Evelyn J. Boettcher
Date: 2022

"""

import argparse
import pandas as pd
import helpers.build_csv as build
import helpers.lg_csv as lg_csv


def UserInputs():
    # List of inputs.
    parser  = argparse.ArgumentParser()
    parser.add_argument("-r","--range", type=int, help="Max Range of numbers: 1-r",required=False, default=4)
    parser.add_argument("-n","--length", type=int, help="Length of df eg number of rows",required=False, default=10000)
    args = parser.parse_args()
    return args

def main(args):
    r = args.range
    n = args.length
    print('Building three DF with: ')
    print('     range of numbers 1-', r)
    print('     length of DF ', n)
    # Set the number of rows our DF is going to have.
    dfi = build.int_columns(n, r) # Build an int df with number 1 to r
    dff = build.float_columns(n, r) # Build a float df with num 1 to r
    dfi8 = build.int8_columns(n, r) # Build a int8 df with num 1 to r
    # Make them into on DF
    df = pd.concat([dfi,dfi8,dff],axis=1 , sort=False)
    print("Top 10 rows of data")
    print(df[1:10])

    # Get Size
    print("Getting size of the DF we just made")
    print("INT   ", lg_csv.df_mem_usage(dfi))
    print("INT8  ", lg_csv.df_mem_usage(dfi8))
    print("FLOAT ", lg_csv.df_mem_usage(dff))
    print("_____" * 4)
    print("As categories")
    # Make the DF into categories
    dfisz_cat = lg_csv.df_mem_usage(dfi['INT'].astype('category'))
    dfisz = lg_csv.df_mem_usage(dfi)
    dfisave = int((float(dfisz[:-2])-float(dfisz_cat[:-2])) / float(dfisz[:-2]) * 100)
    dfi8sz_cat = lg_csv.df_mem_usage(dfi8['INT8'].astype('category'))
    dfi8sz = lg_csv.df_mem_usage(dfi8)
    dfi8save = int((float(dfi8sz[:-2])-float(dfi8sz_cat[:-2]))/float(dfi8sz[:-2]) * 100)
    print("INT  df (plain df, category, SAVINGS)--->", dfisz,',',dfisz_cat,',',dfisave,'%')
    print("INT8 df (plain df, category, SAVINGS)--->", dfi8sz,',',dfi8sz_cat,',',dfi8save,"%")
    #print("INT8 ",lg_csv.df_mem_usage(dfi8))
    print("___NOTE___" * 4)
    print("Categories reduced the size INT df!!")
    print("   BUT because of the overhead ")
    print("   it did not reduce the int8 size")
    print("")
    print("Now, let's try this with random Floats")
    print("Float         ---> ", lg_csv.df_mem_usage(dff['FLOAT']))
    print("Float category---> ", lg_csv.df_mem_usage(dff['FLOAT'].astype('category')))
    print("Categories only made the DF memory use worse")



if __name__=='__main__':
    print('Starting')
    arg = UserInputs()
    main(arg)
