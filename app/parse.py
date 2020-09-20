import requests

'''parser for polls'''
def parser(json_data):
    
    parsed = json_data.split()
    question = parsed[0]
    options = parsed[1:len(parsed)-1]
    
    return question, options