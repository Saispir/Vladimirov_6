import pandas as pd

class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df: pd.DataFrame, title: str = None):
        if title is not None:
            print(title)
        num_columns = df.shape[1]
        num_rows = df.shape[0]
        num_duplicates = df.duplicated().sum()
        duplicates_share = (num_duplicates/num_rows) if num_rows > 0 else 0.0
        formatted_duplicates_share = format(duplicates_share, self.percent_format)
    # добавьте в класс метод show_report
        print(f"Количество столбцов: {num_columns}")
        print(f"Количество строк: {num_rows}")
        print(f"Количество дубликатов: {num_duplicates}")
        print(f"Доля дубликатов: {formatted_duplicates_share}")
    
reporter = DataFrameReporter()

import pandas as pd

data = pd.read_csv('payments.csv')

# вызовите метод show_report для reporter, передав в него датафрейм
reporter.show_report(data)