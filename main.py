import pandas as pd
from src.reporter import DataFrameReporter


def main():
    data = pd.read_csv('data/payments.csv')
    reporter = DataFrameReporter()
    reporter.show_report(data, title="Отчёт по анализу датасета")


if __name__ == '__main__':
    main()
