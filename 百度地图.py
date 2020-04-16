'''
http://api.map.baidu.com/place/v2/search?q=%E9%A5%AD%E5%BA%97&page_size=10&page_num=5&region=%E9%87%8D%E5%BA%86%E6%B8%9D%E5%8C%97%E5%8C%BA&output=json&ak=你的ak值
http://api.map.baidu.com/place/v2/search?q=饭店&page_size=10&page_num=5&region=重庆渝北区&output=json&ak=你的ak值
q查询的内容经过了编码
page_size返回多少条数据
page_num页数编码
region地区经过了编码的
ak需要到http://lbsyun.baidu.com/apiconsole/key#/home注册获取ak值
'''

import requests
import pprint
import csv

class Baiduditu():

    def nextpage(self):
        self.api_url=[]
        for i in range(1,5):   #自定义页数
            api_url = 'http://api.map.baidu.com/place/v2/search?q=%E9%A5%AD%E5%BA%97&page_size=10&page_num={}&region=%E9%87%8D%E5%BA%86%E6%B8%9D%E5%8C%97%E5%8C%BA&output=json&ak=你的ak值'.format(i)
            self.api_url.append(api_url)

    def pasring(self):
        for url in self.api_url:
            print(url)
            response=requests.get(url)
            pprint.pprint(response.json())
            results=response.json()['results']
            # print(results)
            for result in results:
                nama=result['name']
                address=result['address']
                try:
                    phone = result['telephone']
                except:
                    phone='XXXXXXX'
                print(nama,phone,address)
                writer.writerow((nama,phone,address))





if __name__ == '__main__':
    fp = open('百度地图.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('名字', '电话', '地址'))
    baidu=Baiduditu()
    baidu.nextpage()
    baidu.pasring()