import pandas as pd

school = pd.read_excel('data.xlsx',sheet_name='Sheet1', engine = 'openpyxl')
print(school.columns)

list1 = []

for i in range(0, len(school), 5):
    list2 = []
    a = school['SNo'][i]
    # print(a)
    list2.append(a)
    for j in range(i, i+5):
        b = school['Col2'][j]
        # print(b)
        list2.append(b)
    for j in range(i, i+4):
        c = school['Col3'][j]
        # print(c)
        list2.append(c)
    list1.append(list2)

# print('------------------------------output--------------------------------')
# print(list1[2])

second = []


senior = []


middle = []


for k in range(len(list1)):
    ss = list1[k][4][21:]
    i = list1[k][0]
    if ss == 'Secondary School':
        s = list1[k]
        second.append(s)
    elif ss == 'Senior Secondary':
        se = list1[k]
        senior.append(se)
    elif ss == 'Middle Class':
        m = list1[k]
        middle.append(m)

print('Senior secondary length is',len(senior))
print('Secondary length is ',len(second))
print('Middle class length is ',len(middle))
print('----------------------')
print('Overall length is',len(senior)+len(second)+len(middle))

# print(second[0])

count = 1
id_middle = []
data_middle = []
for x in middle:
    x.pop(0)
    id_middle.append(count)
    for i in range(8):
        id_middle.append("")  #[1, , , , , , , , , , 2]
    for y in x:
        data_middle.append(y)
    count = count+1

count = 1
id_second = []
data_second = []
for a in second:
    a.pop(0)
    id_second.append(count)
    for i in range(8):
        id_second.append("")
    for j in a:
        data_second.append(j)
    count=count+1

count = 1
id_senior = []
data_senior = []
for x in senior:
    x.pop(0)
    id_senior.append(count)
    for y in range(8):
        id_senior.append("")
    for z in x:
        data_senior.append(z)
    count = count+1



def write():
    # senior school
    df = pd.DataFrame({
        'SNo' : id_senior,
        'Senior' : data_senior
    })
    writer = pd.ExcelWriter('EXCEL/SeniorSchool.xlsx',engine = 'xlsxwriter')
    df.to_excel(writer,sheet_name='Sheet3',index=False)
    writer.save()

    # secondary school
    df = pd.DataFrame({
        'SNo' : id_second,
        'Secondary_Data' : data_second
    })
    writer = pd.ExcelWriter('EXCEL/SecondarySchool.xlsx',engine = 'xlsxwriter')
    df.to_excel(writer,sheet_name='Sheet4',index=False)
    writer.save()

    # middle class
    df = pd.DataFrame({
        'SNo' : id_middle,
        'Middle_Data' : data_middle
    })
    writer = pd.ExcelWriter('EXCEL/MiddleSchool.xlsx',engine = 'xlsxwriter')
    df.to_excel(writer,sheet_name='Sheet5',index=False)
    writer.save()

write()
