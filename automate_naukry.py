import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
login = driver.find_element(By.XPATH, "//a[@title='Jobseeker Login']")
login.click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys("shriyaghosh13@gmail.com")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'password')]").send_keys("22061996@Xyz")
time.sleep(2)
driver.find_element(By.XPATH, "//button[contains(@class,'loginButton')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='View profile']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@id='attachCV']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='attachCV']").send_keys("/Users/souradeep/PycharmProjects/Ui_Automation/Resume.pdf")
time.sleep(5)