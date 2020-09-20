from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json, requests

URL = "https://us04web.zoom.us/wc/join/93275589158"
driver = webdriver.Chrome(executable_path="./scraper/chromedriver")
driver.get(URL)
name = driver.find_element_by_id("inputname")
name.send_keys("ZConnect")
name.send_keys(Keys.ENTER)
last_chat = None

def make_request(chat):
    usernames = chat.find_elements_by_tag_name("span")
    sender = usernames[0].text
    print(sender)
    if sender == "Me":
        print("me")
        return
    receiver = usernames[1].text
    is_private = True if chat.find_elements_by_class_name("chat-privately") else False
    text = chat.find_elements_by_class_name("chat-item__chat-info-msg")[0].text
    print(text)
    data = {
        "id": 0,
        "from": sender,
        "to": receiver,
        "message": text,
        "is_private": is_private,
    }
    data_json = json.dumps(data)
    print(data_json)

    response = requests.post(url="http://gcp.sidp.me/data",json=data_json)
    
    if response.status_code == 200:
        response_data = response.json()
        message = response_data["message"]
        print(message)
        if message != "":
            chatbox = driver.find_element_by_class_name("chat-box__chat-textarea")
            chatbox.send_keys(message)
            chatbox.send_keys(Keys.ENTER)

def get_chat():
    chats = driver.find_elements_by_class_name("chat-item__chat-info")
    print(len(chats))
    if last_chat == None:
        print(chats[0])
        return chats[0]
    else:
        chat_field = driver.find_elements_by_class_name("chat-content__chat-scrollbar")[0]
        while (chat.get_attribute("innerHTML") != last_chat):
            chat_field.click()
            chat_field.send_keys(Keys.ARROW_UP)
            chats = driver.find_elements_by_class_name("chat-item__chat-info")
            print(len(chats))
            for i, chat in enumerate(reversed(chats)):
                if chat.get_attribute("innerHTML") == last_chat:
                    return chat[i - 1]
# ASSUME that same person doesn't send more than 

while(True):
    time.sleep(1)
    print("heartbeat")
    try:
        print(last_chat)
        chat = get_chat()
        make_request(chat)
        last_chat = chat.get_attribute("innerHTML")
            
    except Exception as e:
        print(type(e))
        continue