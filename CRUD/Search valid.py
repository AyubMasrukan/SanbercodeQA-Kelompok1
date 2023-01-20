import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class TestSearch_valid(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    def test_search_novalid(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "Username").send_keys("ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("ayub123")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click()
        time.sleep(2)
        driver.find_element(By.ID, "searching").send_keys("Ayub")
        time.sleep(2)

        response_message = driver.find_element(By.XPATH, "/html/body/div/div/table/tbody/tr[2]/td[1]").text
        self.assertEqual(response_message, 'Ayub')
    


unittest.main()
