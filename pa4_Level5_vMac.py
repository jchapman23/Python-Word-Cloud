#Josh Chapman
#4/1/2020
#This program takes user input .txt files and creates a word cloud out of the 
#30 most frequent words within that file
from time import sleep
from graphics import Image, Point, Rectangle, Text, Entry, color_rgb, GraphWin
from random import randrange
from buttonclass import Button
################################################################################
#This function is called to the tier() function to determine whether the 
#randomly generated points will 'collide' with any existing Point objects within  
#the xyVals list in drawCloud()
def isTooClose(x,y,inlist):
    #takes current length of list of Point objects
    length = len(inlist)

    #loop checks each iteration of the list to see if the points generated fall
    #wihtin 10 vertical and 20 horizontal pixels of the center of a Point in
    #the list
    #If so, it returns True to the while loop in tier() to reassign the x and y
    #values
    for i in range(length):
        if inlist[i].getY()-5 <= y <= inlist[i].getY()+5 and\
             inlist[i].getX()-10 <= x <= inlist[i].getX()+10:
            return True
################################################################################
#This function is called throughout the program to create a Text object and
#draw the object, setting it to be bold
#It returns the name of the object for use in the function it is called to
def drawText(pt,text,window):
    name = Text(pt, text)
    name.setStyle('bold')
    name.draw(window)
    return name
################################################################################
#This function is called to getInput() to draw Entry objects for user input of 
#.txt files and rgb parameters
#Sets width to 15, allows for prompt text if user desires
def drawEntry(pt,window,text=''):
    name = Entry(pt,15)
    name.draw(window)
    name.setText(text)
    return name
################################################################################
#This is a key function for sorting the list of unique words in order of their
#frequency within a tuple list
def freqSort(item):
    return item[1]
################################################################################
#This function is called to drawCloud() to draw an individual word from the list
#into the graphic window, based on the tier it was put in
def tier(tup,xylist,c1,c2,c3,constant,fontsize,window):
    #multiplies the color values entered by user in getInput() by a constant, and
    #changes based on their tier
    r = int(c1*constant)
    g = int(c2*constant)
    b = int(c3*constant)

    #creates random x and y coordinates using randrange, and tests whether
    #it is too close to any words generated by calling isTooClose()
    x = randrange(15,85)
    y = randrange(15,85)

    #runs until isTooClose() returns True, then Point(x,y) is added to the list,
    #and a text object is created using the word from the tuple object
    while isTooClose(x,y,xylist):
        x = randrange(15,85)
        y = randrange(15,85)

    #word is then assigned its color and font size as determined in drawCloud()
    #and draws it in the window
    xylist.append(Point(x,y))
    word = Text(Point(x,y),tup[0])
    word.setFill(color_rgb(r,g,b))
    word.setSize(fontsize)
    word.draw(window)
################################################################################
#This function is called to the main function to provide an Intro screen for the
#program
#It draws a background using an image, sets a title, an intro text block, and 
#prompt to continue to the next screen
#It enacts a small animation of the title, then undraws all objects when user
#moves to the next screen
def printIntro(gwin):
    #creates Image object to set a background for intro screen
    cloud = Image(Point(50,50),'cloud.gif')
    cloud.draw(gwin)

    #creates a white rectangle with a thicc border and draws it in the window
    #to serve as a backdrop for the prompt
    rect = Rectangle(Point(5,60), Point(95,40))
    rect.setFill('white')
    rect.setWidth(3)
    rect.draw(gwin)

    #creates Text object for title, set to 40 pt font
    #The font size was changed by editing zelle's graphics code from 36 to 48
    title = drawText(Point(50,90),'WordCloud',gwin)
    title.setFill('white')
    title.setSize(40)
    
    #creates a Text object for the intro text block, set to 14 pt font
    intro = drawText(Point(50,50), 'This program is a word cloud generator! '\
                 'By entering a text file\n\n'\
                 ' and choosing a color, you will be'\
                 ' able to see a cloud of 30 unique\n\nwords from the file,'\
                 ' where they are sorted by frequency in size and color!',gwin)
    intro.setSize(14)
    
    #creates Text object for the prompt to continue
    prompt = drawText(Point(50,10),'Click Anywhere to Continue',gwin)

    #while the user is not clicking the screen, the title animation runs
    while gwin.checkMouse() == None:
        title.setText('W o r d C l o u d')
        title.setText('W  o  r  d  C  l  o  u  d')
        title.setText('W   o   r   d   C   l   o   u   d')
        title.setText('W  o  r  d  C  l  o  u  d')
        title.setText('W o r d C l o u d')

    #undraws all objects except the background created for intro screen
    title.undraw()
    prompt.undraw()
    rect.undraw()
    intro.undraw()
