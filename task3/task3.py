import argparse
import json


def iterate_nested_list(nested_values_list, test_id, test_value):
    for item in nested_values_list:
        for item_key, item_value in item.items():
            report_dict[item_key] = item_value
        if item['id'] == test_id:
            item['value'] = test_value
            report_dict[item['id']] = item['value']
        if 'values' in item.keys() and isinstance(item['values'], list):
            iterate_nested_list(item['values'], test_id, test_value)
    return report_dict


parser = argparse.ArgumentParser(description='task3, forming json')
parser.add_argument('tests', help='путь до tests.json', type=argparse.FileType('r', encoding='UTF-8'))
parser.add_argument('values', help='путь до values.json', type=argparse.FileType('r', encoding='UTF-8'))
parser.add_argument('report', help='путь до report.json', type=argparse.FileType('w', encoding='UTF-8'))

args = parser.parse_args()

tests_dict = json.load(args.tests)
values_dict = json.load(args.values)
report_dict = tests_dict
result = {}

for values_list in values_dict['values']:
    result = iterate_nested_list(tests_dict['tests'], values_list['id'], values_list['value'])
json.dump(result, args.report)
