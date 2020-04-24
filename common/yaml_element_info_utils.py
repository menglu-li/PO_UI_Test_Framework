import yaml , os

current_path = os.path.dirname(__file__)
yaml_path = os.path.join(current_path, '../element_info_datas/element_info.yaml')

class YamlElementinfoUtils:

    def __init__(self, file_path = yaml_path):
        self.file_path=file_path
        self.file = open(file_path, encoding='utf-8')
        self.file_data = yaml.safe_load(self.file)

    def get_element_info(self,element_en_name):
        element_infos = {}
        for i in range(len(self.file_data)):
            element_info = {}
            element_info['element_name'] = self.file_data[element_en_name][0]['element_name']
            element_info['locator_type'] = self.file_data[element_en_name][1]['locator_type']
            element_info['locator_value'] = self.file_data[element_en_name][2]['locator_value']
            element_info['timeout'] = self.file_data[element_en_name][3]['timeout']
            element_infos = element_info.copy()
        return element_infos

if __name__ =='__main__':
    element_info = YamlElementinfoUtils()
    project_link = element_info.get_element_info('project_link')
    print(project_link)

