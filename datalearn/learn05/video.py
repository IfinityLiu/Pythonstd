# -*- coding: utf-8 -*-

import sys
from you_get import common as you_get  # 写入you_get库

save_file=r'D:\videospider' # 设置下载目录

url = ''  # 需要下载视频的地址

# 爬取单个视频
sys.argv=['you-get','-o',save_file,url]


# 批量下载视频
# sys.argv=['you-get','-l',save_file,url]

you_get.main()