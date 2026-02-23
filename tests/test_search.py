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


def test_search_contact(driver):
    wait = WebDriverWait(driver, 10)
    login(driver)

    search_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
    )

    search_box.send_keys("Sarah")

    assert search_box.get_attribute("value") == "Sarah"

    search_box.clear()