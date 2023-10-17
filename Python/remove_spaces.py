# Given a string as input, output it without spaces

def removeSpacesA(str):
    str = str.replace(" ", "")
    return str

print(removeSpacesA(" a n apple a day keeps the doctor awa y  "))

def removeSpacesB(str):
    new_str = ""
    i = 0
    while i < len(str):
        if(str[i] != " "):
            new_str += str[i]
        i += 1
    return new_str

print(removeSpacesB(" a n apple a day keeps the doctor awa y  "))