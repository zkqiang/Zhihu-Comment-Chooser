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

#### 运行示例
```
即将对评论用户进行抽奖，同一用户多次评论仅计入首次评论
抽奖文章: https://zhuanlan.zhihu.com/p/44170330
抽奖时间: 2018-09-19 13:22:58.381183
正在抓取评论列表，可能需要数分钟...
评论共计 300 条，有效评论用户 219 名
本次抽取 1 名获奖用户，中奖如下:
用户主页: https://www.zhihu.com/people/zhihubanquan | 昵称：知乎版权 | 评论页数：15 | 序号：10
```
