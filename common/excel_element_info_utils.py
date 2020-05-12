import xlrd, os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info.xls')

class ExcelElementinfoUtil:

    def __init__(self, sheet_name, page_name, file_path = excel_path):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.page_name = page_name
        self.workbook = xlrd.open_workbook(file_path)
        self.worksheet = self.workbook.sheet_by_name(sheet_name)

    def get_element_info(self):
        rows = self.worksheet.nrows
        element_infos = {}
        for i in range(1,rows):
            if self.worksheet.cell_value(i, 2) == self.page_name:
                element_info = {}
                element_info['element_name'] = self.worksheet.cell_value(i, 1)
                element_info['locator_type'] = self.worksheet.cell_value(i, 3)
                element_info['locator_value'] = self.worksheet.cell_value(i, 4)
                element_info['timeout'] = int(self.worksheet.cell_value(i, 5))
                element_infos[self.worksheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__ =='__main__':
    element_info = ExcelElementinfoUtil('project_page', 'first_page').get_element_info()
    print("first_page", element_info)
    element_info2 = ExcelElementinfoUtil('project_page', 'project_page').get_element_info()
    print("project_page:", element_info2)
