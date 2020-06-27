"""
作业一：

安装并使用 requests、bs4 库
爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
并以 UTF-8 字符集保存到 csv 格式的文件中。

猫眼电影网址： https://maoyan.com/films?showType=3

"""


import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd



user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
myurl = 'https://maoyan.com/films?showType=3'
Cookies = r'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593264008; _lxsdk_cuid=172f5ef6acac8-08b213c8840e8c-31627403-2a3000-172f5ef6acac8; __mta=208049453.1593264008262.1593264008262.1593264071703.2; uuid_n_v=v1; iuuid=D5926540B87F11EAB41CF9A19F46288FA87296E348824AB7800638D39F990381; webp=true; ci=30%2C%E6%B7%B1%E5%9C%B3; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172f61cbd46383-082d9923d10daf-73236134-708324-172f61cbd47684%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172f61cbd46383-082d9923d10daf-73236134-708324-172f61cbd47684%22%7D; _last_page=c_dmLad; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593266979; _lxsdk=D5926540B87F11EAB41CF9A19F46288FA87296E348824AB7800638D39F990381; __mta=208049453.1593264008262.1593264071703.1593266980036.3; _lxsdk_s=172f61cb6f8-88a-cd0-70e%7C%7C4'

header = {'user-agent':user_agent,'Cookie':Cookies}
response = requests.get(myurl,headers=header)
bs_info = bs(response.text,'html.parser')
# print(bs_info)
# /html/body/div[2]/section[2]/div[4]/div[2]/div/div/div[1]/div
# movie1 = pd.DataFrame(data = mylist)
movies_info = {'title':[], 'type':[], 'date':[]}
for tags in bs_info.find_all('div',attrs={'class':'classic-movies'}):
    sleep(1)

    for atag in tags.find_all('a'):
        sleep(1)
        title = atag.find('div',attrs={'class':'title line-ellipsis'}).get_text()
        Mtype = atag.find('div',attrs={'class':'actors line-ellipsis'}).get_text()
        date = atag.find('div',attrs={'class':'show-info line-ellipsis'}).get_text()
        movies_info['title'].append(title)
        movies_info['type'].append(Mtype)
        movies_info['date'].append(date)


ten_movies = pd.DataFrame(movies_info)
ten_movies.to_csv('./ten_movies.csv', encoding='UTF-8', index= False, header= False )
# selector = lxml.etree.HTML(atag.text)
# film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
# print(f'电影名称: {film_name}')