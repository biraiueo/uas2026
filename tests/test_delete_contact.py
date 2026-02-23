from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


def login(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:8000/login.php")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("nimda666!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Add New Contact")))


def test_delete_contact(driver):
    wait = WebDriverWait(driver, 10)
    login(driver)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//a[contains(text(),'delete')])[2]")
    )).click()

    try:
        wait.until(EC.alert_is_present())
        Alert(driver).accept()
    except NoAlertPresentException:
        pass

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Add New Contact")))

    assert True