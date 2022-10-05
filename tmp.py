#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : AwesomeTang
# @File    : crawler.py
# @Version : Python 3.7
# @Time    : 2021-04-18 12:17

import requests
import re
import json
import pandas as pd

fundCode = 161725


class FundCrawler:
    def __init__(self,
                 fund_code: int,
                 page_range: int = None,
                 file_name=None):
        """
        :param fund_code:  基金代码
        :param page_range:  获取最大页码数，每页包含20天的数据
        """
        self.root_url = 'http://api.fund.eastmoney.com/f10/lsjz'
        self.fund_code = fund_code
        self.session = requests.session()
        self.page_range = page_range
        self.file_name = file_name if file_name else '{}.csv'.format(self.fund_code)
        self.headers = {
            'Host': 'api.fund.eastmoney.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % self.fund_code,
        }

    def fount_info(self):
        search_url = 'https://fundsuggest.eastmoney.com/FundSearch/api/FundSearchAPI.ashx'
        params = {
            "callback": "jQuery18309325043269513131_1618730779404",
            "m": 1,
            "key": self.fund_code,
        }
        res = self.session.get(search_url,
                               params=params
                               )
        try:
            content = self.content_formatter(res.text)
            fields = '，'.join([i['TTYPENAME'] for i in content['Datas'][0]['ZTJJInfo']])
            print("{:*^30}".format(self.fund_code))
            print("* 基金名称：{0:{1}>10} *".format(content['Datas'][0]['NAME'], chr(12288)))
            print("* 基金类型：{0:{1}>10} *".format(content['Datas'][0]['FundBaseInfo']['FTYPE'], chr(12288)))
            print("* 基金经理：{0:{1}>10} *".format(content['Datas'][0]['FundBaseInfo']['JJJL'], chr(12288)))
            print("* 相关领域：{0:{1}>10} *".format(fields, chr(12288)))
            print("*" * 30)
            return True
        except TypeError:
            print('Fail to pinpoint fund code, {}, please check.'.format(self.fund_code))

    @staticmethod
    def content_formatter(content):
        params = re.compile('jQuery.+?\((.*)\)')
        data = json.loads(params.findall(content)[0])
        return data

    def page_data(self,
                  page_index):
        params = {
            'callback': 'jQuery18308909743577296265_1618718938738',
            'fundCode': self.fund_code,
            'pageIndex': page_index,
            'pageSize': 20,
        }
        res = self.session.get(url=self.root_url, headers=self.headers, params=params)
        content = self.content_formatter(res.text)
        return content

    def page_iter(self):
        for page_index in range(self.page_range):
            item = self.page_data(page_index + 1)
            yield item

    def get_all(self):
        total_count = float('inf')
        page_index = 0
        while page_index * 20 <= total_count:
            item = self.page_data(page_index + 1)
            page_index += 1
            total_count = item['TotalCount']
            yield item

    def run(self):
        if self.fount_info():
            df = pd.DataFrame()
            if self.page_range:
                for data in self.page_iter():
                    df = df.append(data['Data']['LSJZList'], ignore_index=True)
                    print("\r{:*^30}".format(' DOWNLOADING '), end='')
            else:
                for data in self.get_all():
                    df = df.append(data['Data']['LSJZList'], ignore_index=True)
                    print("\r{:*^30}".format(' DOWNLOADING '), end='')
            df.to_csv(self.file_name)
            print("\r{:*^30}".format(' WORK DONE '))
            print("{:*^30}".format(' FILE NAME '))
            print("*{:^28}*".format(self.file_name))
            print("*" * 30)


if __name__ == "__main__":
    c = FundCrawler(fundCode)
    c.run()

'''运行日志
************320007************
* 基金名称：　　　　诺安成长混合 *
* 基金类型：　　　　　　　混合型 *
* 基金经理：　　　　　　　蔡嵩松 *
* 相关领域：　　　半导体，光刻胶 *
******************************
********* WORK DONE **********
********* FILE NAME **********
*         320007.csv         *
******************************
'''
