"""
def search():
    word = input("Enter The word you want search : ")
    if(word.lower() == "smog"):
        print("Pollution")
    cont = input("Do you want search again ? ");
    if(cont == 'Y'.lower()):
        search()
    else:
        print("Thank You")
        return
search()
"""
import json
data = json.load(open("/home/VrajPatel/Desktop/Vraj Patel/Python/Data Dictionary/data.json"))
word = input("Enter The word you want search : ")

def search(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Not Found !!")
       
print(search(word))