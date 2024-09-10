import sys

import numpy as np
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join('./')))
# from logger import Logger


class PreProcess:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        try:
            self.df = df
            # self.logger = Logger("preprocessing.log").get_app_logger()
            # self.logger.info(
            # 'Successfully Instantiated Outlier Class Object')
        except Exception:
            # self.logger.exception(
            # 'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)

    def convert_to_datetime(self, df, column: str):
        """Convert a column to a datetime.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): dataframe column to be converted
        """
        df[column] = pd.to_datetime(
            df[column], errors='coerce')
        # self.logger.info(
        # 'Converted datetime columns to datetime')
        return df

    def convert_to_float(self, df, column: str):
        """Convert column to float.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): Column to be converted to string
        """
        self.df[column] = df[column].astype(float)
        # self.logger.info(
        # 'Successfully converted to float columns')
        return self.df

    def drop_variables(self, df):
        """Drop variables based on a percentage.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            percentage(int): Percentage of variables to be dropped
        """
        df_before_filling = df.copy()
        df = df[df.columns[df.isnull().mean() < 0.3]]
        missing_cols = df.columns[df.isnull().mean() > 0]
        print(missing_cols)
        # self.logger.info(
        #     'Missing columns are: ', missing_cols)
        return df, df_before_filling, missing_cols

    def clean_feature_name(self, df):
        """Clean labels of the dataframe.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        df.columns = [column.replace(' ', '_').lower()
                      for column in df.columns]
        # self.logger.info(
        #     'Cleaned feature names')
        return df

    def rename_columns(self, df: pd.DataFrame, column: str, new_column: str):
        """Rename a column.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): column to be renamed
            new_column (str): New column name
        """
        df[column] = df[column].rename(new_column)
        dfRenamed = df.rename({column: new_column}, axis=1)
        return dfRenamed

    def fill_numerical_variables(self, df):
        """Fill numerical variables.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        df_single = df
        cols = df_single.columns
        num_cols = df_single.select_dtypes(include=np.number).columns
        df_single.loc[:, num_cols] = df_single.loc[:, num_cols].fillna(
            df_single.loc[:, num_cols].median())
        print(num_cols)
        print(df_single.loc[:, num_cols].median())
        # self.logger.info(
        #     'Filled missing numerical variables')
        return cols, df_single, num_cols

    def fill_categorical_variables(self, df, cols, num_cols, df_single):
        """Fill categorical variables.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            cols(list): List of columns
            num_cols(list): List of numerical columns
            df_single(pd.DataFrame): Dataframe with filled numerical variables
        """
        cat_cols = list(set(cols) - set(num_cols))
        df_single.loc[:, cat_cols] = df_single.loc[:, cat_cols].fillna(
            df.loc[:, cat_cols].mode().iloc[0])
        df_cols = df_single.columns
        print(cat_cols)
        print(df_single.loc[:, cat_cols].mode().iloc[0])
        # self.logger.info(
        #     'Filled missing categorical variables with mode')
        return df_cols, df_single, cat_cols

    def drop_duplicates(self, df):
        """Drop duplicates.

        Args:
            df (pd.DataFrame): A dataframe to be preprocessed
        """
        df = df.drop_duplicates()

        return df

    def convert_bytes_to_megabytes(self, df, col):
        """Convert byte data to megabyte.

        Args:
            df (pd.DataFrame): A dataframe to be preprocessed
        """
        megabyte = 1*10e+5
        megabyte_col = df[col] / megabyte
        # self.logger.info(
        #     'Converted bytes to megabytes')
        return megabyte_col