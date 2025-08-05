from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class DataCollector:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def collect_data(self):

        try:
            self.driver.get(self.url)

            # Wait for the element to .fc-event-today
            try:
                today_elem = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".fc-event-today"))
                )
                today_elem.click()
            except TimeoutException:
                print(f"[ERROR - No found .fc-event-today]: {e}")
                return None
            
            # Wait for the modal
            try:
                modal = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".pop-container"))
                )
                return modal.text
            except TimeoutException:
                print("[ERROR - No found .pop-container]")
                return None
            
        except Exception as e:
            print(f"[ERROR]: {e}")
            return None
        finally:
            self.driver.quit()