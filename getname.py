import csv
import os
import pandas as pd
log_csv = pd.read_csv("/Users/wuxinying/PycharmProjects/GithubAPI/organization-out-2.csv", header=None) #log_csv_path为csv文件路径，header=None表示不要把csv文件的第一行作为列标题（csv数据中本来就没有列标题，第一行就是数据，所以这么设置）
print(log_csv.shape[0])
print(log_csv.shape[1])
for r in range(log_csv.shape[0]):  #log_csv.shape[0]为dataframe行数
    to_split = log_csv.iloc[[r], [4]].values[0][0]+'/0' #取出表格中第r行第c列的值得列表（因为dataframe中每个单元格是一个列表，数值在第一行第一列，所以[0][0]取之）
    temp_list = to_split.split('orgs/')   #to_split为字符串，用.split(":")把字符串以冒号为分界点分开为两个字符串，存储在一个列表temp_list中
    log_csv.iloc[[r],[4]] = temp_list[1]   #temp_list第2个值为所需的数值，取之赋给原表对应单元格，行列循环遍历后即可

log_csv.to_csv('/Users/wuxinying/PycharmProjects/GithubAPI/jian3.csv')
123
123