################################################################################
#This function is called to the main function to get input from the user
#Draws Text and Entry objs to take the user input of a .txt file and 
#the r, g, and b values
#Creates a Button object to prompt user to enact .getText() on the Entry objects
#and change the graphic window
def getInput(gwin):

    #creates and draws a Rectangle to serve as a white backdrop to the program
    drop = Rectangle(Point(5,95),Point(95,5))
    drop.setFill('white')
    drop.setWidth(3)
    drop.draw(gwin)

    #creates Text objects to prompt users on where/what to enter
    prompt1 = drawText(Point(30,90),'Enter text file:',gwin)
    
    prompt2 = drawText(Point(30,70),'Enter a red value (0-255):',gwin)

    prompt3 = drawText(Point(30,60),'Enter a green value (0-255):',gwin)

    prompt4 = drawText(Point(30,50),'Enter a blue value (0-255):',gwin)

    prompt5 = drawText(Point(50,80),'You MUST fill out each entry box before '\
        'continuing\n\nIf you do not know r/g/b color '\
        'notation, try entering 255 for the color you\nwant, and'\
        ' 0 for the two you do not (or use the preset values).',gwin)
    prompt5.setStyle('italic')

    #creates Entry objects, setting optional text to prompt correct user input
    getfile = drawEntry(Point(60,90),gwin,text='asdf.txt')
    
    getcolor1 = drawEntry(Point(60,70),gwin,text='255')

    getcolor2 = drawEntry(Point(60,60),gwin,text='0')

    getcolor3 = drawEntry(Point(60,50),gwin,text='255')

    #creates a Button obect labeled 'Build Wordcloud'
    button = Button(gwin,Point(50,22.5),20,15,'Build Wordcloud')

    #waits for .isClicked() to return True and break loop
    pt = gwin.getMouse()
    while not(button.isClicked(pt)):
        pt = gwin.getMouse()

    #once loop is broken, filename and r/g/b values are taken from entry boxes
    filename = getfile.getText()
    r = int(getcolor1.getText())
    g = int(getcolor2.getText())
    b = int(getcolor3.getText())
    
    #all objects created are undrawn to clear window
    prompt1.undraw()
    prompt2.undraw()
    prompt3.undraw()
    prompt4.undraw()
    prompt5.undraw()
    getfile.undraw()
    getcolor1.undraw()
    getcolor2.undraw()
    getcolor3.undraw()
    button.undraw()

    #returns the name of the file and r/g/b values for use in genCloud()
    return filename, r, g, b   
################################################################################
#This function is called to the main function to organize the words from the
#.txt file into a dictionary containing the word and the frequency of which
#that word occurs
#It opens the file, removes unwanted characters and sorts for non-unique words,
#then records the frequency in a for loop
def genCloud(txtfile):

    #creates empty dicitonary to enter words into
    clouds = {}

    #opens the user input file, reads it into string, and sets all letters to
    #lowercase
    openfile = open(txtfile,'r',encoding="utf8")
    readfile = openfile.read().lower()

    #opens the stopwords.txt file to compare user file to
    stopwords = open('stopwords.txt','r',encoding="utf8")
    stops = stopwords.read().split('\n')
    
    #replaces each of these characters with a blank space in the user file
    for char in '!"@#$%^&*()/*-+.,?<>=\][}{|;:`~':
        readfile = readfile.replace(char, ' ')
    
    #splits file into a list of words
    words = readfile.split()

    #for each word in the user file
    for w in words:
        #if the word is not in the stopwords file
        if w not in stops:
            #then the dictionary adds one to the value of key w
            #this adds one to the frequency of the word
            clouds[w] = clouds.get(w,0) + 1

    #closes files, returns dictionary for use in drawCloud()
    openfile.close()
    stopwords.close()
    return clouds
################################################################################
#This function is called to the main function to draw the word cloud you've 
#heard so much about
#Changes the dictionary to a list of tuples, and sorts by frequency
#Edits the list down to top 30 words
#Takes the highest value and uses it as a max comparison
#Tiers out the words based on frequency in comparision to most frquently occuring
#word
def drawCloud(dictwords,rval,gval,bval,gwin):

    #creates empty list that will be hold Point objects of words in the cloud,
    #added by the tier() function
    xyVals = []

    #draws a text object to explain the color and font key to the user
    guide = drawText(Point(50,10),'(Larger Font Size and Brighter Color '\
                     'indiciate a Higher Frequency)',gwin)

    #changes dictionary into a list of the items
    cloud = list(dictwords.items())
    #sorts list by frequency
    cloud.sort(key=freqSort, reverse=True)

    #edits list down to top 30 words
    while len(cloud) > 30:
        cloud.pop()
    
    #pulls the word and the frequency value from the most frequent word
    word, high = cloud[0]

    #creates 4 values based on their relationship to the highest frequency
    a = high
    b = high*0.75
    c = high/2
    d = high/4

    #each word's frequency is compared to the high, and then falls under one
    #of four tiers where parameters for their font and color are assigned
    for pair in cloud:
        #tier 1: 100% color, 48 pt font
        if b < pair[1] <= a:
            tier(pair,xyVals,rval,gval,bval,1,48,gwin)
        #tier 2: 70% color, 36 pt font
        elif c < pair[1] <= b:
            tier(pair,xyVals,rval,gval,bval,.7,36,gwin)
        #tier 3: 50% color, 24 pt font
        elif d < pair[1] <= c:
            tier(pair,xyVals,rval,gval,bval,.5,24,gwin)
        #tier 4: 30% color, 12 pt font
        else:
            tier(pair,xyVals,rval,gval,bval,.3,12,gwin)
################################################################################
#This main function creates the graphic window that the user interacts with, and
#calls four funcitons to create a cloud of words from a user input text file
def main():
    
    win = GraphWin('wordcloud',800,800)
    win.setCoords(0,0,100,100)
    win.setBackground('white')
    
    printIntro(win)

    filename, r, g, b = getInput(win)

    cloudwords = genCloud(filename)

    drawCloud(cloudwords, r, g, b, win)
    
main()
