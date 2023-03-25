import requests
import json


# 获取指定接口的数据
def fetchUrl(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：目标网页的 url
    返回：目标网页的 html 内容
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0',
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

    conditions = 'Traceableai'
    query_url = 'https://api.github.com/orgs/'+conditions+'/repos'

    fetch_result = fetchUrl(query_url)

    print(fetch_result)

123
