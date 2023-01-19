import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    def test_register_valid(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "FirstName").send_keys("Ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Surname").send_keys("Masrukan")
        time.sleep(2)
        driver.find_element(By.ID, "E_post").send_keys(
            "ayub.masrukan0@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "Mobile").send_keys("08879765434754")
        time.sleep(2)
        driver.find_element(By.ID, "Username").send_keys("ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("ayub123")
        time.sleep(2)
        driver.find_element(By.ID, "ConfirmPassword").send_keys("ayub123")
        time.sleep(2)
        driver.find_element(By.ID, "submit").click()
        time.sleep(5)

        response_message = driver.find_element(
            By.XPATH, "/html/body/div/form/div/div[9]/div/label").text
        self.assertEqual(response_message, 'Registration Successful')

    def test_register_usernamesama(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "FirstName").send_keys("Ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Surname").send_keys("Masrukan")
        time.sleep(2)
        driver.find_element(By.ID, "E_post").send_keys(
            "ayub.masrukan0@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID, "Mobile").send_keys("08879765434754")
        time.sleep(2)
        driver.find_element(By.ID, "Username").send_keys("ayub")
        time.sleep(2)
        driver.find_element(By.ID, "Password").send_keys("ayub123")
        time.sleep(2)
        driver.find_element(By.ID, "ConfirmPassword").send_keys("ayub123")
        time.sleep(2)
        driver.find_element(By.ID, "submit").click()
        time.sleep(5)

        response_message = driver.find_element(
            By.XPATH, "/html/body/div/form/div/div[10]/div/label").text
        self.assertEqual(response_message, 'Username already exist')


unittest.main()
