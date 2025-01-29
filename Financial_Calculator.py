import pandas as pd
import string
import os
import openpyxl
from decimal import Decimal


def calculate_percentage(income, bill):

  if income > bill:
    return Decimal((bill / income) * 100).quantize(Decimal('0.00')), 'profit'
  elif bill > income:
    return Decimal((income / bill) * 100).quantize(Decimal('0.00')), 'loss'
  else:
    return 0, 'profit'


def re(type, option, income):
  if type == "num":
    income=''
    while not income.isnumeric():
      income = input(f"Enter your {option}: ")
      if not income.isnumeric():
        print('Invalid Integer')
  elif type=="str":
    income='1'
    while income.isnumeric():
      income = input(f"Enter your {option}: ")
      if income.isnumeric():
        print('Invalid Integer')
  elif type == "spe_char":
    a='%'
    while 2>1:

      income = input(f"Enter your {option}:")
      if any(letter in list(string.punctuation) for letter in income):
        print(' No special Characters allowed.')
        continue
      break
  return income


def old_files():
  extensions = [".csv", ".xlsx"]

  files_list = os.listdir("Data_Files")

  files_with_ext = [
    file for file in files_list for ext in extensions if file.endswith(ext)
  ]

  if not files_with_ext:
    print("You don't have any files.")
    start()

  print('''
Which file do you want to show
1) Excel file
2) CSV file
3) Show all
4) Delete file
5) Back ''')
  a = re("num", "option", 1)
  if a == "1":
    extension = ".xlsx"
    xlsx_files = [file for file in files_list if file.endswith(extension)]
    if not xlsx_files:
      print("No xlsx files")
      old_files()

  elif a == "2":
    extension = ".csv"
    csv_files = [file for file in files_list if file.endswith(extension)]
    if not csv_files:
      print("No csv files")
      old_files()
  elif a == "3":
    extension = (".xlsx",".csv")
    all_files=[file for file in files_list if file.endswith(extension)]
    if not all_files:
      print("No files")
      old_files()
  elif a == "4":
    print('Files list:')
    for file in files_with_ext:
      print(file)
    removea = input("Name the file you want to delete: ")

    while 2 > 1:
      if os.path.exists("Data_Files/" + removea):
        os.remove("Data_Files/" + removea)
        print('The file has been removed')
        old_files()
      else:
        print("The file doesn't exist.")
        removea = input("Name the file you want to delete: ")
  elif a == "5":
    start()
  else:
    print('''Value error. Input out of range.''')
    old_files()
  print("File names: ")

  for file in files_list:
    if file.endswith(extension):
      print(file)

  list_files = input("Enter your file name with its extension: ")

  if list_files.endswith(".xlsx"):
    print(pd.read_excel(os.path.join("Data_Files", list_files)))
    start()
  elif list_files.endswith(".csv"):
    print(pd.read_csv(os.path.join("Data_Files", list_files)))
    start()
  else:
    print("File not found")
    old_files()


def start():
  print('''1) View old files
2) Create new file
3) Exit
 ''')
  ask = re("num", "options(1 or 2)", 1)
  if ask == "1":
    old_files()
  elif ask == "2":
    main()
  elif ask == "3":
    print('Thank you for using.')
    exit()
  else:
    print("Value error. Input out of range.")
    start()


def main():
  income = re("num", "income", 1)
  bill_items = re("str", "bill items",1).split(",")
  bill_amounts = []
  for item in bill_items:
    amount=int(re("num",f"amount for {item}",1))
    bill_amounts.append(amount)

  bill_data = []
  for item, amount in zip(bill_items, bill_amounts):
    percentage, prof = calculate_percentage(int(income), amount)
    if prof == 'profit':
      bill_data.append([
        item,
        amount,
        str(percentage) + '%',
      ])
    else:
      bill_data.append([item, amount, "-" + str(percentage) + '%'])
  df = pd.DataFrame(bill_data, columns=["Item", "Amount", "Percentage from Income"])
  print(df.head())
  if prof == 'profit':
    prof = int(income) - int(amount)
    profa = "Saving"
  else:
    profa = "Loss"
    prof = int(amount) - int(income)
  print(f'''Total Income: {income}
Total Bill:{sum(bill_amounts)}
Total {profa}:{prof}''')

  print('''
1) Save this file as xlsx
2) Save this file as csv
3) Don't save this file
''')
  ask = re("num", "options", 1)
  while ask != "1" and ask != "2" and ask != "3":
    ask = re("num", "options", 1)
  file_name = re("spe_char","file name",1)

  if ask == "1":
    file_type=".xlsx"
    file_path = os.path.join("Data_Files", file_name + file_type)
  elif ask == "2":
    file_type=".csv"
    file_path = os.path.join("Data_Files", file_name + file_type)

  else:
    start()
  while os.path.exists(file_path):
    overwrite = input(
      f"A file with the name {file_name} already exists. Do you want to overwrite it? (y/n): "
    )
    if overwrite.lower() == "y":
      df.to_csv(file_path, index=False)
      print(f"File {file_name} has been overwritten.")
      start()

    elif overwrite.lower() == "n":
      print("Please enter a different file name.")
      file_name = re("spe_char", "file name for the new file", file_name)
      file_path = os.path.join("Data_Files", file_name + file_type)
  if not os.path.exists(file_path):
    if file_type == ".csv":
      df.to_csv(file_path, index=False)
    else:
      df.to_excel(file_path, index=False)
  start()


if not os.path.exists('Data_Files'):
  os.makedirs('Data_Files')
start()
