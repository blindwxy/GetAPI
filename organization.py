import requests
import json
import csv
import os
import pandas as pd
import time
log_csv = pd.read_csv("/Users/wuxinying/PycharmProjects/GithubAPI/API_org_name.csv", header=None) #log_csv_path为csv文件路径，header=None表示不要把csv文件的第一行作为列标题（csv数据中本来就没有列标题，第一行就是数据，所以这么设置）
print(log_csv.shape[0])
print(log_csv.shape[1])

def fetchUrl(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
    '''

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        'Authorization': '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',
        'Content-Type': 'application/json',
        'method': 'GET',
        'Accept': 'application/json'
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    result = json.loads(r.text)  # json字符串转换成字典

    return result

if __name__ == '__main__':
    '''
    主函数：程序入口
    '''
    with open('repo_API2.json', 'w') as f:
        for r in range(log_csv.shape[0]):
            conditions = log_csv.iloc[[r], [4]].values[0][0]
            query_url = 'https://api.github.com/orgs/'+conditions+'/repos'
            fetch_result = fetchUrl(query_url)
            json.dump(fetch_result, f)
            time.sleep(0.2)
            #print(fetch_result)
