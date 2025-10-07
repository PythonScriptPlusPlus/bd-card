from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Path to your chromedriver executable
# CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'  # Update if needed

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
df = pd.DataFrame(columns=["date", "text", "views", "media","reactions","is_forwarded"])

try:
    url = "https://t.me/s/yottoikotto"
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    # Example: Parse message texts
    # target_text = "November 15, 2024"
    target_text = "September 18"
    last_height = driver.execute_script("return document.body.scrollHeight")
    found = False

    while not found:
        page_source = driver.page_source
        if target_text in page_source:
            print(f'"{target_text}" exists on the page.')
            found = True
            break
        # Scroll up by simulating PAGE_UP key
        driver.execute_script("window.scrollBy(0, -window.innerHeight);")
        time.sleep(1)  # Wait for new content to load
        new_height = driver.execute_script("return window.pageYOffset")
        # If we can't scroll up anymore, break to avoid infinite loop
        if new_height == 0:
            print(f'"{target_text}" does not exist on the page.')
            break
        print("Scrolling up...")

    for post in driver.find_elements(By.CSS_SELECTOR, "div.tgme_widget_message_wrap"):
        try:
            date_elem = post.find_element(By.CSS_SELECTOR, "time")
            print(date_elem.get_attribute('outerHTML'))
            date = date_elem.get_attribute("datetime") if date_elem else None
        except NoSuchElementException:
            print("Date element not found.")
            date = None

        try:
            text = post.find_element(By.CSS_SELECTOR, "div.tgme_widget_message_text").text
        except NoSuchElementException:
            text = None

        try:
            views = post.find_element(By.CSS_SELECTOR, "span.tgme_widget_message_views").text
        except NoSuchElementException:
            views = None

        try:
            media = post.find_elements(By.CSS_SELECTOR, "a.tgme_widget_message_photo_wrap, a.tgme_widget_message_document_wrap, a.tgme_widget_message_video_player")
            media_links = [m.get_attribute("href") for m in media if m.get_attribute("href")]
        except NoSuchElementException:
            media_links = None

        try:
            reaction_spans = post.find_elements(By.CSS_SELECTOR, "span.tgme_reaction")
            reactions = {}
            for span in reaction_spans:
                pair = span.text.split()
                emoji = pair[0]
                if emoji == '❤':
                    emoji = '❤️'
                if emoji == '❤\u200d🔥':
                    emoji = '❤️‍🔥'
                count = pair[1]
                reactions[emoji] = count
        except NoSuchElementException:
            reactions = None

        try:
            is_forwarded = bool(post.find_elements(By.CSS_SELECTOR, "div.tgme_widget_message_forwarded"))
        except NoSuchElementException:
            is_forwarded = False

        df = pd.concat([df, pd.DataFrame([{
            "date": date,
            "text": text,
            "views": views,
            "media": media_links,
            "reactions": reactions,
            "is_forwarded": is_forwarded
        }])], ignore_index=True)

        df.to_csv("telegram_messages.csv", index=False)
        
finally:
    driver.quit()