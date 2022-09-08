from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime

class event:
    date = datetime.datetime.now().strftime("%A").lower()

    def __init__(self, name, time ,location, host ):
        self.name = name
        self.time = time
        self.location = location
        self.host = host

    def get_data(self):
        print()
        print(self.time)
        print(self.location)
        print(self.name)
        print(self.host)
        print()
    def get_today(self):
        if self.date in self.time.lower():
            self.get_data()
        




options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))


driver.get("https://cmich.campuslabs.com/engage/events")
#print(driver.page_source)
#driver.save_screenshot('screenshot.png')
event_info = driver.find_element(By.ID, 'event-discovery-list')


x = event_info.text.splitlines( )
# event name = 0
# time = 1
# location = 2
# hosts = 3




length = len(x)
name = []
time = []
location = []
hosts = []


for i in range(length):
    if(i % 4 == 0):
        name.append(x[i])
    if(i % 4 == 1):
        time.append(x[i])
    if(i % 4 == 2):
         location.append(x[i])
    if(i % 4 == 3):
         hosts.append(x[i])

         

events = []
for i in range(len(name)):
    events.append(event(name[i], time[i], location[i], hosts[i]))




print("------------------------------------------")
for i in events:
    i.get_today()

driver.close()

