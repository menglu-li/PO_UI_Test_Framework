import xlrd, os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info.xls')

class ElementinfoUtil:

    def __init__(self, sheet_name, file_path = excel_path):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = xlrd.open_workbook(file_path)
        self.worksheet = self.workbook.sheet_by_name(sheet_name)


    def getelement_info(self):

        rows = self.worksheet.nrows
        element_infos = {}
        for i in range(1,rows):
            element_info = {}
            element_info['element_name'] = self.worksheet.cell_value(i,1)
            element_info['locator_type'] = self.worksheet.cell_value(i,2)
            element_info['locator_value'] = self.worksheet.cell_value(i,3)
            element_info['timeout'] = int(self.worksheet.cell_value(i,4))
            element_infos[self.worksheet.cell_value(i, 0)] = element_info
            # print(element_info)
        print(element_infos)
        return element_infos

# elelment_info = ElementinfoUtil('project_page').getelement_info()

