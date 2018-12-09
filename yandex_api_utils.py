import requests
import json

# Request to Yandex API
def getResultOfRequest (request_url) :
    request = requests.get(request_url)
    content = json.loads(request.content)
    return content

# Getting Text of Synonyms 
def getSynonyms (content) :
    max_lenght = len(content["def"])
    eng_synonyms = ''
    for x in range(0,max_lenght):
        eng_synonyms = eng_synonyms + content["def"][x]["tr"][0]["text"] + ','
        if 'syn' in content["def"][x]["tr"][0] :
            for syn in content["def"][x]["tr"][0]["syn"]:
                eng_synonyms = eng_synonyms + syn["text"] + ','
            
    eng_synonyms = eng_synonyms[:-1]
    return eng_synonyms

# Getting Meaning of Text
def getMeans (content) :
    max_lenght = len(content["def"])
    means = ''
    for x in range(0,max_lenght):
        if 'mean' in content["def"][x]["tr"][0] :
            for mean in content["def"][x]["tr"][0]["mean"]:
                means = means + mean["text"] + ','
            
    means = means[:-1]
    return means