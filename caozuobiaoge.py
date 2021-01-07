import xlrd
import requests


base_url = "http://www.test2.quanfangtongvip.com/"

book = xlrd.open_workbook('case.xls')
sh = book.sheet_by_index(0)

# method=sh.cell(1,2).value
# print(method)


url = base_url + sh.cell(1,1).value
method = sh.cell(1,2).value
data = sh.cell(1,3).value
print(data)
re = requests.post(url=url,params = data)
print(re.text)
