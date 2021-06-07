import pandas as pd

schools = pd.read_excel('data.xlsx',engine='openpyxl',sheet_name='Sheet1')

list1 = []
for i in range(0, len(schools), 5):
    list2 = []
    x = schools['SNo'][i]
    print(x)
    list2.append(x)
    for j in range(i,i+5):
        y = schools['Col2'][j]
        print(y)
        list2.append(y)
    for k in range(i,i+4):
        z = schools['Col3'][k]
        print(z)
        list2.append(z)
    list1.append(list2)
print(list1[30])