from difflib import get_close_matches
dict = {"above": "in a higher position than something else",
        "broom": "brush with long handle and bristles used for cleaning the floor or ground",
        "centenary":"100 years after an important event"}
word = input("Enter a word : ")
if word in dict.keys():
    print("Meaning : "+dict[word])
elif(len(get_close_matches(word,dict.keys())) >0):
    print(f"Did you mean { get_close_matches(word,dict.keys())[0] } ?")
else:
    print("Word doesn't exist!")
    