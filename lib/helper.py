from pandas import DataFrame, Series
import numpy as np


def get_number_of_zero_values(column: Series):
    '''takes a series and returns the number of zero entries in that column'''
    return column.size -np.count_nonzero(column)


def get_city_or_region(df: DataFrame, city:str): 
    '''takes a dataframe and a string and returns the dataframe filtered by the string'''
    return df[df.regio2 == city]
