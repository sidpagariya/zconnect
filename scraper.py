from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json, requests

URL = "https://us04web.zoom.us/wc/join/93275589158"
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(URL)
name = driver.find_element_by_id("inputname")
name.send_keys("ZConnect")
name.send_keys(Keys.ENTER)
waiting_for_login = input()

# ASSUME that same person doesn't send more than 
last_index = 0
while(True):
    time.sleep(1)
    try:
        chats = driver.find_elements_by_class_name("chat-item__chat-info")
        while (len(chats) > last_index):
            chat = chats[last_index]
            usernames = chat.find_elements_by_tag_name("span")
            sender = usernames[0].text
            if sender == "Me":
                last_index += 1
                continue
            receiver = usernames[1].text
            is_private = True if chat.find_elements_by_class_name("chat-privately") else False
            text = chat.find_elements_by_class_name("chat-item__chat-info-msg")[0].text
            data = {
                "id": last_index,
                "from": sender,
                "to": receiver,
                "text": text,
                "is_private": is_private,
            }
            data_json = json.dumps(data)
            print(data_json)
            last_index += 1
            response = {"text": "test"} # requests.post(url="https://gcp.sidp.me/data", json=data_json)
            if response != "":
                response_data = json.loads(response)
                message = response_data["text"]
                chatbox = driver.find_element_by_class_name("chat-box__chat-textarea")
                chatbox.send_keys(message)
                chatbox.send_keys(Keys.ENTER)
    except Exception:
        continue