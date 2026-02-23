from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:8000/login.php")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("nimda666!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Add New Contact")))


def test_add_contact(driver):
    wait = WebDriverWait(driver, 10)
    login(driver)

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add New Contact"))).click()

    wait.until(EC.presence_of_element_located((By.NAME, "name")))

    driver.find_element(By.NAME, "name").send_keys("Selenium")
    driver.find_element(By.NAME, "email").send_keys("selenium@test.com")
    driver.find_element(By.NAME, "phone").send_keys("08123456789")
    driver.find_element(By.NAME, "title").send_keys("Tester")

    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Save']").click()

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Add New Contact")))

    assert True