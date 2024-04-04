from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()
        sleep(60)
        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        down = download_speed.text
        up = upload_speed.text
        return f"Hey Internet Provider, why is my internet speed {down}down/{up}up when I'm paying for " \
               f"{PROMISED_DOWN}down/{PROMISED_UP}up?"

    def tweet_at_provider(self, the_tweet):
        # Login to Twitter
        self.driver.get("https://twitter.com/")
        sleep(6)
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
        login_button.click()
        sleep(4)
        username_input = self.driver.find_element(By.CSS_SELECTOR, "input")
        username_input.send_keys("pythonbooty", Keys.ENTER)
        sleep(4)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("0601masa", Keys.ENTER)
        sleep(5)
        post_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/compose/tweet"]')
        post_button.click()
        sleep(2)
        input_field = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        input_field.send_keys(the_tweet, Keys.COMMAND, Keys.ENTER)


twitter_bot = InternetSpeedTwitterBot()
tweet_text = twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider(tweet_text)
