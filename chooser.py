# -*- coding: utf-8 -*-

__author__ = 'zkqiang'
__zhihu__ = 'https://www.zhihu.com/people/z-kqiang'
__github__ = 'https://github.com/zkqiang/Zhihu-Comment-Chooser'

import requests
import json
import re
import time
import random

# 抽奖的文章
ARTICLE_URL = 'https://zhuanlan.zhihu.com/p/44665180'

# 抽奖总数
CHOICE_TOTAL = 6

# 不参与抽奖的用户主页
BLACK_LIST = ['https://www.zhihu.com/people/zhihuadmin']


def get_comments(article_url):
    """
    请求 API 获取所有评论数据
    """
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'origin': 'https://www.zhihu.com',
        'referer': article_url,
    }

    params = {
        'include': 'data[*].author,collapsed,reply_to_author,disliked,'
                   'content,voting,vote_count,is_parent_author,is_author,algorithm_right',
        'order': 'normal',
        'limit': 20,
        'offset': 0,
        'status': 'open'
    }

    code = re.findall(r'/(\d{4,})$', article_url)[0]
    api_url = 'https://www.zhihu.com/api/v4/articles/{}/comments'.format(code)
    comments = list()
    while True:
        resp = requests.get(api_url, params=params, headers=headers)
        resp.encoding = 'utf-8'
        resp_data = json.loads(resp.text)
        if resp_data['paging']['is_end'] is True:
            break
        comment_page = resp_data['data']
        comments.extend(comment_page)
        params['offset'] += 20
        time.sleep(1)
    return comments


def parse_authors(comments):
    """
    解析评论数据，返回评论用户列表
    """
    authors = list()
    url_tokens = set()
    for idx, cm in enumerate(comments):
        # 跳过精彩评论
        if cm['featured'] is True:
            continue
        url_token = cm['author']['member']['url_token']
        # 跳过重复的评论用户
        if url_token in url_tokens:
            continue
        user_url = 'https://www.zhihu.com/people/' + url_token
        # 跳过黑名单用户
        is_black = False
        for black in BLACK_LIST:
            if black in user_url:
                is_black = True
                break
        if is_black is True:
            continue
        author = {
            # 用户主页
            'user_url': user_url,
            # 用户昵称
            'name': cm['author']['member']['name'],
            # 评论所在页数
            'page': idx // 20 + 1,
            # 评论在页数里的顺序(精彩评论也计入顺序)
            'order': idx % 20 + 1,
        }
        authors.append(author)
        url_tokens.add(url_token)
    return authors


def choice(chosen, num):
    """
    从列表里随机抽取若干个对象
    """
    return random.sample(chosen, num)


def run():
    print('即将对评论用户进行抽奖，同一用户多次评论仅计入首次评论')
    print('抽奖文章:', ARTICLE_URL)
    from datetime import datetime
    print('抽奖时间:', datetime.now())
    print('正在抓取评论列表，可能需要数分钟...')
    comments = get_comments(ARTICLE_URL)
    authors = parse_authors(comments)
    print('评论共计 {} 条，有效评论用户 {} 名'.format(
        len(comments), len(authors))
    )
    res = choice(authors, CHOICE_TOTAL)
    print('本次抽取 {} 名获奖用户，中奖如下:'.format(CHOICE_TOTAL))
    for r in res:
        print('用户主页: {} | 昵称：{} | 评论页数：{} | 页内序号：{}'.format(
            r['user_url'], r['name'], r['page'], r['order']
        ))


if __name__ == '__main__':
    run()
