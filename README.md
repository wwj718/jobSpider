#jobSpider

jobSpider是一只scrapy爬虫，用于爬取职位信息

目前收录：

*  [拉勾网](https://www.lagou.com)


# 功能
1. 爬取Lagou网的职位信息(爬取最新的5000条)



# 安装与依赖
*  git clone https://github.com/wwj718/jobSpider
*  cd jobSpider
*  pip install -r requirements.txt
*  mongodb(可选)
*  在setting.py中修改csv保存的路径（FEED_URI变量）,默认是当前目录
*  运行 ： scrapy crawl LagouSpider（开始爬取数据）


# 我的开发环境
OSX python2.7

在windows7下测试可用

### 可选特性

如果要使用mongodb数据库，取消setting.py中的ITEM_PIPELINES注释

#  代码风格
采用[yapf](https://github.com/google/yapf)来统一代码风格

`yapf -i filename.py`

