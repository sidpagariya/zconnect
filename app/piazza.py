from piazza_api.rpc import PiazzaRPC

def piazza_search(class_id, query, n_results=1):
    
    p = PiazzaRPC(class_id)
    p.user_login('hackmit2020@umich.edu', 'hackmit2020')
    result = p.search(query)
    
    if(len(result)==0):
        print("No Piazza results found for query: " + str(query))
        return
    
    if(len(result) < n_results):
        n_results = len(result)
    
    posts = []
    links = []
    messages = []
    for i in range(n_results):
        posts.append(result[i]["nr"])
        links.append('https://piazza.com/class/' + class_id + '?cid=' + str(posts[i]))
        messages.append(result[i]["subject"] + ": " + links[i])
        print(result[i]["subject"] + ": " + links[i])
        
    return "Results for '" + query + "' in Piazza:\n" + "\n".join(messages)