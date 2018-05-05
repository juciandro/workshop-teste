# -*- codding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import  unittest, time, re
from time import sleep

#class é a suit
class DadosPessoais(unittest.TestCase):
    def setUp(self): #pré-condição, self(this)
        self.driver = webdriver.Chrome(executable_path="./driver/chromedriver")#atribui o driver
        self.driver.get("http://www.eventlister.com.br/login")#url que vai ser testado
        self.driver.implicitly_wait(30)#tempo de espera espera
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_realizar_login(self):#teste
        driver =  self.driver
        sleep(5)#má praticá
        driver.find_element_by_css_selector(".outline").click()
        sleep(5)
        driver.find_element_by_xpath("(//input[@id='user_email'])[2]").click()
        driver.find_element_by_xpath("(//input[@id='user_email'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='user_email'])[2]").send_keys("souzajuciandro17@gmail.com")
        driver.find_element_by_xpath("(//input[@id='user_password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='user_password'])[2]").send_keys("programaçãoj")
        driver.find_element_by_xpath("(//input[@id='user_password'])[2]").send_keys(Keys.ENTER)

        # driver.find_element_by_id("dropdownMenuLink").click()
        # driver.find_element_by_link_text("Minha Conta").click()
        # driver.find_element_by_css_selector("li.nav-item:nth-child(2) > a:nth-child(1)").click()
        # driver.find_element_by_id("user_name").click()

        def tearDown(self):
            self.driver.quit()
            self.assertEqyal([], self.vericationErrors)

        if __name__ == '__main__':
                        unittest.main()
