from bs4 import BeautifulSoup
import requests
import os


def get_html(web_url):  # 爬虫获取网页
    '''获取每一部电影的信息'''
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    # 不加text返回的是response，加了返回的是字符串
    html = requests.get(url=web_url, headers=header).text
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('ol').find_all('li')  # 返回的信息最好只有需要的那部分，所以需要进行筛选
    return data


def get_info(all_movie):
    '''筛选出信息，保存进文本'''
    f = open("D:/pyobj/datalearn/learn05/douban.txt", 'a')

    for info in all_movie:
        '''排名'''
        nums = info.find('em')
        num = nums.get_text()
        '''名字'''
        names = info.find('span')  # 直接获取第一个span标签
        name = names.get_text()
        '''导演'''
        charactors = info.find('p')  # 此段信息需要替换符号
        charactor = charactors.get_text().replace(" ", "").replace("\n", "")  # 使信息排列规律
        charactor = charactor.replace("\xa0", "").replace("\xee", "").replace("\xf6", "").replace("\u0161", "").replace(
            "\xf4", "").replace("\xfb", "").replace("\u2027", "").replace("\xe5", "")
        '''评语'''
        remarks = info.find_all('sapan', {'class': 'inq'})
        if remarks:  # 判断电影是否有影评
            remark = remarks[0].get_text().replace('\u22ef', '')
        else:
            remark = '此影片么有影评'
        print(remark)
        '''评分'''
        scores = info.find_all('span', {'class': 'rating_num'})
        score = scores[0].get_text()

        # f.write(num + '、')
        f.write(name + '  ')
        f.write('评分: ' + score + ',  ')
        f.write(charactor + ',  ' + '\n')
        # f.write(remark + ',' + '\n')
        # f.write('\n')

    f.close()  # 关闭文件


if __name__ == "__main__":
    if os.path.exists('D:\\pyobj\\datalearn\\learn05') == False:  # 两个if来判断是否文件路径存在
        os.mkdir('D:\\pyobj\\datalearn\\learn05')
    if os.path.exists('D:\\pyobj\\datalearn\\learn05\\douban.txt') == True:
        os.remove('D:\\pyobj\\datalearn\\learn05\\douban.txt')

    page = 0  # 初始化页数
    while page <= 225:
        web_url = 'https://movie.douban.com/top250?start=%s&filter=' % page
        all_move = get_html(web_url)  # 返回每一页的网页
        get_info(all_move)  # 匹配对应信息存入本地
        page += 25
