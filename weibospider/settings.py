# -*- coding: utf-8 -*-

# Scrapy settings for weibospider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibospider'

SPIDER_MODULES = ['weibospider.spiders']
NEWSPIDER_MODULE = 'weibospider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'weibospider (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
#     'Connection': 'keep-alive',
#     'Host': 'm.weibo.cn',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibospider.middlewares.WeibospiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'weibospider.middlewares.ProxyMiddleware': 100,
    'weibospider.middlewares.RandomUserAgentMiddleware': 200,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapy_redis.pipelines.RedisPipeline': 299,  # 存储在redis刮项后处理
    'weibospider.pipelines.TimePipeline': 300,
    'weibospider.pipelines.WeiboPipeline': 301,
    'weibospider.pipelines.MongoPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MONGO_URI = 'localhost'

MONGO_DATABASE = 'weibo'

PROXY_URL = 'http://localhost:5555/random'

RETRY_HTTP_CODES = [401, 403, 408, 414, 500, 502, 503, 504]

RANDOM_UA_TYPE = 'random'

# 分布式爬虫设置
# Redis配置
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = '6379'
# # REDIS_PASSWORD = 'liutc1014'
# # REDIS_URL = 'redis://:@127.0.0.1:6379'
# # 使调度在redis存储请求队列
# SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# # SCHEDULER = 'scrapy_redis_bloomfilter.scheduler.Scheduler'
# # 确保所有的蜘蛛都共享相同的过滤器通过Redis复制
# DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# # DUPEFILTER_CLASS = 'scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter'
# # 散列函数的个数，默认为6，可以自行修改
# BLOOMFILTER_HASH_NUMBER = 6
# # Bloom Filter 的bit参数，默认30，占用128MB空间，去重两级1亿
# BLOOMFILTER_BIT = 30
# # 爬虫的请求调度算法，有三种可供选择
# # scrapy_redis.queue.SpiderQueue：队列。先入先出队列，先放入Redis的请求优先爬取；
# # scrapy_redis.queue.SpiderStack：栈。后放入Redis的请求会优先爬取；
# # scrapy_redis.queue.SpiderPriorityQueue：优先级队列。根据优先级算法计算哪个先爬哪个后爬
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# # 配置持久化
# SCHEDULER_PERSIST = True