from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = "https://us04web.zoom.us/wc/join/93275589158"
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(URL)
name = driver.find_element_by_id("inputname")
name.send_keys("ZConnect")
name.send_keys(Keys.ENTER)
waiting_for_login = input()

chatbox = driver.find_element_by_class_name("chat-box__chat-textarea")
chatbox.send_keys("test")
chatbox.send_keys(Keys.ENTER)

chat_data = []
while(True):
    time.sleep(1)
    try:
        chat = driver.find_elements_by_class_name("chat-item__chat-info")[-1]
        usernames = chat.find_elements_by_tag_name("span")
        sender = usernames[0].text
        receiver = usernames[1].text
        private = True if chat.find_elements_by_class_name("chat-privately") else False
        text = chat.find_elements_by_class_name("chat-item__chat-info-msg")[0].text
        tup = (sender, receiver, private, text)
        if len(chat_data) == 0 or tup != chat_data[-1]:
            chat_data.append(tup)
        print(chat_data)
    except Exception:
        continue