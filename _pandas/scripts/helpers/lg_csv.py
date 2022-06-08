"""
Author: Evelyn J. Boettcher, DiDacTex, LLC
Date: 20190621
Description: Python script to read in large csv files (~10GB)
      It utilizes categories to reduce the in memory usage by 90%

NOTE: Categories only are useful if the data values in a column repeats  by 50%
  Example: Days of weeks, people names, places all tend to repeat

"""
import pandas as pd


def lg_csv_read(datafile, catcolumns, floatcolumns=[], datetimecol=[], noncatcol=[]):
    '''
    WARNING:
    ========
        Only inputted columns are exported out in the DataFrame!!

    ARGS:
    =====
      datafile: str (csv file that you want to read in)
      catcolumns: list (list of columns in the csv files that can be categories)
           e.g. have 50% row repeats
      floatcolumns: list of columns that you want declared as floats 16
      datetimecol: list of columns that can be converted to pandas datetime format
      noncatcol: Lis tof columns that you want read in but can't be categorized

    RETURNS:
    ========
       df: pandas dataframe (reduced memory df because categories are utilized!!)
    '''
    column_types = dict() # Build a dictonary of column types
    for k in catcolumns:
        column_types[k]='category'
    for k in floatcolumns:
        column_types[k]='float16'
    columnsread = catcolumns+ floatcolumns + datetimecol + noncatcol
    if len(datetimecol)>0:
        df = pd.read_csv(datafile, usecols=columnsread, dtype=column_types,
          parse_dates=datetimecol, infer_datetime_format = True)
    else:
        df = pd.read_csv(datafile, usecols=columnsread, dtype=column_types)
    return df


def fillNA_categories(df, labelsna, textstr='Unk'):
    '''
    WARNING:
    ========
        ASSUMES categories are being used!!

    ARGS:
    =====
        df = pandas DataFrame
        labelsna: list of columns that you want na labes as textstr
        textstr: str (String that you want the na replaced with)
    RETURNS:
    ========
       df = dataframe
    '''
    for lna in labelsna:
        df[lna] = df[lna].cat.add_categories(textstr).fillna(textstr)
        df[lna] = df[lna].cat.remove.unused_categories()
    return df


def df_mem_usage(pandas_obj):
    '''
    Calculates how much memory a pandas_obj (df or series) is taking
    RETURNS:
        mem_size: Str

    '''
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else: # Assumes it is a Series
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b/1024**2
    return "{:03.4f}MB".format(usage_mb)
