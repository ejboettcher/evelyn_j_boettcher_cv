import pandas as pd
import build_csv as build
import lg_csv as lg_csv


n=100000
dfi = build.int_columns(n,4)
dff = build.float_columns(n,4)
dfi8 = build.int8_columns(n,4)

print("INT ",lg_csv.df_mem_usage(dfi))
print("INT8 ",lg_csv.df_mem_usage(dfi8))
print("FLOAT ",lg_csv.df_mem_usage(dff))

df = pd.concat([dfi,dfi8,dff],axis=1 , sort=False)

print("Top 10 rows of data")
print(df[1:10])

print("INT category---"  ,lg_csv.df_mem_usage(dfi['INT'].astype('category')),dfi.astype('category').info())
print("INT8 category---",lg_csv.df_mem_usage(dfi8['INT8'].astype('category')),dfi8.astype('category').info())
print("Float--- ",lg_csv.df_mem_usage(dff['FLOAT']),dff.info())
print("Float category---",lg_csv.df_mem_usage(dff['FLOAT'].astype('category')),dff.astype('category').info())
