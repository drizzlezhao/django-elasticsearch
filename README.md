# django-elasticsearch
A Django + elasticsearch project    
# 实现功能  
模仿思否的搜索功能实现对文章进行关键字检索  
关键字在前端页面中高亮显示  
# 使用步骤
请在elasticsearch安装目录下的plugins文件夹下放IK分词器  
运行utils目录下create_elastic_index.py文件创建elasticsearch的mappings    
运行utils目录下spider.py文件获取基本数据  
# 数据库字符编码问题
如果使用示例爬虫spider.py获取数据  
需要将数据库Blog表的title和content字段编码改为utf8mb4
