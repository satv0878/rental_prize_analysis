from pandas import DataFrame, Series
import numpy as np


def get_number_of_zero_values(column: Series):
    return column.size -np.count_nonzero(column)


def get_city_or_region(df: DataFrame, city:str): 
    return df[df.geo_bln ==city]
