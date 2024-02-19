import os , time
from selenium import webdriver 
from selenium.common.exceptions import WebDriverException as E
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#os.environ['PATH'] += r'/home/sheela/Downloads/webdriver/chromedriver-linux64'


#driver = webdriver.Chrome()

class Twitterbot:
    
    def __init__(self , email , password):
        self.email = email
        self.password= password
        
        os.environ['PATH'] += r'/root_directory/root/your_folder/webdriver/chromedriver-linux64'
        
        
        # Creating a webdriver.Chrome instance
        self.bot = webdriver.Chrome()
        
        
    def login(self):
       
         #it refering the instance of webdriver which we have created inside constructor above
         bot = self.bot
        
         #fetch login page
         bot.get("http://www.google.com")
         print("opening google")
         time.sleep(5)
         
         print("opening twitter")
         bot.get('https://twitter.com/')
         time.sleep(5)
         
         
         print("waiting for signin to be present")
         Signin_button = WebDriverWait(bot , 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , '[data-testid="loginButton"]'))).click()
         print("Clicking the signin button")
         time.sleep(5)

         #WebDriverWait(bot , 10).until(EC.presence_of_element_located((By.CLASS_NAME , "1")))
        
         print("opening login page")
         email = bot.find_element(By.CSS_SELECTOR, 'input[type="text"][name="text"]' )  
         email.send_keys(self.email , Keys.RETURN)
         print("email send")
         time.sleep(5)
         
         
         password = bot.find_element(By.CSS_SELECTOR, 'input[type="password"][name="password"]')  
         password.send_keys(self.password, Keys.RETURN)
         print("provide password")
         time.sleep(10)
         
         
         login_button= bot.find_element(By.CSS_SELECTOR, 'div.css-1rynq56 span.css-1qaijid')
         login_button.click()
         time.sleep(5)
         

         
         # Check if login was successful (you need to adapt this based on your HTML structure)
         if "https://twitter.com/home" in bot.current_url:
                print("Login successful")
         else:
                print("Login failed")
        
        
    def like_retweet(self , hastag):
        pass

        
    
