'''/anon [TEXT] - anonymous
/startpoll [QUESTION] [OPTION1] [OPTION2] […]
/starteng
/endeng
/showeng - TEMP command'''

import numpy as np
import matplotlib.pyplot as plt
from app.piazza import piazza_search

CLASS_ID = 'kd8aencspmt2tb'


def parse_eng(messages):
    final = []
    responses = []
    for i in range(len(messages)):
        if ("starteng" in messages[i]):
            i+=1
            while(i < len(messages) and "stopeng" not in messages[i]):
                rating = messages[i][0]
                if rating.isnumeric() and int(rating) >= 1 and int(rating) <= 5:
                    responses.append(int(messages[i][0]))
                i+=1
            final.append(responses)
            responses = []
    return final

def handle_command(message, global_history, temp_history):
    message_arr = message.split(" ", 2)
    command = message_arr[0]
    if command == "/anon":
        return anon(message.split("/anon")[1]), False
    elif command == "/starteng":
        return starteng(), True
    elif command == "/stopeng":
        return stopeng(), False
    elif command == "/showeng":
        hists = parse_eng(temp_history)
        if len(hists) > 0:
            return showeng(hists[0]), False
    elif command == "/showeng_final":
        return showeng_final(parse_eng(global_history)), False
    elif command == "/startpoll":
        if message_arr[1].isnumeric():
            return startpoll(message_arr[1]), False
    elif command == "/endpoll":
        return endpoll(), False
    elif command == "/question":
        if len(message_arr) == 2:
            query = message_arr[1]
            return piazza_search(CLASS_ID, query), False
        n, query = message_arr[1], message_arr[2]
        if n.isnumeric():
            return piazza_search(CLASS_ID, query, int(n)), False
        else:
            query = message.split(" ", 1)[1]
            return piazza_search(CLASS_ID, query), False
        return "", False
    return "", False

def anon(message):
    if message or len(message) > 0:
        return "Someone asked:" + message
    return ""

def startpoll(text):
    #question, options = parse.parser(text)
    return

def endpoll():
    return

def starteng():
    return "Checkpoint: Hey there! How well would you say you understood the content on the last slide (1 = not at all , 5 = crystal clear)?"

def stopeng():
    return ""

def showpoll(hist, question, options):
    '''options are all of the diff'''
    return ""

def showeng(hist):
    '''shows histogram of student understanding for a given slide '''
    '''assume data is in form of histogram with bins 1, 2, 3, 4, 5'''
    plt.figure()
    plt.hist(hist, facecolor='blue', alpha=0.5)
    plt.xticks([1, 2, 3, 4, 5])
    plt.show()
    plt.title('Distribution of Student Understanding: Most recent slide (sample size of ' + str(len(hist)) + ' students)')
    plt.xlabel('Level of Understanding')
    plt.ylabel('Count')
    plt.show()
    plt.savefig('recent.png')
    return ""

def showeng_final(array_hists):
    '''shows histogram of average student understanding across all slides'''
    avgs = []
    for array in array_hists:
        avgs.append(np.mean(array)) 
    
    slides = np.linspace(1, len(array_hists), num=len(array_hists))
    print(np.shape(slides))
    print(np.shape(avgs))
    plt.figure()
    plt.bar(slides,avgs)
    plt.xticks(slides)
    plt.title('Student Understanding per Slide')
    plt.xlabel('Slide')
    plt.ylabel('Average Student Understanding')
    plt.show()
    
    plt.boxplot(array_hists)
    plt.show()
    plt.title('Student Understanding all Slides')
    plt.xlabel('Slide')
    plt.ylabel('Student Understanding')
    plt.savefig('understanding_allslides.png')

    return ""
        
    







