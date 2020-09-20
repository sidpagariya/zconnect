# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:48:30 2020

@author: sanje
"""

'''/anon [TEXT] - anonymous
/startpoll [QUESTION] [OPTION1] [OPTION2] […] 
/endpoll
/starteng [N] - samples N students for engagement 
/endeng
/showpoll - TEMP command
/showeng - TEMP command'''

import numpy as np
import matplotlib.pyplot as plt

def parser(path):
    '''parses Zoom chat txt file'''
    messages = []
    f = open(path, "r")
    responses = []
    final = []
    for x in f:
        messages.append((x.split(":")[-1]).split("\\")[0])
    
    for i in range(len(messages)):
        if ("starteng" in messages[i]):
            i+=2
            while(i < len(messages) and "stopeng" not in messages[i]):
                rating = messages[i][1]
                if rating.isnumeric() and int(rating) >= 1 and int(rating) <= 5:
                    responses.append(int(messages[i][1]))
                i+=1
            final.append(responses)
            responses = []
    return final


def handle_command(message):
    message_arr = message.split(" ") # /anon asdjhakjsdh asdhklajsdh 
    command = message_arr[0]
    if command == "/anon":
        return anon(message.split("/anon")[1])
    elif command == "/starteng":
        return starteng()

def anon(message):
    return "Someone asked:" + message

def startpoll(text):
    #question, options = parse.parser(text)
    return

def endpoll():
    return

def starteng():
    return "Checkpoint: Hey there! How well would you say you understood the content on the last slide (1 = not at all , 5 = crystal clear)?"

def showpoll(hist, question, options):
    '''options are all of the diff'''
    return

def showeng(hist, slide):
    '''shows histogram of student understanding for a given slide '''
    '''assume data is in form of histogram with bins 1, 2, 3, 4, 5'''
    plt.figure()
    plt.hist(hist, facecolor='blue', alpha=0.5)
    plt.xticks([1, 2, 3, 4, 5])
    plt.show()
    plt.title('Distribution of Student Understanding: Slide ' + str(slide) + ' (sample size of ' + str(len(hist)) + ' students)')
    plt.xlabel('Level of Understanding')
    plt.ylabel('Count')
    plt.savefig("C:\\Users\\sanje\\OneDrive\\Desktop\\understanding_slide" + str(slide) + ".png");
    return

def showeng_final(array_hists):
    '''shows histogram of average student understanding across all slides'''
    avgs = [];
    for array in array_hists:
        avgs.append(np.mean(array));
    
    
    slides = np.linspace(1, len(array_hists), num= len(array_hists));
    print(np.shape(slides))
    print(np.shape(avgs));
    plt.figure()
    plt.bar(slides,avgs)
    plt.xticks(slides)
    plt.title('Student Understanding per Slide')
    plt.xlabel('Slide')
    plt.ylabel('Average Student Understanding')
    plt.show()
    
    plt.boxplot(array_hists);
    plt.show()
    plt.title('Student Understanding per Slide')
    plt.xlabel('Slide')
    plt.ylabel('Student Understanding')
    plt.savefig("C:\\Users\\sanje\\OneDrive\\Desktop\\understanding_allslides.png");

    return
        
    

if __name__ == "__main__":
    
    path = "C:\\Users\\sanje\\OneDrive\\Documents\\Zoom\\2020-09-19 16.37.51 EECS4LYFE Meeting Room - HackMIT 93275589158\\meeting_saved_chat.txt";
    array_hist = parser(path);
    showeng(array_hist[2], 2)
    showeng_final(array_hist)
        
    







