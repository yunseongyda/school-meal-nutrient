from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataCollector:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def collect_data(self):
        self.driver.get(self.url)

        # check if HTML elements are found
        elems = self.driver.find_elements(By.CSS_SELECTOR, ".fc-event-today")
        if not elems:
            print("No events found on the page.")
            self.driver.quit()

        # click today
        self.driver.find_element(By.CSS_SELECTOR, ".fc-event-today").click()

        # wait for the modal to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".pop-container"))
        )

        # parse the modal content
        modal = self.driver.find_element(By.CSS_SELECTOR, ".pop-container")
        data = modal.text

        self.driver.quit()
        return data