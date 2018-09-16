# 知乎评论抽奖器

#### 功能简介
对知乎专栏文章中参与评论的用户进行抽奖，同一用户多次评论仅计入首次评论

#### 使用方法
修改 chooser.py 开头的常量，直接 run() 即可

`ARTICLE_URL` 抽奖文章的链接，如：`https://zhuanlan.zhihu.com/p/44170330`

`CHOICE_TOTAL` 抽奖个数

`BLACK_LIST` 不参与抽奖的用户，需要是点头像后的用户主页，如：
`['https://www.zhihu.com/people/zhihuadmin']` 或
`['zhihuadmin']`

运行后最终会打印结果：
```
# 首先是请求 API 后的 Response
...

有效评论用户：
[ { 
    # 用户主页
    'user_url': 'https://www.zhihu.com/people/zhihuadmin',
    # 评论所在页数
    'page': 1,
    # 评论在页数里的次序(如果有精彩评论，也会计入次序，但不会计入抽奖)
    'order': 1,
  },
    ...
]

中奖用户:
[
    ...
]
```
