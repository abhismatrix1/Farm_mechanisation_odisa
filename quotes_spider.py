import scrapy
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_url = 'http://agrisnetodisha.ori.nic.in/FMNEW/CitizenView_Permit.aspx'
    download_delay = 1.5
    cookies = {'ASP.NET_SessionId': '45qklh555xzhek55hb4ceb45'}
    circles = []
    filled_circles = False

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse, cookies=self.cookies)

    def pop_circle(self):
        if len(self.circles) > 0:
            circle = self.circles[-1]
            #del self.circles[-1]
            return circle
        else:
            return None

    def parse(self, response):
       # if self.filled_circles==False:
            #print(response)
        #    self.circles = response.css('select#ctl00_ContentPlaceHolder1_ddlDao > option ::attr(value)').extract_first()
            #print(self.circles)
        #    self.filled_circles = True
       # circle = self.pop_circle()
      #  if circle != None:
            yield scrapy.FormRequest.from_response(
                response,
                formdata={
                    'ctl00$ContentPlaceHolder1$ddl_year': '2011-2012',
                    'ctl00$ContentPlaceHolder1$ddlDist': 'ANGUL',
                    'ctl00$ContentPlaceHolder1$ddlImpl': 'Tractor',
                   # 'txtDate':'01-Mar-2015',
                   # 'txtDateTo':'01-Mar-2016',
                    'ctl00$ContentPlaceHolder1$ddlDao': '0101'
                },
                dont_click=True,
                cookies=self.cookies,
                #callback=self.parse_results
            )

    def parse_tags(self, response):
        for tag in response.css('select#tag > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': response.css(
                        'select#author > option[selected] ::attr(value)'
                    ).extract_first(),
                    'tag': tag,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_results,
            )

    def parse_results(self, response):
        # print(response.css("table#cphBody_GridArrivalData > tr").extract())
        data = []
        key = response.css("span#cphBody_LabComName ::text").extract_first()
        # for tr in response.css("table#cphBody_GridArrivalData tr"):
        #     if len(tr.css('td')) > 0:
        #         data.append(tr.css('td span ::text').extract())
        last_row = response.css("table#cphBody_GridArrivalData tr")[-1]
        data.append(last_row.css('td span ::text').extract())
        yield {
            'key': key,
            'data': data
        }
        yield scrapy.Request(url=self.start_url, callback=self.parse, cookies=self.cookies)


