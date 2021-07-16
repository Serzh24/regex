from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def updating_phone_numbers(list_list, regular, new):
    pattern = re.compile(regular)
    final = [[pattern.sub(new, string) for string in list_] for list_ in list_list]
    return final

def name_correction(list_list):
    result = [' '.join(employee[0:3]).split(' ')[0:3] + employee[3:7] for employee in list_list]
    return result

def remove_duplicates(correct_name_list):
    new_list = []
    for compared in correct_name_list:
        for employee in correct_name_list:
            if compared[0:2] == employee[0:2]:
                list_employee = compared
                compared = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        compared.append(employee[i])
                    else:
                        compared.append(list_employee[i])
        if compared not in new_list:
            new_list.append(compared)
    return new_list


correct_name_list = (name_correction(contacts_list))
correct_num_list = updating_phone_numbers(correct_name_list, r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})', r'+7(\2)\3-\4-\5')
correct_num_additional_list = updating_phone_numbers(correct_num_list, r'\(?доб.\s(\d{4})\)?', r'доб.\1')
correct_list = remove_duplicates(correct_num_additional_list)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(correct_list)