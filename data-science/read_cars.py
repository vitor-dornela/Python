import pandas as pd
import polars as pl

# sep=',' is default, should change if needed (ex. sep=';')
# index_col='Car Name' is now the default index
df_cars = pd.read_csv('data-science/data/cars.csv', sep=',', index_col='Car Name') 
print(df_cars.head()) # print first 5 rows
print(df_cars.info()) # print info about the dataframe
print(df_cars.describe()) # print statistics about the dataframe

# To handle large datasets, it's recommended to use Polars library to read data
df_cars = pl.read_csv('data-science/data/cars.csv')
print(df_cars) 

people1 = pd.read_csv('data-science/data/hyperskill-dataset-91401981.txt', header=3)
print(people1.head(3))

people2 = pd.read_csv('data-science/data/hyperskill-dataset-91401981.txt', index_col='Name')
print(people2.head(5))
