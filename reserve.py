from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, datetime
from config import *


def initialize_driver():
    """Initialize the Chrome WebDriver."""
    driver = webdriver.Chrome()
    return driver


def login(driver):
    """Log in to the application."""
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    driver.find_element(By.ID, 'email').send_keys(USERNAME)
    driver.find_element(By.ID, 'password').send_keys(PASSWORD)
    
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Login"]'))
    )
    login_button.click()


def start_reservation(driver):
    """Create a new reservation."""
    create_reservation_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-sm.btn-outline-danger[onclick^="goTo"]'))
    )
    create_reservation_button.click()
    
    open_calendar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.selectDateButton'))
    )
    open_calendar_button.click()

    # Select the target date
    select_date(driver, RESERVATION_DATE)
    
    # Click the add reservation button
    add_reservation_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "addReservation"))
    )
    add_reservation_button.click()


def select_date(driver, date):
    """Select a date from the date picker."""
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bootstrap-datetimepicker-widget"))
    )
    target_date = driver.find_element(By.CSS_SELECTOR, f'td[data-day="{date}"]')
    driver.execute_script("arguments[0].click();", target_date)


def select_time(driver):
    """Select the start time for the reservation."""
    start_time_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "addReservationStartTimePicker"))
    )
    start_time_input.click()

    time_picker = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bootstrap-datetimepicker-widget"))
    )

    # Select hour
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-action='showHours']"))
    ).click()
    hour_element = WebDriverWait(time_picker, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[text()='{HOUR_TO_SELECT}']"))
    )
    hour_element.click()

    # Select minutes
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-action='showMinutes']"))
    ).click()
    minute_element = WebDriverWait(time_picker, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[text()='{MINUTE_TO_SELECT}']"))
    )
    minute_element.click()

    # Toggle period if needed
    if PERIOD_TO_SELECT == "AM":
        toggle_period = WebDriverWait(time_picker, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-action='togglePeriod']"))
        )
        toggle_period.click()

    # Close the modal
    modal_title = driver.find_element(By.ID, "addReservationModalLabel")
    modal_title.click()


def select_reservation_length(driver):
    """Select the reservation length from the dropdown."""
    select_length_container = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection--single"))
    )
    select_length_container.click()  # Open the dropdown

    option_to_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{RESERVATION_LENGTH}')]"))
    )
    option_to_select.click()


def navigate_to_next(driver):
    """Click the Next button to proceed."""
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @name='next']"))
    )

    while True:
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute >= 0 and now.second >= 0:
            next_button.click()
            break
        time.sleep(0.5)



def choose_court(driver):
    # Wait for the Left Tennis label to be clickable
    left_tennis_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "label-AMN-93736d6d9d2346bd9d93d2d778c6d92a"))
    )
    time.sleep(2)
    # Get the associated info element for Left Tennis
    left_tennis_info = driver.find_element(By.ID, "info-AMN-93736d6d9d2346bd9d93d2d778c6d92a").text
    right_tennis_info = driver.find_element(By.ID, "info-AMN-461db7b7e14a4713829c4488ee127dd7").text

    # both Court full
    if "Waitlist Only" in left_tennis_info and "Waitlist Only" in right_tennis_info:
        raise Exception("Both Courts are full.")
 
    # Check if the Left Tennis court is "Waitlist Only"
    elif "Waitlist Only" in left_tennis_info:
        # If "Waitlist Only", reserve Right Tennis court
        right_tennis_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "label-AMN-461db7b7e14a4713829c4488ee127dd7"))
        )
        right_tennis_label.click()
    else:
        # Otherwise, reserve Left Tennis court
        left_tennis_label.click()

    # Click the "Next" button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "next"))
    )
    next_button.click()


def submit(driver):
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "addReservationSubmit"))
    )
    submit_button.click()


def main():
    global HOUR_TO_SELECT, MINUTE_TO_SELECT, PERIOD_TO_SELECT, TIME_TO_EXECUTE
    driver = initialize_driver()
    try:
        login(driver)
        start_reservation(driver)
        select_time(driver)
        select_reservation_length(driver)
        navigate_to_next(driver)
        choose_court(driver)
        submit(driver)
        print("Court reserved successfully.")
    except Exception :
        HOUR_TO_SELECT = ALTERNATE_HOUR_TO_SELECT  # Select hour (01 for 1 PM) ALTERNATE
        MINUTE_TO_SELECT = ALTERNATE_MINUTE_TO_SELECT  # Select minutes (30)     ALTERNATE
        PERIOD_TO_SELECT = ALTERNATE_PERIOD_TO_SELECT  # Select period (AM or PM) 
        driver.get(LOGIN_URL)
        start_reservation(driver)
        select_time(driver)
        select_reservation_length(driver)
        navigate_to_next(driver)
        choose_court(driver)
        submit(driver)
        print("Court reserved successfully.")
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()
