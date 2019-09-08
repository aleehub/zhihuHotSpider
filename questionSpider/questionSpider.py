import html
import re
import requests
from lxml import etree


def get_page_html(url, headers):

    # 获取响应对象
    response = requests.get(url, headers=headers)

    if response.status_code == requests.codes.ok:

        content = etree.HTML(response.text)

        # path = "../data/question/1.html"

        # 调用写入方法将爬取网页存储到本地
        # write_to_html(path, response)

        # 在打印有etree生成的字符串时，中文会变成数字格式，此时可以用
        # print(html.unescape(etree.tostring(content).decode('utf-8')))

        # 问题信息
        questionInfo = content.xpath("//main[@class='App-main']/div[@class='QuestionPage']/meta/@content")
        # 问题细节
        questionDetail = content.xpath("//div[@class='QuestionHeader-detail']//span[contains(@class,'RichText')]/text()")
        # 回答列表
        answerele = content.xpath("//div[@class='List-item']//span[contains(@class,'RichText')]")
        answerList = []

        for item in answerele:
            answer = html.unescape(etree.tostring(item).decode('utf-8'))
            # print(type(answer))
            pattern = re.compile('<.*?>', re.S)
            answersub = re.sub(pattern, "", answer)

            # print(answersub)
            answerList.append(answersub)

        dic = {
            "title": questionInfo[0],
            "url": questionInfo[1],
            "about": questionInfo[2],
            "answerCount": questionInfo[3],
            "commentCount": questionInfo[4],
            "dateCreated": questionInfo[5],
            "dateModified": questionInfo[6],
            "zhihu:followerCount": questionInfo[7],

        }
        try:
            path = "F:\\data\\%s.txt" % questionInfo[0]

            # path = "../data/answer/%s.txt"

            write_to_txt(path, str(dic))
            write_to_txt(path, str(questionDetail))
            write_to_txt(path, str(answerList))

        except OSError:

            print('OSError:', questionInfo[0], questionInfo[1])

            return

        else:

            print("已完成:", questionInfo[0])



    else:
        print('失败：无效链接')
        return


def write_to_html(path, response):

    with open(path, "wb") as f:

        f.write(response.content)


def write_to_txt(path, result):

    with open(path, "a", encoding='utf-8') as f:

        f.write(result+"\n\n\n")




