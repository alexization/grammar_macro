from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class grammar():
    def __init__(self) -> None:
        super().__init__()

    def open_grammar(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://speller.cs.pusan.ac.kr/')
        self.driver.implicitly_wait(5)

    def spell_check(self, str_before):
        self.driver.find_element(By.ID, 'text1').send_keys(str_before)
        self.driver.find_element(By.ID, 'btnCheck').click()
        test = self.driver.find_element(By.XPATH, 
        '/html/body/table/tbody/tr[2]/td').text

        if test[0:3] == '맞춤법':
            self.driver.find_element(By.ID, 'btnRenew2').click()
            return str_before

        count = 1
        while True:
            try:
                self.driver.find_element(By.XPATH, 
                f"/html/body/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[2]/td[1]/div/table/tbody/tr/td/font[{count}]/span").click()
                count += 1

            except:
                break
        
        str_after = self.driver.find_element(By.XPATH, "/html/body/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[2]/td[1]/div/table/tbody/tr/td").text
        self.driver.find_element(By.ID, 'btnRenew2').click()
        
        return str_after