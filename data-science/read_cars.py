import pandas as pd
import polars as pl

# sep=',' is default, should change if needed (ex. sep=';')
# index_col='Car Name' is now the default index
df_cars = pd.read_csv('data-science/data/cars.csv', sep=',', index_col='Car Name') 
print(df_cars.head()) # print first 5 rows

# To handle large datasets, it's recommended to use Polars library to read data
df_cars = pl.read_csv('data-science/data/cars.csv')
print(df_cars) 