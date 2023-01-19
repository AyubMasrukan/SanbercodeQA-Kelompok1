import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class TestEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    def test_edit_valid(self):
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
        driver.find_element(By.ID, "searching").send_keys("venkat")
        time.sleep(2)
        driver.find_element(
            By.XPATH, "/html/body/div/div/form/input[2]").click()
        time.sleep(2)
        driver.find_element(
            By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[7]/a[2]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/p/a[2]").click()
        time.sleep(2)


unittest.main()
