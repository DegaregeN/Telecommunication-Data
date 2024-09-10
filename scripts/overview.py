import sys

import numpy as np
import pandas as pd
from logger import Logger


class Overview:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        try:
            self.df = df
            self.logger = Logger("overview.log").get_app_logger()
            self.logger.info(
                'Successfully Instantiated Outlier Class Object')
        except Exception:
            self.logger.exception(
                'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)

    # how many missing values exist or better still what is the % of missing values in the dataset?

    def percent_missing(self, df: pd.DataFrame):
        """Get the percentage of missing values in the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be preprocessed

        Returns:
            pd.DataFrame: the dataframe
        """
        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        self.logger.info(
            "Missing value of the dataset calculated")
        print("The telecom dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

        # return df

    def number_of_duplicates(self, df):
        """Return the number of duplicates in the dataset.

        Args:
            df (pd.DataFrame): Dataset to be analyzed
        """
        duplicated_entries = df[df.duplicated()]
        self.logger.info(
            'Number of duplicated fields calculated')
        print(duplicated_entries.shape)

    def get_skewness(self, df):
        """Return the skewness of the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
        """
        # calculate skewness
        skewness = df.skew(axis=0, skipna=True)
        self.logger.info(
            'Skewness calculated')
        return skewness

    def get_decile(self, df: pd.DataFrame, column: str, decile: int, labels: list = []) -> pd.DataFrame:
        """Get the decile based on the column.

        Args:
            df (pd.DataFrame): Dataset to be used for Decile
            column (str): column to calculate the decile
            decile (int): number of decile
            labels (list, optional): Decile labels. Defaults to [].

        Returns:
            pd.DataFrame: Calculated decile
        """
        df['deciles'] = pd.qcut(df[column], decile, labels=labels)
        return df