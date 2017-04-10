import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_url = 'http://agmarknet.gov.in/'
    download_delay = 1.5
    cookies = {'ASP.NET_SessionId': 't3vci5diwp3rjatcuqlyxzwl'}
    states = []
    filled_states = False

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse, cookies=self.cookies)

    def pop_state(self):
        if len(self.states) > 0:
            state = self.states[-1]
            del self.states[-1]
            return state
        else:
            return None

    def parse(self, response):
        if self.filled_states==False:
            self.states = response.css('select#ddlState > option ::attr(value)').extract()
            self.filled_states = True
        state = self.pop_state()
        if state != None:
            yield scrapy.FormRequest.from_response(
                response,
                formdata={
                    'ddlArrivalPrice': '0',
                    'ddlCommodity': 'Pomegranate',
                    'txtDate':'01-Mar-2015',
                    'txtDateTo':'01-Mar-2016',
                    'ddlState': state
                },
                cookies=self.cookies,
                callback=self.parse_results
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