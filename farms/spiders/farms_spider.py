import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.selector import Selector

class FarmsSpider(scrapy.Spider):
    name = 'farms'
    start_url = 'http://agrisnetodisha.ori.nic.in/FMNEW/CitizenView_Permit.aspx'
    download_delay = 1.5
    cookies = {'ASP.NET_SessionId': '45qklh555xzhek55hb4ceb45'}
    years = []
    implements=[]
    districts=[]
    circles=[]
    filled_years = False
    fw = open('rough', 'w')

    def start_requests(self):

        yield scrapy.Request(url=self.start_url, callback=self.parse_year, cookies=self.cookies)


    def pop_circle(self):
        if len(self.circles) > 0:
            circle = self.circles[-1]
            del self.circles[-1]
            #print(circle)
            return circle
        else:
            return None

    def pop_district(self):
        if len(self.districts) > 0:
            district = self.districts[-1]
            del self.districts[-1]
            #print(district)
            return district
        else:
            return None

    def pop_implement(self):
        if len(self.implements) > 0:
            implement = self.implements[-1]
            del self.implements[-1]
            #print(implement)
            return implement
        else:
            return None

    def pop_year(self):
        if len(self.years) > 0:
            year = self.years[-1]
            del self.years[-1]
            #print(year)
            return year
        else:
            return None

    def parse_year(self, response):
        #if self.filled_years==False:
            self.years = response.css('select#ctl00_ContentPlaceHolder1_ddl_year > option ::attr(value)').extract()[1:]
            #self.filled_years=True

            self.year = self.pop_year()
            #while self.year != None:
                #print(self.year)

            self.year = '2011-2012'
            return scrapy.FormRequest(url=self.start_url,
                                   formdata={
                                       'ctl00$ScriptMain': 'ctl00$ContentPlaceHolder1$Upd | ctl00$ContentPlaceHolder1$ddl_year',
                                       '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ddl_year',
                                       '__EVENTARGUMENT': '',
                                       '__LASTFOCUS': '',
                                       '__VIEWSTATE':response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                                           #'1ZVpYqS8qHEBjnVwNEc4raHA+CH0uOj8tCfXiGTTpZlrw / 8sHiSB4JpmPMa0U2MJHipFRAtdJ / mufYHeekL1c / EQa / 9qxS5BEi4t4xRO9o46PbXNHuOYoQGb1IVazzJ25E69xx6 / ILi7xsILq3a6kbrsGNtvEDXoQrbijW0P6Miu / PiSx9Z6dGxOp8eRcEvvJffIWDjVbd93YkQuqTFFOfQl0Nelwu9LRnDAhifKgG5pKi + Kzg3evVs31MguJ51 / fASOYh8OLdg1uPMJlB / 5f770dHz4XgQvYMp1AhOny8JlYyW09ThxBVQxbQ8h / AHUYe51bZupevsV9FZYZdb4lYu6zNXBkWOFVjaH / bh0cQlAKI0VB0W6Xpal3tN1BirDO7o7fy2LIcTIzJWRLp3 + wZbe7ncT2LbBDlX8KoiLlXmTeuJZtxF0fJ69LegYpnge2KI7xeT + lMmOSpFxDswBfczPOmJ9UgtApUzVGwqzDzAd75SfNHaGGuolyYXUlZnyVnzm25D2JWddI3ceUXU79Q28PsH8jd1lQlY / fyTmhdCQP45qFeuwO89U7lt + 1TKdvNdMJI2p1i3JzP5bgXjJdgkJ / ZBUpkhEOzOkWsBCF / XFBmW3qOWpdV4u7LGWVwauX7O6UPTK7MNnRzP53ncGe4RWury + xCVw3re / 6TTgbDNdD5PKlp9fv5Lbr1IHrGhZX + CEF7AuGowzHeOWbkDhhfRsd1QJhbwlqqqNJro2V / JXl / OD + EPcJ509WGuEA3sTEAudkvIYY7XHmEtg4ATVVg1uVpHxRfO8nWWcnB76lmlS + tI6CLAi7lz0xy4iukNrFvVjfcaDSNqtBaQZFcPRtOkEBVR + n + P0JLrnZQFtEOGXFcCEZY2XRYHokXn9jDZ6GJxpj4JKh3IPcUHoIVcUJvhJgINH2I6LvphyifllqZIoZX3zF123 / 0f9LYWRrhlJlXZLko8CjXmjicysEjbbhVFf0yg9bmFKQIno5rA5Mxb66jle / Rc1LznsMuD / pHcogHm + jZfY769gfTF8VAOIWH2J + 4 + eBzhLtxWWB + WibemEs + qszpYgouxghTo8 / KcfOdfwN8CelOcB1OzM5Ef0gs7456F4kJtTLfT + uxt1EroCC97yATnELbbjEkYdWK / NPR / sNQ + YBTLKVB2oqGH / lAIGbEKyLzo8vhh / HnqtBo71ExAU1Jc0RSIFHxBAE2aRzoqIH + AmB / ZILn9gvChkICPGT1VSSWJiqZQbnXKv3g / jyB4VwRFM4RVb43SPUsX729QiWRJx9YSvMJUIcqdDeLgINiurKjzfP8rvI / nZHiGFgHU8Zeq + 7klCo4Lodpjty5lZWGW9LJrq4XRYrITWFcrUZb + ThbGGZe1t + YngDzNp552b6GY35ZRAzfyY7SCnHyLDeimyF98PQow6fFRPRQ9Oo7444qf6xVL21TUj + FZXwiogvo7pvbk8q82KKrPmAPV / B / LRRlEyX2Eqpze + B9Hha6E0Ddn12qPlLKzGoYGeA + xgqjp5 + sjYF2w9EsMhpQhfw + QzQMq2EFLv + f15G7NphJtT + k0Kmrx8k6dHsHu8Vuc8pFJE + HAvywzyAftB3TWZkA ==',
                                       '__VIEWSTATEGENERATOR': 'CD4DDF2D',
                                       '__VIEWSTATEENCRYPTED': '',
                                       '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                                           #'3ydVi + tKhNiPOmP7pqgfaOu3G8INC + 7pzHL3h72DTjQk7zPdkNDPb7TfYA916zn6rOpL64X9cAuXgGOUTm2R1pm8v3EAnVwbD6UAAb9Hghv2uSsiZYUbyQiqR47l5 + RgTDArwGycQrNFCJjYxZSpHbYGYf1RWYaGD7UggoZadqC8EVllEVtGuobz + 5GBU3Uafz + bSsH6OMNO2zDKXTBPgG25PMx4xRTKx4QiTQxRYYM + zy9MOVJeQZhHgNaP8GmLs2 + YFXmP4AAQ8a2Osv6UxCVvmnskRDEmfOcisqBW8F7TRk0HIZgSy / bAq5XWO3WvAadSv4pYK40cM4LvCp2yLw2j0N1GHointt9HitLR6jWNka / bTXn49IJDX8gIJ + Jq + cjITlV2g2fQO5 + S + Fad1q977utd / eyoQPHlfnKdFerdknj + h2wB / ppoWGV86 + QnAnvkilX5jRy6q51CVGLHgwCtiaad962Z6E / BBBFa2etFVDtjfhYkwpYQ8yymOvbnyPnsJZ6U7z0pOzQRIT / TRs8f9ELL2ER + QM + Rdcn14T0GLa81TTypZWeT5voTbBNqaJg3iA ==',
                                       'ctl00$ContentPlaceHolder1$ddl_year': self.year,
                                       'ctl00$ContentPlaceHolder1$ddlImpl': 'Select Implement',
                                       'ctl00$ContentPlaceHolder1$ddlDist': 'Select',
                                       'ctl00$ContentPlaceHolder1$ddlDao': 'Select',
                                   },
                                    cookies=self.cookies,
                                    callback=self.parse_implement
                                   )





    def parse_implement(self,response):

        self.implements=response.css('select#ctl00_ContentPlaceHolder1_ddlImpl > option ::attr(value)').extract()[1:]
        self.year = response.css('select#ctl00_ContentPlaceHolder1_ddl_year > option[selected] ::attr(value)').extract_first()
        #self.fw.write(self.year + ' ' + ' ' + '\n')
        print(self.year,self.implements)

        self.implement = self.pop_implement()
        #while self.implement != None:
        self.implement = '1'
        print(self.implement)
        yield scrapy.FormRequest(url=self.start_url,
                                     formdata={
                                         'ctl00$ScriptMain': 'ctl00$ContentPlaceHolder1$Upd | ctl00$ContentPlaceHolder1$ddlImpl',
                                         '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ddlImpl',
                                         '__EVENTARGUMENT': '',
                                         '__LASTFOCUS': '',
                                         '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                                             #'1ZVpYqS8qHEBjnVwNEc4raHA+CH0uOj8tCfXiGTTpZlrw / 8sHiSB4JpmPMa0U2MJHipFRAtdJ / mufYHeekL1c / EQa / 9qxS5BEi4t4xRO9o46PbXNHuOYoQGb1IVazzJ25E69xx6 / ILi7xsILq3a6kbrsGNtvEDXoQrbijW0P6Miu / PiSx9Z6dGxOp8eRcEvvJffIWDjVbd93YkQuqTFFOfQl0Nelwu9LRnDAhifKgG5pKi + Kzg3evVs31MguJ51 / fASOYh8OLdg1uPMJlB / 5f770dHz4XgQvYMp1AhOny8JlYyW09ThxBVQxbQ8h / AHUYe51bZupevsV9FZYZdb4lYu6zNXBkWOFVjaH / bh0cQlAKI0VB0W6Xpal3tN1BirDO7o7fy2LIcTIzJWRLp3 + wZbe7ncT2LbBDlX8KoiLlXmTeuJZtxF0fJ69LegYpnge2KI7xeT + lMmOSpFxDswBfczPOmJ9UgtApUzVGwqzDzAd75SfNHaGGuolyYXUlZnyVnzm25D2JWddI3ceUXU79Q28PsH8jd1lQlY / fyTmhdCQP45qFeuwO89U7lt + 1TKdvNdMJI2p1i3JzP5bgXjJdgkJ / ZBUpkhEOzOkWsBCF / XFBmW3qOWpdV4u7LGWVwauX7O6UPTK7MNnRzP53ncGe4RWury + xCVw3re / 6TTgbDNdD5PKlp9fv5Lbr1IHrGhZX + CEF7AuGowzHeOWbkDhhfRsd1QJhbwlqqqNJro2V / JXl / OD + EPcJ509WGuEA3sTEAudkvIYY7XHmEtg4ATVVg1uVpHxRfO8nWWcnB76lmlS + tI6CLAi7lz0xy4iukNrFvVjfcaDSNqtBaQZFcPRtOkEBVR + n + P0JLrnZQFtEOGXFcCEZY2XRYHokXn9jDZ6GJxpj4JKh3IPcUHoIVcUJvhJgINH2I6LvphyifllqZIoZX3zF123 / 0f9LYWRrhlJlXZLko8CjXmjicysEjbbhVFf0yg9bmFKQIno5rA5Mxb66jle / Rc1LznsMuD / pHcogHm + jZfY769gfTF8VAOIWH2J + 4 + eBzhLtxWWB + WibemEs + qszpYgouxghTo8 / KcfOdfwN8CelOcB1OzM5Ef0gs7456F4kJtTLfT + uxt1EroCC97yATnELbbjEkYdWK / NPR / sNQ + YBTLKVB2oqGH / lAIGbEKyLzo8vhh / HnqtBo71ExAU1Jc0RSIFHxBAE2aRzoqIH + AmB / ZILn9gvChkICPGT1VSSWJiqZQbnXKv3g / jyB4VwRFM4RVb43SPUsX729QiWRJx9YSvMJUIcqdDeLgINiurKjzfP8rvI / nZHiGFgHU8Zeq + 7klCo4Lodpjty5lZWGW9LJrq4XRYrITWFcrUZb + ThbGGZe1t + YngDzNp552b6GY35ZRAzfyY7SCnHyLDeimyF98PQow6fFRPRQ9Oo7444qf6xVL21TUj + FZXwiogvo7pvbk8q82KKrPmAPV / B / LRRlEyX2Eqpze + B9Hha6E0Ddn12qPlLKzGoYGeA + xgqjp5 + sjYF2w9EsMhpQhfw + QzQMq2EFLv + f15G7NphJtT + k0Kmrx8k6dHsHu8Vuc8pFJE + HAvywzyAftB3TWZkA ==',
                                         '__VIEWSTATEGENERATOR': 'CD4DDF2D',
                                         '__VIEWSTATEENCRYPTED': '',
                                         '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                                             #'3ydVi + tKhNiPOmP7pqgfaOu3G8INC + 7pzHL3h72DTjQk7zPdkNDPb7TfYA916zn6rOpL64X9cAuXgGOUTm2R1pm8v3EAnVwbD6UAAb9Hghv2uSsiZYUbyQiqR47l5 + RgTDArwGycQrNFCJjYxZSpHbYGYf1RWYaGD7UggoZadqC8EVllEVtGuobz + 5GBU3Uafz + bSsH6OMNO2zDKXTBPgG25PMx4xRTKx4QiTQxRYYM + zy9MOVJeQZhHgNaP8GmLs2 + YFXmP4AAQ8a2Osv6UxCVvmnskRDEmfOcisqBW8F7TRk0HIZgSy / bAq5XWO3WvAadSv4pYK40cM4LvCp2yLw2j0N1GHointt9HitLR6jWNka / bTXn49IJDX8gIJ + Jq + cjITlV2g2fQO5 + S + Fad1q977utd / eyoQPHlfnKdFerdknj + h2wB / ppoWGV86 + QnAnvkilX5jRy6q51CVGLHgwCtiaad962Z6E / BBBFa2etFVDtjfhYkwpYQ8yymOvbnyPnsJZ6U7z0pOzQRIT / TRs8f9ELL2ER + QM + Rdcn14T0GLa81TTypZWeT5voTbBNqaJg3iA ==',
                                         'ctl00$ContentPlaceHolder1$ddl_year': self.year,
                                         'ctl00$ContentPlaceHolder1$ddlImpl': self.implement,
                                         'ctl00$ContentPlaceHolder1$ddlDist': 'Select',
                                         'ctl00$ContentPlaceHolder1$ddlDao': 'Select',
                                     },
                                     cookies=self.cookies,
                                     callback=self.parse_district
                                     )
        self.implement = self.pop_implement()


    def parse_district(self,response):
        #self.districts = []

        self.year = response.css('select#ctl00_ContentPlaceHolder1_ddl_year > option[selected] ::attr(value)').extract_first()
        self.implement = response.css('select#ctl00_ContentPlaceHolder1_ddlImpl > option[selected] ::attr(value)').extract_first()
        self.districts = response.css('select#ctl00_ContentPlaceHolder1_ddlDist > option ::attr(value)').extract()[1:]
        #print(self.districts)
        #self.fw.write(self.year +' ' +  self.implement + ' ' +'\n')
        print(self.year, self.implement,self.districts)

        #print(3)
        self.district = self.pop_district()
        #while self.district != None:
        self.district = '01'
        print(self.district)

        yield scrapy.FormRequest(url=self.start_url,
                                     formdata={
                                         'ctl00$ScriptMain': 'ctl00$ContentPlaceHolder1$Upd | ctl00$ContentPlaceHolder1$ddlDist',
                                         '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ddlDist',
                                         '__EVENTARGUMENT': '',
                                         '__LASTFOCUS': '',
                                         '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                                             #'1ZVpYqS8qHEBjnVwNEc4raHA+CH0uOj8tCfXiGTTpZlrw / 8sHiSB4JpmPMa0U2MJHipFRAtdJ / mufYHeekL1c / EQa / 9qxS5BEi4t4xRO9o46PbXNHuOYoQGb1IVazzJ25E69xx6 / ILi7xsILq3a6kbrsGNtvEDXoQrbijW0P6Miu / PiSx9Z6dGxOp8eRcEvvJffIWDjVbd93YkQuqTFFOfQl0Nelwu9LRnDAhifKgG5pKi + Kzg3evVs31MguJ51 / fASOYh8OLdg1uPMJlB / 5f770dHz4XgQvYMp1AhOny8JlYyW09ThxBVQxbQ8h / AHUYe51bZupevsV9FZYZdb4lYu6zNXBkWOFVjaH / bh0cQlAKI0VB0W6Xpal3tN1BirDO7o7fy2LIcTIzJWRLp3 + wZbe7ncT2LbBDlX8KoiLlXmTeuJZtxF0fJ69LegYpnge2KI7xeT + lMmOSpFxDswBfczPOmJ9UgtApUzVGwqzDzAd75SfNHaGGuolyYXUlZnyVnzm25D2JWddI3ceUXU79Q28PsH8jd1lQlY / fyTmhdCQP45qFeuwO89U7lt + 1TKdvNdMJI2p1i3JzP5bgXjJdgkJ / ZBUpkhEOzOkWsBCF / XFBmW3qOWpdV4u7LGWVwauX7O6UPTK7MNnRzP53ncGe4RWury + xCVw3re / 6TTgbDNdD5PKlp9fv5Lbr1IHrGhZX + CEF7AuGowzHeOWbkDhhfRsd1QJhbwlqqqNJro2V / JXl / OD + EPcJ509WGuEA3sTEAudkvIYY7XHmEtg4ATVVg1uVpHxRfO8nWWcnB76lmlS + tI6CLAi7lz0xy4iukNrFvVjfcaDSNqtBaQZFcPRtOkEBVR + n + P0JLrnZQFtEOGXFcCEZY2XRYHokXn9jDZ6GJxpj4JKh3IPcUHoIVcUJvhJgINH2I6LvphyifllqZIoZX3zF123 / 0f9LYWRrhlJlXZLko8CjXmjicysEjbbhVFf0yg9bmFKQIno5rA5Mxb66jle / Rc1LznsMuD / pHcogHm + jZfY769gfTF8VAOIWH2J + 4 + eBzhLtxWWB + WibemEs + qszpYgouxghTo8 / KcfOdfwN8CelOcB1OzM5Ef0gs7456F4kJtTLfT + uxt1EroCC97yATnELbbjEkYdWK / NPR / sNQ + YBTLKVB2oqGH / lAIGbEKyLzo8vhh / HnqtBo71ExAU1Jc0RSIFHxBAE2aRzoqIH + AmB / ZILn9gvChkICPGT1VSSWJiqZQbnXKv3g / jyB4VwRFM4RVb43SPUsX729QiWRJx9YSvMJUIcqdDeLgINiurKjzfP8rvI / nZHiGFgHU8Zeq + 7klCo4Lodpjty5lZWGW9LJrq4XRYrITWFcrUZb + ThbGGZe1t + YngDzNp552b6GY35ZRAzfyY7SCnHyLDeimyF98PQow6fFRPRQ9Oo7444qf6xVL21TUj + FZXwiogvo7pvbk8q82KKrPmAPV / B / LRRlEyX2Eqpze + B9Hha6E0Ddn12qPlLKzGoYGeA + xgqjp5 + sjYF2w9EsMhpQhfw + QzQMq2EFLv + f15G7NphJtT + k0Kmrx8k6dHsHu8Vuc8pFJE + HAvywzyAftB3TWZkA ==',
                                         '__VIEWSTATEGENERATOR': 'CD4DDF2D',
                                         '__VIEWSTATEENCRYPTED': '',
                                         '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                                             #'3ydVi + tKhNiPOmP7pqgfaOu3G8INC + 7pzHL3h72DTjQk7zPdkNDPb7TfYA916zn6rOpL64X9cAuXgGOUTm2R1pm8v3EAnVwbD6UAAb9Hghv2uSsiZYUbyQiqR47l5 + RgTDArwGycQrNFCJjYxZSpHbYGYf1RWYaGD7UggoZadqC8EVllEVtGuobz + 5GBU3Uafz + bSsH6OMNO2zDKXTBPgG25PMx4xRTKx4QiTQxRYYM + zy9MOVJeQZhHgNaP8GmLs2 + YFXmP4AAQ8a2Osv6UxCVvmnskRDEmfOcisqBW8F7TRk0HIZgSy / bAq5XWO3WvAadSv4pYK40cM4LvCp2yLw2j0N1GHointt9HitLR6jWNka / bTXn49IJDX8gIJ + Jq + cjITlV2g2fQO5 + S + Fad1q977utd / eyoQPHlfnKdFerdknj + h2wB / ppoWGV86 + QnAnvkilX5jRy6q51CVGLHgwCtiaad962Z6E / BBBFa2etFVDtjfhYkwpYQ8yymOvbnyPnsJZ6U7z0pOzQRIT / TRs8f9ELL2ER + QM + Rdcn14T0GLa81TTypZWeT5voTbBNqaJg3iA ==',
                                         'ctl00$ContentPlaceHolder1$ddl_year': self.year,
                                         'ctl00$ContentPlaceHolder1$ddlImpl': self.implement,
                                         'ctl00$ContentPlaceHolder1$ddlDist': self.district,
                                         'ctl00$ContentPlaceHolder1$ddlDao': 'Select',
                                     },
                                     cookies=self.cookies,
                                     callback=self.parse_circle
                                     )
        self.district = self.pop_district()


    def parse_circle(self,response):
        #self.circles=[]
        self.year = response.css('select#ctl00_ContentPlaceHolder1_ddl_year > option[selected] ::attr(value)').extract_first()
        self.implement = response.css('select#ctl00_ContentPlaceHolder1_ddlImpl > option[selected] ::attr(value)').extract_first()
        self.district = response.css('select#ctl00_ContentPlaceHolder1_ddlDist > option[selected] ::attr(value)').extract_first()
        self.circles=response.css('select#ctl00_ContentPlaceHolder1_ddlDao > option ::attr(value)').extract()[1:]
        #print(self.circles)
        print(self.year, self.implement, self.district,self.circles)
        #self.fw.write(self.year + ' ' + self.implement + ' ' + self.district + ''  + '\n')
        #print(4)

        self.circle = self.pop_circle()
        #while self.circle != None:
            #self.circle = self.pop_circle()

        print(self.circle)



        self.circle='0101'
            #if self.circle !=None:
        return scrapy.FormRequest(url=self.start_url,
                                     formdata={
                                         'ctl00$ScriptMain': 'ctl00$ContentPlaceHolder1$Upd | ctl00$ContentPlaceHolder1$ddlDao',
                                         '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$ddlDao',
                                         '__EVENTARGUMENT': '',
                                         '__LASTFOCUS': '',
                                         '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                                             #'1ZVpYqS8qHEBjnVwNEc4raHA+CH0uOj8tCfXiGTTpZlrw / 8sHiSB4JpmPMa0U2MJHipFRAtdJ / mufYHeekL1c / EQa / 9qxS5BEi4t4xRO9o46PbXNHuOYoQGb1IVazzJ25E69xx6 / ILi7xsILq3a6kbrsGNtvEDXoQrbijW0P6Miu / PiSx9Z6dGxOp8eRcEvvJffIWDjVbd93YkQuqTFFOfQl0Nelwu9LRnDAhifKgG5pKi + Kzg3evVs31MguJ51 / fASOYh8OLdg1uPMJlB / 5f770dHz4XgQvYMp1AhOny8JlYyW09ThxBVQxbQ8h / AHUYe51bZupevsV9FZYZdb4lYu6zNXBkWOFVjaH / bh0cQlAKI0VB0W6Xpal3tN1BirDO7o7fy2LIcTIzJWRLp3 + wZbe7ncT2LbBDlX8KoiLlXmTeuJZtxF0fJ69LegYpnge2KI7xeT + lMmOSpFxDswBfczPOmJ9UgtApUzVGwqzDzAd75SfNHaGGuolyYXUlZnyVnzm25D2JWddI3ceUXU79Q28PsH8jd1lQlY / fyTmhdCQP45qFeuwO89U7lt + 1TKdvNdMJI2p1i3JzP5bgXjJdgkJ / ZBUpkhEOzOkWsBCF / XFBmW3qOWpdV4u7LGWVwauX7O6UPTK7MNnRzP53ncGe4RWury + xCVw3re / 6TTgbDNdD5PKlp9fv5Lbr1IHrGhZX + CEF7AuGowzHeOWbkDhhfRsd1QJhbwlqqqNJro2V / JXl / OD + EPcJ509WGuEA3sTEAudkvIYY7XHmEtg4ATVVg1uVpHxRfO8nWWcnB76lmlS + tI6CLAi7lz0xy4iukNrFvVjfcaDSNqtBaQZFcPRtOkEBVR + n + P0JLrnZQFtEOGXFcCEZY2XRYHokXn9jDZ6GJxpj4JKh3IPcUHoIVcUJvhJgINH2I6LvphyifllqZIoZX3zF123 / 0f9LYWRrhlJlXZLko8CjXmjicysEjbbhVFf0yg9bmFKQIno5rA5Mxb66jle / Rc1LznsMuD / pHcogHm + jZfY769gfTF8VAOIWH2J + 4 + eBzhLtxWWB + WibemEs + qszpYgouxghTo8 / KcfOdfwN8CelOcB1OzM5Ef0gs7456F4kJtTLfT + uxt1EroCC97yATnELbbjEkYdWK / NPR / sNQ + YBTLKVB2oqGH / lAIGbEKyLzo8vhh / HnqtBo71ExAU1Jc0RSIFHxBAE2aRzoqIH + AmB / ZILn9gvChkICPGT1VSSWJiqZQbnXKv3g / jyB4VwRFM4RVb43SPUsX729QiWRJx9YSvMJUIcqdDeLgINiurKjzfP8rvI / nZHiGFgHU8Zeq + 7klCo4Lodpjty5lZWGW9LJrq4XRYrITWFcrUZb + ThbGGZe1t + YngDzNp552b6GY35ZRAzfyY7SCnHyLDeimyF98PQow6fFRPRQ9Oo7444qf6xVL21TUj + FZXwiogvo7pvbk8q82KKrPmAPV / B / LRRlEyX2Eqpze + B9Hha6E0Ddn12qPlLKzGoYGeA + xgqjp5 + sjYF2w9EsMhpQhfw + QzQMq2EFLv + f15G7NphJtT + k0Kmrx8k6dHsHu8Vuc8pFJE + HAvywzyAftB3TWZkA ==',
                                         '__VIEWSTATEGENERATOR': 'CD4DDF2D',
                                         '__VIEWSTATEENCRYPTED': '',
                                         '__EVENTVALIDATION': response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                                             #'3ydVi + tKhNiPOmP7pqgfaOu3G8INC + 7pzHL3h72DTjQk7zPdkNDPb7TfYA916zn6rOpL64X9cAuXgGOUTm2R1pm8v3EAnVwbD6UAAb9Hghv2uSsiZYUbyQiqR47l5 + RgTDArwGycQrNFCJjYxZSpHbYGYf1RWYaGD7UggoZadqC8EVllEVtGuobz + 5GBU3Uafz + bSsH6OMNO2zDKXTBPgG25PMx4xRTKx4QiTQxRYYM + zy9MOVJeQZhHgNaP8GmLs2 + YFXmP4AAQ8a2Osv6UxCVvmnskRDEmfOcisqBW8F7TRk0HIZgSy / bAq5XWO3WvAadSv4pYK40cM4LvCp2yLw2j0N1GHointt9HitLR6jWNka / bTXn49IJDX8gIJ + Jq + cjITlV2g2fQO5 + S + Fad1q977utd / eyoQPHlfnKdFerdknj + h2wB / ppoWGV86 + QnAnvkilX5jRy6q51CVGLHgwCtiaad962Z6E / BBBFa2etFVDtjfhYkwpYQ8yymOvbnyPnsJZ6U7z0pOzQRIT / TRs8f9ELL2ER + QM + Rdcn14T0GLa81TTypZWeT5voTbBNqaJg3iA ==',
                                         'ctl00$ContentPlaceHolder1$ddl_year': self.year,
                                         'ctl00$ContentPlaceHolder1$ddlImpl': self.implement,
                                         'ctl00$ContentPlaceHolder1$ddlDist': self.district,
                                         'ctl00$ContentPlaceHolder1$ddlDao': self.circle,
                                     },
                                     cookies=self.cookies,
                                     callback=self.parse_result
                                     )
        #self.circle = self.pop_circle()
            #return scrapy.Request(url=x)




    def parse_result(self,response):
        self.year = response.css(
            'select#ctl00_ContentPlaceHolder1_ddl_year > option[selected] ::attr(value)').extract_first()
        self.implement = response.css(
            'select#ctl00_ContentPlaceHolder1_ddlImpl > option[selected] ::attr(value)').extract_first()
        self.district = response.css(
            'select#ctl00_ContentPlaceHolder1_ddlDist > option[selected] ::attr(value)').extract_first()
        self.circle = response.css(
            'select#ctl00_ContentPlaceHolder1_ddlDao > option[selected] ::attr(value)').extract_first()
        #self.fw.write(self.year + ' ' + self.implement + ' ' + self.district + ' ' + self.circle + '\n')
        print(self.year, self.implement, self.district, self.circle)
        #h=Selector(response)
        key=[]
        print(response.css("tr"))
        #y=key.
        value = response.css('td.fmDispData::text')
        for keys in response.css('tr'):
            key=keys.css('td.textLeft::text').extract()
        #print(key)
        print(len(key),len(value))
        #self.fw.write(key )
        #self.fw.write(value)
        #view(response)
        open_in_browser(response)
        #self.fw.write()
        #print(5,response.css('select#ctl00_ContentPlaceHolder1_ddlDao > option[selected] ::attr(value).text()').extract_first())

        #print(response.css('//*[@id="ctl00_ContentPlaceHolder1_grdCitz"]/tbody/tr[1]/td/table/tbody/tr[3]/td[1]').extract())
        return





        #    self.filled_circles = True
       # circle = self.pop_circle()
      #  if circle != None:

