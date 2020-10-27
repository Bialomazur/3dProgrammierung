def remove_bmw(string):


    if type(string) != type(""):
        raise Exception("This program only works for text.")

    return string.replace("b","").replace("B","").replace("W","").replace("M","").replace("m","").replace("w","")
    
    # forbidden_letters = ["b", "B", "m","M", "w", "W"]

    # for letter in string:
    #     if letter == "b





print(remove_bmw("bmwHELLO World!"))
print(remove_bmw(123123))