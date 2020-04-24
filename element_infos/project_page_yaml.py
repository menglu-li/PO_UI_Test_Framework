import os,time
from selenium import webdriver
from element_infos.login_page_po import LoginPage
from common.log_utils import logger
from common.yaml_element_info_utils import YamlElementinfoUtils


class ProjectPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.input_username('admin')
        self.input_password('admin123456')
        self.click_login()
        element_info = YamlElementinfoUtils()

        # 项目页各链接（除下拉选项链接）
        self.project_link = element_info.get_element_info('project_link')
        self.task_link = element_info.get_element_info('task_link')
        self.kanban_link = element_info.get_element_info('kanban_link')
        self.burn_link = element_info.get_element_info('burn_link')
        self.story_link = element_info.get_element_info('story_link')
        self.qa_link = element_info.get_element_info('qa_link')
        self.doc_link = element_info.get_element_info('doc_link')
        self.team_link = element_info.get_element_info('team_link')
        self.effort_link = element_info.get_element_info('effort_link')
        self.action_link = element_info.get_element_info('action_link')
        self.product_link = element_info.get_element_info('product_link')
        self.view_link = element_info.get_element_info('view_link')

        # 新增项目页面
        self.add_project_button = element_info.get_element_info('add_project_button')
        self.add_project_link = element_info.get_element_info('add_project_link')
        self.project_name = element_info.get_element_info('project_name')
        self.project_code = element_info.get_element_info('project_code')
        self.start_end_date = element_info.get_element_info('start_end_date')
        self.project_save_button = element_info.get_element_info('project_save_button')

        # 新增任务页面
        self.add_task_button = element_info.get_element_info('add_task_button')
        self.task_project_select = element_info.get_element_info('task_project_select')
        self.task_project_select_result = element_info.get_element_info('task_project_select_result')
        self.task_type_select = element_info.get_element_info('task_type_select')
        self.task_type_result = element_info.get_element_info('task_type_result')
        self.task_name = element_info.get_element_info('task_name')
        self.task_save_button = element_info.get_element_info('task_save_button')

    def goto_project_link(self):
        self.click(self.project_link)

    def goto_task_link(self):
        self.click(self.task_link)

    def goto_kanban_link(self):
        self.click(self.kanban_link)

    def goto_burn_link(self):
        self.click(self.burn_link)

    def goto_story_link(self):
        self.click(self.story_link)

    # 待更新，qa link是下拉选项
    # def goto_qa_link(self):
    #     self.click(self.qa_link)

    def goto_doc_link(self):
        self.click(self.doc_link)

    def goto_team_link(self):
        self.click(self.team_link)

    def goto_effort_link(self):
        self.click(self.effort_link)

    def goto_action_link(self):
        self.click(self.action_link)

    def goto_product_link(self):
        self.click(self.product_link)

    def goto_view_link(self):
        self.click(self.view_link)

    # 新增项目页面操作
    def click_add_project_button(self):
        self.click(self.add_project_button)
        logger.info("点击新增项目按钮")

    def click_add_project_link(self):
        self.click(self.add_project_link)
        logger.info("点击页面中新增项目的链接")

    def input_project_name(self, project_name):
        self.input(self.project_name, project_name)
        logger.info("输入项目名称%s" % project_name)

    def input_project_code(self, project_code):
        self.input(self.project_code, project_code)
        logger.info("输入项目代码%s" % project_code)

    def input_start_end_date(self):
        self.click(self.start_end_date)
        logger.info("选择起始日期=一星期")

    def click_save_project_button(self):
        self.scroll_to_element(self.project_save_button)
        self.click(self.project_save_button)
        logger.info("点击保存项目按钮")

    # 新增任务页面操作
    def click_add_task_button(self):
        self.click(self.add_task_button)
        logger.info("点击新增任务按钮")

    def input_task_project(self, project_name):
        self.click(self.task_project_select)
        task_project = self.task_project_select_result['locator_value'] + '//li[text()="' + str(project_name) + '"]'
        self.task_project_select_result['locator_value'] = task_project
        time.sleep(2)
        self.click(self.task_project_select_result)
        logger.info("选择所属项目%s" % project_name)

    def input_task_type(self, task_type):
        self.click(self.task_type_select)
        task_type = self.task_type_result['locator_value'] + '//li[text()="' + str(task_type) + '"]'
        self.task_type_result['locator_value'] = task_type
        time.sleep(2)
        self.click(self.task_type_result)
        logger.info("选择任务类型%s" % task_type)

    def input_task_name(self, task_name):
        self.input(self.task_name, task_name)
        logger.info("输入任务名称%s" % task_name)

    def click_save_task_button(self):
        self.scroll_to_element(self.task_save_button)
        self.click(self.task_save_button)
        logger.info("点击任务保存按钮")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/biz/user-login-L2Jpei8=.html")
    projectpage = ProjectPage(driver)
    # 各页面链接跳转
    projectpage.goto_project_link()
    projectpage.goto_task_link()
    projectpage.goto_kanban_link()
    projectpage.goto_burn_link()
    projectpage.goto_story_link()
    projectpage.goto_doc_link()
    projectpage.goto_team_link()
    projectpage.goto_effort_link()
    projectpage.goto_product_link()
    projectpage.goto_view_link()

    # 新增项目
    # projectpage.goto_project_link()
    # projectpage.click_add_project_button()
    # projectpage.input_project_name("项目名称01")
    # projectpage.input_project_code("project01")
    # projectpage.input_start_end_date()
    # projectpage.click_save_project_button()

    # 新增任务
    projectpage.goto_project_link()
    projectpage.goto_task_link()
    projectpage.click_add_task_button()
    projectpage.input_task_project("项目名称01")
    projectpage.input_task_type("设计")
    projectpage.input_task_name("任务名称02")
    projectpage.click_save_task_button()

    driver.close()
