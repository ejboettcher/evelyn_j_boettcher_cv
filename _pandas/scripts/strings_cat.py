"""
This script builds a pandas dataframe (df) of strings.
The length of the data frame is (n)
There are columns with and without categories 
The last column is created from a random characters of length (-r) 

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
    parser.add_argument("-s","--save", type=int, help="save to csv",required=False, default=0)
    args = parser.parse_args()
    return args

def main(args):
    r = args.range
    n = args.length
    print('Building three DF with: ')
    print('     length of random string in a row 1-',r)
    print('     length of DF ',n)
    # Set the number of rows our DF is going to have.
    df =  build.strings_columns_NoCat(n) # Build 3 columns of string data withOUT Categories
    dfc = build.strings_columns(n) # Build 2 columns of string data WITH categories
    dfr = build.random_str(n,r) # Build a string df with 1 to r length
    # Make them into on DF
    df_All = pd.concat([df,dfc,dfr],axis=1 , sort=False)
    print("Top 10 rows of data")
    print(df_All[1:10])

    # Get Size
    print("Size of the DF we just made")
    print("String NO Categories     ", lg_csv.df_mem_usage(df))
    print("String WITH Categories   ", lg_csv.df_mem_usage(dfc))
    print("Random String (1 column) ", lg_csv.df_mem_usage(dfr))
    print("_____"*4)
    print("Now lets make them all into categories")
    # Make the DF into categories
    names = ["HELLO",'Locations','Days']
    dfsz_cat = lg_csv.df_mem_usage(df[names].astype('category'))
    dfsz = lg_csv.df_mem_usage(df[names])
    dfsave = int((float(dfsz[:-2])-float(dfsz_cat[:-2])) / float(dfsz[:-2]) * 100)
    dfcsz_cat = lg_csv.df_mem_usage(dfc.astype('category'))
    dfcsz = lg_csv.df_mem_usage(dfc)
    dfcsave = int((float(dfcsz[:-2])-float(dfcsz_cat[:-2]))/float(dfcsz[:-2]) * 100)
    print("String Columns: HELLO, Locations, Days")
    print("NO CAT to category (plain df, category, SAVINGS)--->", dfsz,',',dfsz_cat,',',dfsave,'%')
    print("Cat df to category (plain df, category, SAVINGS)--->", dfcsz,',',dfcsz_cat,',',dfcsave,"%")
    #print("INT8 ",lg_csv.df_mem_usage(dfi8))
    print("___NOTE___" * 4)
    #print("Categories reduced the size INT df!!")
    #print("   BUT because of the overhead ")
    #print("   it did not reduce the int8 size")
    print("")
    print("Now, let's try this with random STRINGS")
    a = lg_csv.df_mem_usage(dfr)
    c = lg_csv.df_mem_usage(dfr['Random_String'].astype('category'))
    print("String: Random         ---> ",a)
    print("String: Random category---> ",c)
    if float(c[:-2])>float(a[:-2]):
         print("Categories only made the DF memory use worse")
    else:
        print("__________________________" * 2)
        print("WHAT.......")
        print("   There was an improvement!!!")
        print("   HOW  DID  THAT  HAPPEN????")
        print("__________________________" * 2)
    return df_All


if __name__ == '__main__':
    print('Starting')
    arg = UserInputs()
    df = main(arg)
    if arg.save == 1:
        print("Saving df as a csv")
        df.to_csv('my_awesome.csv', index=False)
        df[["HELLO",'Locations','Days',"HELLO_c",'Locations_c','Days_c']].to_csv('My_Awesome_cat.csv', index=False)
