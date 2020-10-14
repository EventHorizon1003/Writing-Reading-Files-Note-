import os,pyperclip
# note of os
# Adding the backlash on the path -> os.path.join()

# Find the current working directory -> os.getcwd()
    #Using os.chdir(<address>) to change the directory

# There are two ways to specify the path
    # Absolute path -> always begins with root folder
    # Relative path -> skip the program's current working directory
        # . mean this directory     eg: .\eggs means eggs is in the current working directory
        # .. mean the parent folder eg: ..\eggs mean eggs is the under root folder

# Creating new folder -> os.makedirs()
    # os.makedirs('C:\\delicious\\newfolder\\picture')

# Return the list of every filename in the path argument -> os.listdir(<>)

# Os.path module
    # os.path.abspath(.<path>) -> will convert relative path to a string of absolute path
        # . represent relative path
    # os.path.isabs(<path>) -> return True if argument is absolute path ; False if path is relative
    # os.path.relpath(path, start)  -> return the relative path from start to path / By default : cwd used as start path
    # os.path.dirname(<path>) -> return a string of everything that come before the "last file"
    # os.path.basename(<path>) -> return a string of last item
        # os.path.split(<path>) -> separate the base and dir in tuple
            # U also can use split() and path.sep to separate each folder in the list
            # See notefunction2  *** os.path.sep == "\\"
    # os.path.getsize(<path>) -> will return the size if the file of 'path' argument
    # os.path.exist(<path>) -> True : file/folder is exist
    # os.path.isfile(<path>) -> True : if the path is exist and it is file
    # os.path.isdir(<path>) -> True : if the path is exist and it is folder

#### Reading / Writing  ###
# Opening files -> open(<path>) #path can be relative or absolute
# If the file.txt is not exist, then the python will create one
    # a = open('path') *** The return value will save in File object but still cannot take the value form it.
        # a = open('path','r')  in read mode
            # Although the default mode is reading mode (wont overwrite the file)but you can still put r in the second argument
        # a = open('path','a')  in append mode
        # a = open('path','w')  in write mode

# Reading file -> a = b.read() , b is File object
    # To get the a list of the string value -> FO.readlines()
# ***See the notefunction3***

# Writing to files -> Fileobject.write(-)
# ***See the notefunction4***

#--------------------------------------------------------------
import shelve
# Save the date from the python in binary file -> shelve mode
    # only have open and close
    # it save the date like the dictionary
        # shelFile = shelve.open('mydata')
        # hero = ['axe', 'ogre', 'invoker']  ---- 'hero' is the values
        # shelFile['heros'] = hero  ---- 'heros' is the key
        # shelFile.close()
    # if u want the value return list-like values
        # shelFile = shelve.open('mydata')
        # list(shelFile.keys())
        # list(shelFile.values())
        # shelFile.close()
    # ***See the notefunction5***

#----------------------------------------------------------------
# Saving the the content of list / dictionary as a string formatted with the pprint.pformat()
# It not just easy to read but it is also syntactically correct
# So u can save it in .py file and import it later
    # ***See the notefunction6***

def notefunction0 () :
    a = os.path.join('usr','doc','gg') # join the string with '\'
    print(a)

def notefunction() :

    path = os.path.abspath('.') # get the abs path
    print(os.path.dirname(path)) # before the last folder
    print(os.path.basename(path)) # the last folder

def notefunction2() :

    a = os.path.abspath('.')
    print(a.split(os.path.sep))


def notefunction3():

    a = os.getcwd()
    path = a + "\\a" # Create the file "a"

    c = open(path)  # Open the file and return the file object
    d = c.read()    # Read the File object of c

def notefunction4():

    a = os.getcwd()
    path = a + "\\Helloworl"
    print(path)
    pyperclip.copy(a)

    c = open(path,'w')
    c.write("Hello World ! \n")

    c.close()
    c = open(path,'a')
    c.write("Bacon is not a fruit")

    c.close()
    c = open(path,'r')
    content = c.read()
    c.close()

    print(content)

def notefunction5():

    shelFile = shelve.open('mydata')
    hero = ['axe', 'ogre', 'invoker']  #'hero' is the values
    num = 0
    shelFile['heros'] = num  # 'heros' is the key
    shelFile.close()

    a = "if u want the value return list-like values"
    print(a)
    shelFile = shelve.open('mydata')
    k = list(shelFile.keys())
    print(k)
    v = list(shelFile.values())
    print(v)
    shelFile.close()

def notefunction6() :
# Define the datapath
    path = "C:\\Users\\ACER\\Desktop\\Python\\Revisiom\\Hero.py"
    print(path)
# Write the data with ppformat
    import pprint
    hero = [{'name':'voker','type':'intel'},{'name':'void','type':'agility'}]
    fileObj = open(path,'w')
    fileObj.write("hero = " + pprint.pformat(hero) + '\n')
    fileObj.close
# Write the data without ppformat
    fileObj1 = open(path,'a')
    try :
         fileObj1.write("hero" + hero)
         print("It work")
    except TypeError :
         print("Type error , only concatenate with string ")
         print("This why u need ppformat to convert to string")
    fileObj1.close

# import the data
    print('')
    print('Importing the data........')
    import Hero
    print(Hero.hero) # print(hero variable in Hero.py)


def space():
    print('')
def new_note(n):
    if n == '1' :
        notefunction()
    elif n == '0' :
        notefunction0()
    elif n == '2' :
        notefunction2()
    elif  n == '3' :
        notefunction3()
    elif  n == '4' :
        notefunction4()
    elif  n == '5' :
        notefunction5()
    elif  n == '6' :
        notefunction6()
#Loop
while True :
    print("What example you want me to show ?")
    num = input()
    new_note(num)