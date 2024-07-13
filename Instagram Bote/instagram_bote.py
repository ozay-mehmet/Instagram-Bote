import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Insta:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password
    
    def login(self):
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/")
        
        WebDriverWait(self.browser, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#loginForm")))
        
        self.browser.find_element(By.NAME, "username").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        WebDriverWait(self.browser, 30).until(EC.url_contains("accounts"))
        
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        
    def scroll_until_end(self, scroll_box):
        last_height = self.browser.execute_script("return arguments[0].scrollHeight", scroll_box)
        
        while True:
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            time.sleep(2)
            new_height = self.browser.execute_script("return arguments[0].scrollHeight", scroll_box)
            if new_height == last_height:
                break
            last_height = new_height           
        
    def getFollow(self):
        try:
            WebDriverWait(self.browser, 30).until(EC.url_contains(f"{self.username}"))
            following = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/following/')]")))
            following.click()
        except Exception as e:
            print(e)
            self.browser.get(f"https://www.instagram.com/{self.username}/")

        time.sleep(2)
        dialog = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))
        
        # dialog.send_keys(Keys.END)

        self.scroll_until_end(dialog)

        links = self.browser.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")
        names = [name.text for name in links if name.text != '']
        
        with open("follows.txt", "w", encoding='utf-8') as file:
            for name in names:
                file.write(name + "\n")
    
    def getFollowers(self):
        
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        
        try:
            WebDriverWait(self.browser, 30).until(EC.url_contains(f"{self.username}"))
            followers = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/followers/')]")))
            followers.click()
        except Exception as e:
            print(e)
            self.browser.get(f"https://www.instagram.com/{self.username}/")

        time.sleep(2)
        dialog = WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))

        self.scroll_until_end(dialog)
        
        time.sleep(2)
        links = self.browser.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")

        with open("followers.txt", "w", encoding='utf-8') as file:
            names = [name.text for name in links if name.text != '']
            for name in names:
                file.write(name + "\n")
    
    def compare_follows_and_followers(self):
        with open("follows.txt", "r", encoding='utf-8') as file:
            follows = [line.strip() for line in file.readlines()]
        
        with open("followers.txt", "r", encoding='utf-8') as file:
            followers = [line.strip() for line in file.readlines()]
        
        not_following_back = [user for user in follows if user not in followers]
        not_followed_back = [user for user in followers if user not in follows]
        
        with open("compare.txt", "w", encoding='utf-8') as file:
            file.write("Not Following Back:\n")
            for user in not_following_back:
                file.write(user + "\n")
            
            file.write("\nNot Followed Back:\n")
            for user in not_followed_back:
                file.write(user + "\n")
        
    
    def closeInsta(self):
        self.browser.quit()        
    
username = input("Please enter a username : ")        
password = input("Please enter a password : ")
    
insta = Insta(username, password)
insta.login()
insta.getFollow()
insta.getFollowers()
insta.compare_follows_and_followers()
insta.closeInsta()
