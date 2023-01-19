import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class TestCreat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    def test_Creat_valid(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("ayub123")
        time.sleep(2)
        driver.find_element(
            By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div/p[1]/a").click()
        time.sleep(2)
        driver.find_element(By.ID, "Name").send_keys("Ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Company").send_keys("Sanbercode")
        time.sleep(2)
        driver.find_element(By.ID, "Address").send_keys("Ngawi")
        time.sleep(2)
        driver.find_element(By.ID, "City").send_keys("Kedunggalar")
        time.sleep(2)
        driver.find_element(By.ID, "Phone").send_keys("089876545344")
        time.sleep(2)
        driver.find_element(By.ID, "Email").send_keys("ayub@gmail.com")
        time.sleep(2)
        driver.find_element(
            By.XPATH, "/html/body/div/form/div/div[7]/div/input").click()
        time.sleep(2)


unittest.main()
