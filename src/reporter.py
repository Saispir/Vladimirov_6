import pandas as pd
class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all
    
    def show_report(self, df, title=None):
        if title:
            print(title)
    
        print('Количество столбцов:', df.shape[1])
        print('Количество строк:', df.shape[0])

        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)

        print('Доля дубликатов:', format(duplicates / df.shape[0], self.percent_format))

        print(df.describe(include='all' if self.include_all else None))

        total_cells = df.shape[1] * df.shape[0]
        missing_values_count = df.isnull().sum().sum()
        missing_values_share = (missing_values_count / total_cells) if total_cells > 0 else 0.0
        formatted_missing_share = format(missing_values_share, self.float_format)
        
        # выведите количество пропусков во всем датафрейме одним числом
        print(f"Количество пропусков: {missing_values_count}")
        
        # выведите долю пропусков во всем датафрейме одним числом с плавающей точкой
        # в формате float_format
        print(f"Доля пропусков: {formatted_missing_share}")


import pandas as pd

data = pd.read_csv('data/payments.csv')

# не нужно менять код ниже - он для проверки правильности работы show_report с разными настройками
reporter_1 = DataFrameReporter(float_format='0.02f', percent_format='0.03%')
reporter_2 = DataFrameReporter(float_format='0.03f', percent_format='0.01%', include_all=True)

reporter_1.show_report(data, 'Отчёт в формате 1:')
print()
reporter_2.show_report(data, 'Отчёт в формате 2:')