
from questionSpider import questionSpider

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36\
                      (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Cookie': '_zap=cd52b570-3f65-4e66-8d90-302831164a1d; d_c0="AMBj4eRk-A-PTjj7C05LU7ZsCLfa5y8b6cg=|1567147484"; capsion_ticket="2|1:0|10:1567329482|14:capsion_ticket|44:MTYzOGJmMjlhYTc2NDRiMmE5MzYwNmZiZjY2MDc3NTI=|6dc5eaabf2e6bc2bc58ccbea19c2f864c78bd03c44a0d8e59abd32037234388e"; z_c0="2|1:0|10:1567329489|4:z_c0|92:Mi4xbFFXSEJnQUFBQUFBd0dQaDVHVDREeVlBQUFCZ0FsVk4wZHBZWGdBWDdKcUItTFBhajI2MWl4bUZLbk41dEdfNlJ3|cb47f200d7eb179429940dccd96c32d9b0e62d873f815a50ecdcce35f2077e32"; tst=h; tshl=; q_c1=dc2e4de9d98441e5bedc9a362469b35a|1567414785000|1567414785000; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _xsrf=NEq9JMDmRxDIz4L4xjJyv13bsLDGnUCz'
    }

for i in range(344671234, 344679999):

    path = "https://www.zhihu.com/question/%s" % i

    questionSpider.get_page_html(path, headers)
