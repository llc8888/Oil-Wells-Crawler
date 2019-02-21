import scrapy
import numpy as np
import urllib
import requests
import scrapy
import lxml
import json
from bs4 import BeautifulSoup
import re
from lxml import etree
from datetime import datetime
from wells.items import WellsItem

class WellSearchSpider(scrapy.Spider):
    name = 'well_spider'
    allowed_domains =['secure.conservation.ca.gov']
    start_urls = ['https://secure.conservation.ca.gov/WellSearch/Details?api='+'00100001'+'&District=&County=&Field=&Operator=&Lease=&APINum=&address=&ActiveWell=false&ActiveOp=true&Location=&sec=&twn=&rge=&bm=&PgStart=0&PgLength=10&SortCol=6&SortDir=asc&Command=Search#prodCharts' ]

    custom_settings = {'LOG_ERROR':"ERROR"}
    def parse(self,response):
        soup = BeautifulSoup(response.body, "lxml")
        api_array = np.load('./spiders/api_list.npz')['arr_0']

        for i in range(1,len(api_array)):
            urls = 'https://secure.conservation.ca.gov/WellSearch/Details?api='+api_array[i]+'&District=&County=&Field=&Operator=&Lease=&APINum=&address=&ActiveWell=false&ActiveOp=true&Location=&sec=&twn=&rge=&bm=&PgStart=0&PgLength=10&SortCol=6&SortDir=asc&Command=Search#prodCharts'
            yield scrapy.Request(urls, callback=self.extract_wells_info)

    def soup_details(self,response):
        soup = BeautifulSoup(response, "lxml")
        wells_info = self.extract_wells_info(soup)

        print(wells_info)

    def extract_wells_info(self,response):
        well_api = response.xpath('//div[@class="col-sm-2"]/span[@id="wellAPI"]/text()').get()
        country_name = response.xpath('//div[@class="col-sm-2"]/text()[preceding-sibling::br and following-sibling::span]')[1].get().strip()
        lease_name = response.xpath('//div[@class="col-sm-3"]/text()[preceding-sibling::label[@for="WellInfo_LeaseName"]]')[1].get().strip()
        operator = response.xpath('//div[@class="col-sm-5"]/text()[preceding-sibling::label[@for="WellInfo_OperatorName"]]')[1].get().strip()
        well_status = response.xpath('//div[@class="col-sm-2"]/text()[preceding-sibling::label[@for="WellInfo_WellStatusCode"]]')[0].get().strip()
        spud_date = response.xpath('//div[@class="col-sm-1"]/text()[preceding-sibling::label[@for="WellInfo_SPUDDate"]]')[1].get().strip()
        latitude = response.xpath('//div[@class="col-sm-1"]/text()[preceding-sibling::label[@for="WellInfo_Latitude"]]')[1].get().strip()
        longitude = response.xpath('//div[@class="col-sm-2"]/text()[preceding-sibling::label[@for="WellInfo_Longitude"]]')[1].get().strip()
        regex = '\[\"[0-9]{4}\",\"[0-9]+\",\"[0-9]+\",\"[0-9]+\"\]'
        production_table = re.findall(regex, response.body.decode('utf-8'))
        print(response.url)
        item = WellsItem(well_api=well_api,country_name=country_name, production_table=production_table,\
                         well_status=well_status,lease_name=lease_name,operator=operator,\
                         spud_date=spud_date,latitude=latitude, longitude=longitude)
        yield item
