"""
File that contains the utilities (classes and/or functions) for the main project.

"""

import os
from datetime import datetime
from project import config

class GENERAL:
    """
    Class that contains general use functions for common work.

    """

    def hello():
        """
        Example function that prints a simple line by terminal.

        """
        print(f"Hello! Today is {datetime.today().date()} and you are working on the root of {os.path.basename(os.getcwd())}.")

    def file_to_drive(worksheet, df, drive_file_name, folder_id, index_included=True, deleting=False):
        """
        Function that uploads a file into Google Drive.

        """
        gc = gspread.oauth(config.path_credentials)
        sh = gc.open(title=drive_file_name,folder_id=folder_id)
        if deleting:
            actual_worksheet = sh.worksheet(worksheet)
            actual_worksheet.clear()
        set_with_dataframe(sh.worksheet(worksheet), df,include_index=index_included)

    def months_between(d1, d2):
        """
        Function that calculates months between the two given dates.

        """
        dd1 = min(d1, d2)
        dd2 = max(d1, d2)
        return (dd2.year - dd1.year)*12 + dd2.month - dd1.month
