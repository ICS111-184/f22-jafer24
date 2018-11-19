# -*- coding: utf-8 -*-
"""
ICS 111 Intro to Computer Science I
Filename: f22_birthdate.py
@author: Joe Ferguson
github: jafer24
Created on 19NOV18

Create a program that check and resolves exceptions. 
Input name and birthday to dictionary, recall birthday and write to a file.
"""

import datetime
#strdate = '11-05-2018'
birthdays = {} #creates a dictionary named 'birthdays'
letter = 's' #made up value to initialize letter

def enterName(): #function to set item name and quantity of item
#    while(True):
    global name #needed to change global name
    global dtbday
    name = input('Please enter a name: ')
    for strdate in name:
#        name = input('Please enter a name: ')
        if name not in birthdays:
            try:
                strdate = input('Please enter their birthday: ') 
                #,'\'s birthday: ')#'Please enter', ame,
                dtbday = datetime.datetime.strptime(strdate, "%m-%d-%Y").date()
                birthdays[name] = dtbday
                #break
            except ValueError:
                print('ERROR: Please input the correct date format: mm-dd-yyyy ')
        else:
            print(name,'\'s birthday is', dtbday)
            break
    return name # and strdate


def write(): #This function creates a text document and writes the name and birthday
    nameHandle = open('friendsbdays.txt', 'w')
#    nameHandle.write(str(name))
    nameHandle.write(str(birthdays)) #writes dictionary
#    nameHandle.write(' ') #adds space between inputs
#    nameHandle.write(str(dtbday))
    nameHandle.close()
    print('Saved to file friendsbdays.txt')
    return

#while(True):

while letter != 'q': #q breaks out of loop, all other inputs continue

    print('\nFriends Birthday List!')
    print('\nCommand  Action')
    print('  n \t Enter a name')
    print('  w \t Write to file "friendsbdays.txt".')
    print('  q \t Quit')
    letter = input('\nPlease enter a single-letter command: ') #sets new letter 


    if letter == 'n':
        enterName()
    elif letter == 'w': #goes to write def
        write()
    elif letter == 'q': #quits the loop
        print('\nGoodbye.')
        break
    else: #continues the loop
        pass

#print(birthdays)
