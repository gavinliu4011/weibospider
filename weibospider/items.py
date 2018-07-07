# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    collection = 'users'

    id = Field()  # 微博ID
    name = Field()  # 微博名称
    avatar = Field()  # 微博头像
    cover = Field()  # 背景图
    gender = Field()  # 性别
    description = Field()  # 描述
    fans_count = Field()  # 粉丝量
    follows_count = Field()  # 关注
    weibos_count = Field()  # 微博数量
    verified = Field()  # 是否认证
    verified_reason = Field()  # 认证理由
    verified_type = Field()  # 认证类型
    follows = Field()
    fans = Field()
    crawled_at = Field()


class UserRelationItem(Item):
    collection = 'users'

    id = Field()
    follows = Field()
    fans = Field()


class WeiboItem(Item):
    collection = 'weibos'

    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()

