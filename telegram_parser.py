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
    time.sleep(2)  # Wait for page to load

    # Example: Parse message texts
    target_text = "November 15, 2024"
    # target_text = "September 18"
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
        print(f"Scrolling up... {time.strftime('%Y-%m-%d %H:%M:%S')}")

    for post in driver.find_elements(By.CSS_SELECTOR, "div.tgme_widget_message_wrap"):
        try:
            date_elem = None
            for elem in post.find_elements(By.CSS_SELECTOR, "time"):
                if "time" in elem.get_attribute("class").split():
                    date_elem = elem
                    break
            # print(date_elem.get_attribute('outerHTML'))
            date = date_elem.get_attribute("datetime") if date_elem else None
        except NoSuchElementException:
            # print("Date element not found.")
            date = None

        try:
            text_elem = post.find_element(By.CSS_SELECTOR, "div.tgme_widget_message_text.js-message_text")
            text = text_elem.text
        except NoSuchElementException:
            text = None

        try:
            views = post.find_element(By.CSS_SELECTOR, "span.tgme_widget_message_views").text
        except NoSuchElementException:
            views = None

        try:
            photos = post.find_elements(By.CSS_SELECTOR, "a.tgme_widget_message_photo_wrap")
            documents = post.find_elements(By.CSS_SELECTOR, "a.tgme_widget_message_document_wrap")
            videos = post.find_elements(By.CSS_SELECTOR, "a.tgme_widget_message_video_player")

            # photo_links = [m.get_property("backgroundImage") for m in photos if m.get_property("backgroundImage") != 'none']

            photo_links = []
            for m in photos:
                bg_image = m.value_of_css_property("background-image")[4:-2]
                # print(f'bg_image: {bg_image}')
                if bg_image and bg_image != 'none':
                    photo_links.append(bg_image)
            document_links = [m.get_attribute("href") for m in documents if m.get_attribute("href")]
            video_links = [m.get_attribute("href") for m in videos if m.get_attribute("href")]

            media_links = {
            "photos": photo_links,
            "documents": document_links,
            "videos": video_links
            }
        except NoSuchElementException:
            media_links = {"photos": [], "documents": [], "videos": []}

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
            is_forwarded = bool(post.find_elements(By.CSS_SELECTOR, "div.tgme_widget_message_forwarded_from"))
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