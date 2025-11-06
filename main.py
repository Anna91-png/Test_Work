import argparse
import csv
import os
from csv_reporter.reports import average_rating
from tabulate import tabulate

REPORTS = {
    'average-rating': average_rating.generate
}

def read_data(files):
    rows = []
    for file in files:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows.extend(reader)
    return rows

def main():
    parser = argparse.ArgumentParser(description='Generate reports from CSV files.')
    parser.add_argument('--files', nargs='+', required=True, help='Paths to CSV files')
    parser.add_argument('--report', required=True, choices=REPORTS.keys(), help='Report type')
    args = parser.parse_args()

    if not all(os.path.exists(f) for f in args.files):
        print("❌ Один или несколько файлов не найдены.")
        return

    data = read_data(args.files)
    report_func = REPORTS[args.report]
    report = report_func(data)
    print(tabulate(report, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()

