# csv_context.py
import pandas as pd

class CSVContext:
    dataframe = None  # Shared object

    @classmethod
    def set_result(cls, df):
        cls.dataframe = df

    @classmethod
    def get_result(cls):
        return cls.dataframe

class CSVInfoContext:
    info = None  # Shared object

    @classmethod
    def set_info(cls, info):
        cls.info = info

    @classmethod
    def get_info(cls):
        return cls.info
class CodeContext:
    code = None  # Shared object

    @classmethod
    def set_code(cls, info):
        cls.code = info

    @classmethod
    def get_code(cls):
        return cls.code
class ChartCodeContext:
    code = None  # Shared object

    @classmethod
    def set_code(cls, info):
        cls.code = info

    @classmethod
    def get_code(cls):
        return cls.code

class ResultContext:
    result = None  # Shared object

    @classmethod
    def set_result(cls, result):
        cls.result = result

    @classmethod
    def get_result(cls):
        return cls.result

class DataPathContext:
    path = None  # Shared object

    @classmethod
    def set_path(cls, path):
        cls.path = path

    @classmethod
    def get_path(cls):
        return cls.path