import os
import pyttsx3
import time
import random
import winsound
import pip


def countdown(n):   #setting time
    while n > 0:
        n = n - 1
    if n ==0:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
greet = ['hi', 'hello', 'yo', 'bonjour', 'holaa', 'salaam' ,'namaste']
sayingbye = ['Goodbye..', 'Adios..', 'Take care....', 'See yaa...', 'Aastala Vista']
donno = ['Come again', "I don't get it",'Speak up' , 'Say something!' , 'Yes?' , "What's your command my lord"]
blus = ['So sweet of you..., Thankyou!', 'Thanks a lot', 'That means a lot, thanks']
engine = pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)
engine.setProperty('rate',180)  #180 words per minute
engine.setProperty('volume',0.9)
print("Hi...!")
engine.say("Hi...!")
engine.runAndWait();
print('''
How would you like your input?
Press 1 for text commands
Press 2 for voice commands
''')
engine.say("How would you like your input?")
engine.runAndWait();
inputSource= input()
if(inputSource == "1"):
    print("Lets type...")
    engine.say("Lets type...")
    engine.runAndWait();
elif(inputSource == "2"):
    print("This is a pro version feature")
    engine.say("This is a pro version feature")
    engine.runAndWait();
else:
    print("INVALID INPUT")
while 1>0:

    # Record Audio
    try:
        if(inputSource == "1"):
            i=input().lower()
        else:
            print("INVALID INPUT")
        # if i=='exit' or i=='stop' or i=='bye' or i=='quit':
        if ('exit' in i) or ('stop' in i) or ('bye' in i):
            a1=random.choice(sayingbye)
            print(a1)
            engine.say(a1)
            engine.runAndWait();
            break
        else:
            
            if ('hello' in i) or ('hi' in i) or ('hey' in i):
                a2=random.choice(greet)
                print(a2)
                engine.say(a2)
                engine.runAndWait();
            elif ('who' in i) and ('are' in i):
                print("I am bubbles. My creator is Bhawani")
                engine.say("I am bubbles. My creator is Bhawani")
                engine.runAndWait();
            elif ('how' in i) and ('are' in i) and ('you' in i):
                print("Everything is Awesome, so am i.")
                engine.say("Everything is Awesome, so am i.")
                engine.runAndWait();
            elif ('from' in i) and ('bit' in i) and ('college' in i):
                print("It's my creators college")
                engine.say("It's my creators college")
                engine.runAndWait();
            elif (('i' in i) and ('want' in i)) or (('you' in i) and ('do' in i)):
                print("Dont expect much from me, I am in Beta stage")
                engine.say("Dont expect much from me, I am in Beta stage")
                engine.runAndWait();
            elif ("didn't" in i) or ('did not' in i):
                print("Oh don't deny you liar")
                engine.say("Oh don't deny you liar, hahahah")
                engine.runAndWait();
            elif ('you' in i) and (('awesome' in i) or ('great' in i) or ('smart' in i) or ('intelligent' in i)):
                a4=random.choice(blus)
                print(a4)
                engine.say(a4)
                engine.runAndWait();
            elif ('what' in i) or ("what's" in i):
                if ('time' in i):
                    a5=time.strftime("%I:%M:%S")
                    print(a5)
                    engine.say(a5)
                    engine.runAndWait();
                elif ('date' in i):
                    a6=time.strftime("%d/%m/%Y")
                    print(a6)
                    engine.say(a6)
                    engine.runAndWait(); 
            
                # if userInput[j].lower()=='hello' or userInput[j].lower()=='hi':
                #     a2=random.choice(greet)
                #     print(a2)
                #     engine.say(a2)
                #     engine.runAndWait();
                # elif userInput[j].lower()=='who':
                #     if (userInput[j+1].lower()=='are') and (userInput[j+2].lower()=='you'):
                #         print("I am bubbles. My creator is Bhawani")
                #         engine.say("I am bubbles. My creator is Bhawani")
                #         engine.runAndWait();
                # if userInput[j].lower()=='how':
                #     if (userInput[j+1].lower()=='are') and (userInput[j+2].lower()=='you'):
                #         print("Everything is Awesome, so am i.")
                #         engine.say("Everything is Awesome, so am i.")
                #         engine.runAndWait();
            userInput=i.split( )
            lengthOfInput=len(userInput)
            for j in range(0,lengthOfInput):
                if userInput[j].lower()=='my':
                    if userInput[j+1]=='name':
                        if userInput[j+3].lower()=='sam':
                            print("Hello Sam, It's great to see you...i am sure ur smiling while looking at this, how are you?")
                            engine.say("Hello Sam, It's great to see you...i am sure ur smiling while looking at this, how are you?")
                            engine.runAndWait();

                        elif userInput[j+3].lower()=='jack':
                            print('Hello DAD, how are you?')
                            engine.say('Hello DAD, how are you?')
                            engine.runAndWait();

                        elif userInput[j+3].lower()=='duffy':
                            print('Hello MOM, how are you?')
                            engine.say('Hello MOM, how are you?')
                            engine.runAndWait();

                        elif userInput[j+3].lower()=='tuffy':
                            print('Hello sis, how are you?')
                            engine.say('Hello sis, how are you?')
                            engine.runAndWait();
                        else:
                            print("Hello",userInput[j+3])
                            engine.say("Hello"+userInput[j+3])
                            engine.runAndWait();
                elif userInput[j].lower()=='i':
                    if userInput[j+1].lower()=='am':
                        print("Hello",userInput[j+2])
                        engine.say("Hello"+userInput[j+2])
                        engine.runAndWait();
                elif userInput[j].lower()=='start':
                    print("Starting...",userInput[j+1])
                    engine.say("Starting...",userInput[j+1])
                    engine.runAndWait();
                    #os.system(userInput[j+1])
                    if userInput[j+1].lower()=='calculator':
                        os.system('start calc.exe')
                    elif userInput[j+1].lower()=='command' and userInput[j+2].lower()=='prompt':
                        os.system('start cmd')
                    elif userInput[j+1].lower()=='vlc':
                        os.system('start vlc.exe')
                    elif userInput[j+1].lower()=='spotify':
                        os.system('start spotify.exe')
                    #elif userInput[j+1].lower()=='i' and userInput[j+2].lower()=='heart':
                        #os.system('start iHeartRadio')
                    elif userInput[j+1].lower()=='chrome':
                        os.system('start chrome.exe')
                    elif userInput[j+1].lower()=='saavn' or userInput[j+1].lower()=='sawan':
                        os.system('start saavn')      
                elif userInput[j].lower()=='set' and userInput[j+2].lower()=='alarm':
                    print('Setting an alarm for',userInput[j+4],'seconds')
                    engine.say('Setting an alarm for given seconds')
                    engine.runAndWait();
                    countdown(int(userInput[j+4])*100)
                 
                #web development commands
                elif (userInput[j].lower()=='create' or userInput[j].lower()=='make') and (userInput[j+1].lower()=='web' or userInput[j+1].lower()=='a') and (userInput[j+2].lower()=='web' or userInput[j+2].lower()=='app') :
                    file = open("project.html","w+")
                    file.write("<div> \n <h1>Hello World</h1> \n </div>")
                    file.close()
                    print("Program created")
                    engine.say("Program created")
                    engine.runAndWait();
                elif (userInput[j].lower()=='open') and (userInput[j+1].lower()=='the' or userInput[j+1].lower()=='project') and (userInput[j+2].lower()=='project' or userInput[j+2].lower()=='file') :
                    os.system('start project.html')
                    print("File opened")
                    engine.say("File opened")
                    engine.runAndWait();

                elif (userInput[j].lower()=='add' and userInput[j+1].lower()=='text'):
                    file = open("project.html", "r")
                    list_of_lines = file.readlines()
                    for x in range(2,len(userInput)):
                        list_of_lines.insert(x-1,userInput[x] + " ")
                    file = open("project.html", "w")
                    file.writelines(list_of_lines)
                    file.close()
                    print("Text changed")
                    engine.say("Text changed")
                    engine.runAndWait();
                
    except sr.UnknownValueError:
        a3=random.choice(donno)
        print(a3)
        engine.say(a3)
        engine.runAndWait();
    except sr.RequestError as e:
        print("Oops, there was an error; {0}".format(e))
        engine.say("Oops, there was an error; {0}".format(e))
        engine.runAndWait();

                       
                        
                
                        


            
        
