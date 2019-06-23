from selenium import webdriver

class login:
    def __init__(self,driver):
        self.driver=driver

    def loginactime(self,un,pwd):
        self.driver.find_element_by_name("username").send_keys(un)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_xpath("//a[@class='initial']").click()



