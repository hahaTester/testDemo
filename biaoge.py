import xlrd
import xlwt
import json
import requests
book = xlrd.open_workbook('case.xls')
print(book.nsheets)

base_url = "http://www.test2.quanfangtongvip.com/"

def run_excel(file_name, save_file="case,xls"):
    wb=xlrd.open_workbook(file_name)
    sh=wb.sheet_by_index(0)

    # wb2 = copy(wb)
    # sh2 = wb2.get_sheet(0)

    for i in range(1, sh.nrows):
        url = base_url + sh.cell(i, 1).value
        data = json.loads(sh.cell(i, 4).value)
        headers = {}
        method = sh.cell(i, 2).value
        data_type = sh.cell(i, 3).value
        excepted = sh.cell(i, 5).value
        if data_type.lower() == 'json':
            data = json.dumps(data)
            headers = {"Content-Type": "application/json"}

        if method.lower() == "get":
            resp = requests.get(url=url, headers=headers)
        else:
            resp = requests.post(url=url, headers=headers, data=data)
        if eval(excepted):
            status = "PASS"
        else:
            status = "FAIL"
        sh2.write(i, 6, resp.text)
        sh2.write(i, 7, status)

    wb2.save(save_file)
    print("保存成功")