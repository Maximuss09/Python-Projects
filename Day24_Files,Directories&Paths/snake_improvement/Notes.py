
# --------------------------------
# OPTION 1
# file = open("my_text")
# content = file.read()
# print(content) 
# file.close()

with open("C:/Users/ttpin/OneDrive/Documentos/Python Docs/Day24_Files,Directories&Paths/my_text") as file: 
    content = file.read()
    print(content)



#OPTION 2

with open("C:/Users/ttpin/OneDrive/Documentos/Python Docs/Day24_Files,Directories&Paths/my_text", mode="a",) as file: 
    file.write("\nNew Text.")
    
# ------------------------------------

