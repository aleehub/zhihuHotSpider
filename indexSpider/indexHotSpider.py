# 知乎热门话题首页信息分析
# 利用xpath解析文档内容

import requests
from lxml import etree


def get_page_html(url, headers):
    """
    获取首页热门话题
    :param url: 知乎热门话题路径
    :param headers: 请求头，包含用户身份，cookies等信息
    :return: 返回一个热门问题：排名，问题，链接，热度列表
    """

    # 获取响应对象
    response = requests.get(url, headers=headers)

    # 定义存储路径
    path = "../data/hot.html"

    # 调用写入方法将爬取网页存储到本地
    write_to_html(path, response)
    # 生成xpath解析对象
    content = etree.HTML(response.text)

    # 在打印有etree生成的字符串时，中文会变成数字格式，此时可以用
    # print(html.unescape(etree.tostring(content).decode('utf-8')))

    # 排名
    rank = content.xpath("//div[contains(@class,'HotItem-rank')]/text()")
    # 标题
    title = content.xpath("//h2[contains(@class,'HotItem-title')]/text()")
    # 链接
    link = content.xpath("//div[contains(@class,'HotItem-content')]/a/@href")
    # 热度
    hot = content.xpath("//div[contains(@class,'HotItem-metrics')]/text()")

    # print(rank)
    # print(title)
    # print(link)
    # print(hot)

    hot_list = []

    for i in range(len(rank)):

        hot_list.append({
            "rank": rank[i],
            "title": title[i],
            "link": link[i],
            "hot": hot[i]
        })

    return hot_list


def write_to_txt(path, hot_list):
    """
    写入到文本
    :param path:  保存文本路径
    :param hot_list: 保存列表
    :return:
    """

    with open(path, "a", encoding="utf-8") as f:

        for i in hot_list:

            f.writelines(str(i)+"\n")


def write_to_html(path, response):

    with open(path, "wb") as f:

        f.write(response.content)


def main():
    """

    :return: 返回一个热门问题的链接
    """


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
                      (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Cookie': '_zap=cd52b570-3f65-4e66-8d90-302831164a1d; d_c0="AMBj4eRk-A-PTjj7C05LU7ZsCLfa5y8b6cg=|1567147484"; capsion_ticket="2|1:0|10:1567329482|14:capsion_ticket|44:MTYzOGJmMjlhYTc2NDRiMmE5MzYwNmZiZjY2MDc3NTI=|6dc5eaabf2e6bc2bc58ccbea19c2f864c78bd03c44a0d8e59abd32037234388e"; z_c0="2|1:0|10:1567329489|4:z_c0|92:Mi4xbFFXSEJnQUFBQUFBd0dQaDVHVDREeVlBQUFCZ0FsVk4wZHBZWGdBWDdKcUItTFBhajI2MWl4bUZLbk41dEdfNlJ3|cb47f200d7eb179429940dccd96c32d9b0e62d873f815a50ecdcce35f2077e32"; tst=h; tshl=; q_c1=dc2e4de9d98441e5bedc9a362469b35a|1567414785000|1567414785000; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _xsrf=NEq9JMDmRxDIz4L4xjJyv13bsLDGnUCz'
    }

    url = "https://www.zhihu.com/hot"

    path = "../data/indexinfo.txt"

    result = get_page_html(url, headers)

    write_to_txt(path, result)

    questionList =[]

    for i in result:
       questionList.append(i["link"])

    return questionList
