from selenium import webdriver
import os
import time

class InstagramBot:
    def __init__(self, username, password):
        self.base_url = 'https://www.instagram.com'
        self.login_url = 'https://www.instagram.com/accounts/login/'
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def login(self):
        """
        Logs in

        """
        self.driver.get(self.login_url)
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        time.sleep(2)
        
    def nav_user(self, user):
        """
        Navigates to the user profile

        Args:
            user:str: name of the user profile 
        """
        self.driver.get('{}/{}'.format(self.base_url, user))

    def follow_user(self, user):
        """
        Navigates and follows the user profile that you pass

        Args:
            user:str: name of the user profile that you want to follow
        """
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click() 


if __name__ == "__main__":
    ig_bot = InstagramBot('place here username', 'place here password')

    ig_bot.login()
    ig_bot.follow_user('champagnepapi')