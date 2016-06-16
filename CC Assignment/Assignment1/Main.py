import urllib
import os
import colorama
from datetime import datetime
from colorama import Fore, Back, Style

#########################################################################3
def Line_Compilation(f_line,Linenumber,characterposition,check,IFchecker):
    i = characterposition
    headerfile_character=""
    check = check
    coutdefinervalue=""
    typedefined=""
    ifstatmentchecker=""
    ifstatmentcheckervalue=""
    ifstatmentcheckervalue2=""

    f_line=f_line.lstrip()

    #print (line)
    if f_line[i] is '#':
                i = i + 1
                if f_line[i] is 'i':
                    i = i + 1
                    if f_line[i] is 'n':
                        i = i + 1
                        if f_line[i] is 'c':
                            i = i + 1
                            if f_line[i] is 'l':
                                i= i + 1
                                if f_line[i] is 'u':
                                    i = i + 1
                                    if f_line[i] is 'd':
                                        i = i + 1
                                        if f_line[i] is 'e':
                                            print ("There is an include library in it ..")
                                            i = i + 1
                                            if f_line[i] is '<' or '"':
                                                if f_line[i] is '<':
                                                    stoppingelement='>'
                                                    i += 1
                                                    while f_line[i] is not stoppingelement:
                                                        #headerfile_character.append(f_line[i])

                                                        headerfile_character += str(f_line[i])

                                                        i += 1
                                                    print (str(headerfile_character))

                                                    if headerfile_character =="iostream":

                                                        print ("Including the header file iostream")

                                                        headerfile1=open('C:\\Program Files (x86)\\CodeBlocks\\MinGW\\lib\\gcc\\mingw32\\4.7.1\\include\\c++\\iostream','r') #Reading the header file here!

                                                        headerfile1data=headerfile1.readlines()

                                                        for line in headerfile1data:

                                                            main_file.write(line+'\n')

                                                            #Another section of include!

                                                        #work on the repetition in a single line when needed Right here!!!

                                                    elif headerfile_character=="conio.h":
                                                        print("Including Conio.h header File")

                                                        headerfile2=open('C:\\Program Files (x86)\\CodeBlocks\\MinGW\\include\\conio.h','r') #reading form the second header FIle!.

                                                        headerfile2data=headerfile2.readlines()

                                                        for line in headerfile2data:

                                                            main_file.writelines(line)

                                                    elif headerfile_character=="io.h":

                                                        print("including another header file IO")

                                                        path="C:\\Program Files (x86)\\CodeBlocks\\MinGW\\lib\\gcc"

                                                        headerfile3 = open(path+'\\mingw32\\4.7.1\\include\\c++\\mingw32\\bits\\c++io.h','r') # for including the header file 3 path

                                                        headerfile3data = headerfile3.readlines()

                                                        for line in headerfile3data:

                                                            main_file.write(line+'\n')

                                                    elif headerfile_character=="stdlib":

                                                        print ("includding another header file to the directory")

                                                        path="C:\Program Files (x86)\CodeBlocks\MinGW\include\stdlib.h"

                                                        headerfile4=open(path,'r')

                                                        headerfile4data=headerfile4.readlines()

                                                        for line in headerfile4data:
                                                            main_file.write(line)
                                                    else :
                                                            print ('There HeaderFile Doesnt exist '+str(Linenumber)+' Error , cant locate the header file.. Terminating Sourcefile')
                                                            exit()
                                                elif f_line[i] is '"':

                                                        stoppingelement='"'

                                                        i +=1

                                                        while f_line[i] is not stoppingelement:
                                                        #headerfile_character.append(f_line[i])
                                                            headerfile_character += str(f_line[i])

                                                            i += 1
                                                        print (str(headerfile_character))

                                                        if headerfile_character =="iostream":

                                                            print ("Including the header file iostream")

                                                            headerfile1=open('C:\\Program Files (x86)\\CodeBlocks\\MinGW\\lib\\gcc\\mingw32\\4.7.1\\include\\c++\\iostream','r') #Reading the header file here!

                                                            headerfile1data=headerfile1.readlines()
                                                            for line in headerfile1data:

                                                                main_file.write(line+'\n')
                                                                #Another section of include!
                                                        elif headerfile_character=="conio.h":
                                                            print("Including Conio.h header File")

                                                            headerfile2=open('C:\\Program Files (x86)\\CodeBlocks\\MinGW\\include\\conio.h','r') #reading form the second header FIle!.

                                                            headerfile2data=headerfile2.readlines()

                                                            for line in headerfile2data:

                                                                main_file.writelines(line)
                                                        elif headerfile_character=="io.h":
                                                            print("including another header file IO")

                                                            path="C:\\Program Files (x86)\\CodeBlocks\\MinGW\\lib\\gcc"

                                                            headerfile3 = open(path+'\\mingw32\\4.7.1\\include\\c++\\mingw32\\bits\\c++io.h','r') # for including the header file 3 path

                                                            headerfile3data = headerfile3.readlines()

                                                            for line in headerfile3data:

                                                                main_file.write(line+'\n')
                                                        elif headerfile_character=="stdlib":
                                                            print ("includding another header file to the directory")

                                                            path="C:\Program Files (x86)\CodeBlocks\MinGW\include\stdlib.h"

                                                            headerfile4=open(path,'r')

                                                            headerfile4data=headerfile4.readlines()

                                                            for line in headerfile4data:
                                                                main_file.write(line)
                                                        else :
                                                            print ('There HeaderFile Doesnt exist '+linenumber+' Error , cant l;ocate the header file')
                                                            exit()
                                                else:
                                                    print 'There is an Error in the line: '+str(Linenumber)
                                                    exit()
                                            else:
                                                    print ('###There is an error in the header File at: '+str(linenumber)+' \n TIme is '+str(current_time))
                                                    exit()
                                        else:

                                            print ('###There is an error in the header File at : '+str(linenumber)+'\n TIme is '+str(current_time))
                                            exit()
                                    else:
                                        print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                        exit()
                                else:
                                    print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                    exit()
                            else:
                                print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                exit()
                        else:
                                print ('###There is an error in the header File at#### '+str(linenumber)+'\n TIme is '+str(current_time))
                                exit()
                    elif f_line[i] is 'f':
                        print ('Enterted the if statment') #here write the if statment
                        i += 1
                        IFchecker = 1
                        #main_file.write('#if'+' statments'+'\n') # Working on the statment
                        if f_line[i] is ' ':
                            i += 1
                            print ('if sstatmnet here!')
                            #main_file.write('if statment')
                            while f_line[i] is not ' ':
                                ifstatmentchecker += f_line[i]
                                i += 1
                            print (ifstatmentchecker)# Workingheerereere
                            main_file.write('if ('+ifstatmentchecker+')'+'{')
                            while f_line[i] is not ':':
                                i += 1
                                ifstatmentcheckervalue+=f_line[i]
                            print (ifstatmentcheckervalue)
                            i+=1
                            while f_line[i] is not ';':
                                ifstatmentcheckervalue2 += f_line[i]
                                i += 1
                            print (ifstatmentcheckervalue2)
                            main_file.write('cout<<'+ifstatmentcheckervalue+'}else'+'{cout<<'+ifstatmentcheckervalue2+';} \n')
                                #You are working here!!!!!
                                #it is here!!!
                elif f_line[i] is 'd':

                    i += 1

                    if f_line[i] is 'e':
                        i += 1

                        if f_line[i] is 'f':
                            i += 1

                            if f_line[i] is 'i':
                                i += 1

                                if f_line[i] is 'n':
                                    i += 1

                                    if f_line[i] is 'e':
                                        i += 1

                                        definername=""
                                        definernamevalue=""
                                        print 'There is a define statment here !!!!'

                                        if f_line[i] is ' ':
                                            i += 1

                                            while f_line[i] is not ' ':

                                                definername += f_line[i]

                                                i += 1

                                            definerlists_element.append(definername) ##Writing in to a list of define to keep track

                                            while f_line[i] is ' ':
                                                i += 1

                                                i += 1
                                            while f_line[i] is not '"':

                                                definernamevalue += f_line[i]    #Getting the value of the define word!

                                                i += 1

                                            definerlists_element_value.append(definernamevalue)

                                            if (type(definernamevalue)== int):  # to check the type of the definernamevalue

                                                typedefined=int

                                            elif (type(definernamevalue)== str):

                                                typedefined='string'

                                            elif (type(definernamevalue)==float):

                                                typedefined=float

                                            else:

                                                print ('Invalid Type defined at line '+Linenumber+ 'checked on time :'+current_time)

                                            main_file.write('Global '+typedefined+' '+str(definername)+' = '+str(definernamevalue)+'; \n')
                                            print 'done'

                                        #write here to include the extra things Brov! in define statment
                                    else:
                                        print ('###There is an error in the header File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                                        exit()
                                else:
                                    print ('###There is an error in the header File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                                    exit()
                            else:
                                print ('###There is an error in the header File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                                exit()
                        else:
                             print ('###There is an error in the header File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                             exit()
                    else:
                        print ('###There is an error in the header File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                        exit()
                elif f_line[i] is 'e':
                        i += 1

                        if f_line[i] is 'r':
                            i += 1

                            if f_line[i] is 'r':
                                i += 1
                                if f_line[i] is 'o':

                                    i += 1
                                    if f_line[i] is 'r':
                                        print ('An error defination here Write the statment here') #write the statment here!!!!
                                        ##ERROR Statment here!!!!!!
                        elif f_line[i] is 'n':
                            i += 1
                            if f_line[i] is 'd':
                                i += 1
                                if f_line[i] is 'i':
                                    i += 1
                                    if f_line[i] is 'f':
                                        i += 1

                                        if ifchecker== 1 and (f_line[i] is ' ' or f_line[i] is '\r'):
                                            main_file.write('#endif')

                elif f_line[i] is '#':
                    i +=1
                    '''if f_line[i] is '#':
                        print('Unknown Start of the # statment !!! Error at line number' +str(Linenumber)+' on position '+str(i))
                        exit()'''  # You need to work on it !
                    print ('There is a preprocessor in the line:0'+str(linenumber))
                    main_file.write('##'+' PreProcessorStatment'+'\n')
                    #Work needed to be done HERe!!!!! ## is the work (after completing it )
                else:
                    print('Unknown Start of the # statment !!! Error at line number' +str(Linenumber)+' on position '+i)
                    exit()

    elif f_line[i] is 'i':
        i += 1

        if f_line[i] is 'n':
            i += 1

            if f_line[i] is 't':
                i += 1

                if f_line[i] is ' ':
                    i += 1

                    if f_line[i] is 'm':
                        i += 1

                        if f_line[i] is 'a':
                            i += 1

                            if f_line[i] is 'i':
                                i += 1

                                if f_line[i] is 'n':
                                    i += 1

                                    if f_line[i] is '(':
                                        i += 1
                                        if f_line[i] is ')':

                                            # you just accessed the main part of the source file!
                                            main_file.write('int main()'+'\n')

                                            stackcheck[0]='int main()'
                                        else:

                                            print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))

                                            exit()

                                    else:
                                        print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                                        exit()
                                else:

                                    print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                                    exit()
                            else:

                                print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                                exit()
                        else:

                            print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                            exit()

                    else:
                        print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))

                        exit()
                else:

                    print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                    exit()
            else:

                print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
                exit()
            #You are working here    Working here!!!


        else:

            print ('###There is an error in main File at#### '+str(Linenumber)+'\n TIme is '+str(current_time))
            exit()
    elif f_line[i] is '{':
        main_file.write(f_line[i])

        i += 1

        if stackcheck[0] is 'int main()':

            while f_line[i] is not ';':
                main_file.write(f_line[i])
                i +=1
            main_file.write(';')

            if f_line[i] is '}':
                main_file.write('}')
            Check = 1


        else:
            print ('Invalid start of { with out main statment ERROR!!!!!!'+str(Linenumber)+'\n TIme is '+str(current_time))
            exit()
                                            ##You left here!!!
    elif f_line[i] is '}':
        print ('ending the statment!')

        if check == 1:
            main_file.write('}')
        else:
            print ('Invalid '+'} at line :'+str(linenumber))

    elif f_line[i] is '_':
        i += 1
        if f_line[i] is '_':
            i +=1
            if f_line[i] is 'd':
                i += 1
                if f_line[i] is 'a':
                    i += 1
                    if f_line[i] is 't':
                        i += 1
                        if f_line[i] is 'e':
                            i+=1
                            if f_line[i] is '_':
                                i +=1
                                if f_line[i] is '_':
                                    i+=1
                                    dateactual=current_time.date()
                                    main_file.write('cout<<'+str(dateactual)+';'+'\n')  # Convert in to date latter on!
                                else:
                                    print('THere is an error in the line number : '+str(linenumber)+'__date__ required')
                            else:
                                print('THere is an error in the line number : '+str(linenumber)+'__date__ required')
                        else:
                            print('THere is an error in the line number : '+str(linenumber)+'__date__ required')
                    else:
                        print('THere is an error in the line number : '+str(linenumber)+'__date__ required')
                else:
                    print('THere is an error in the line number : '+str(linenumber)+'__date__ required')
            elif f_line[i] is 't':
                i += 1
                if f_line[i] is 'i':
                    i += 1
                    if f_line[i] is 'm':
                        i += 1
                        if f_line[i] is 'e':
                            i += 1
                            if f_line[i] is '_':
                                i += 1
                                if f_line[i] is '_':
                                    i +=1
                                    timeactual=current_time.time()
                                    main_file.write('cout<<"'+str(timeactual)+'";'+'\n')
                                else:
                                    print('THere is an error in the line number : '+str(linenumber)+'__time__  required')
                            else:
                                print('THere is an error in the line number : '+str(linenumber)+'__time__  required')
                        else:
                            print('THere is an error in the line number : '+str(linenumber)+'__time__  required')
                    else:
                        print('THere is an error in the line number : '+str(linenumber)+'__time__  required')
                else:
                    print('THere is an error in the line number : '+str(linenumber)+'__time__ required')
            elif f_line[i] is 'l':
                i += 1
                if f_line[i] is 'i':
                    i +=1
                    if f_line[i] is 'n':
                        i += 1
                        if f_line[i] is 'e':
                            i += 1
                            if f_line[i] is '_':
                                i += 1
                                if f_line[i] is '_':
                                    i += 1
                                    currentline=Linenumber
                                    main_file.write('cout<<"'+str(currentline)+'";'+'\n')
                                else:
                                    print('THere is an error in the line number : '+str(linenumber)+' __line__ required')
                            else:
                                print('THere is an error in the line number : '+str(linenumber)+'  __line__ required')
                        else:
                            print('THere is an error in the line number : '+str(linenumber)+' __line__ required')
                    else:
                        print('THere is an error in the line number : '+str(linenumber)+' __line__ required')
                else:
                    print('THere is an error in the line number : '+str(linenumber)+' __line__ required')

            else:
                print('THere is an error in the line number : '+str(linenumber)+' Unknown command or fields')
    elif f_line[i] is 'c':
        i +=1
        if f_line[i] is 'o':
            i += 1
            if f_line[i] is 'u':
                i += 1
                if f_line[i] is 't':
                    i += 1
                    if f_line[i] is '<':
                        i += 1
                        if f_line[i] is '<':
                            i += 1
                            if f_line[i] is '"':
                                i+=1
                                #main_file.write('cout<<"')
                                # Here check the statment is such a way that \t and \n can be replaced
                                if f_line[i] is "/":
                                    i += 1
                                    if f_line[i] is 't':
                                        print ('a tab here!')
                                        main_file.write('cout<<"     ";'+'\n')
                                        i += 1
                                    elif f_line[i] is 'n':
                                        print ('A next Line is here')
                                        main_file.write('cout<<endl;')
                                        i += 1
                            else:
                                k=0
                                while f_line[i] is not ';':
                                    coutdefinervalue += f_line[i]
                                    i += 1
                                if coutdefinervalue in definerlists_element:   #You need to work here!!!
                                    print ('Detected a value here!')           # you need to work here in the detected value
                                    print (definerlists_element[0])            # you need to definerlists_element here!
                                    main_file.write('cout<<"'+definerlists_element_value[0]+'"')



                                    #You are working here
    else:
        print ('An Error Occured in the line  :'+str(Linenumber)+" couldn't locate the name at position "+str(i+1))
        exit()
    #Write the Else if statment by judging the main file!
try :

    curDir = os.getcwd()
    check = 0

    current_time=datetime.today()

    stackcheck=list()

    stackcheck.append('None')

    print ('Current time is '+str(current_time))

    print ('Current Directory:'+curDir)

    i = 0
    ifchecker=0

    definerlists_element=list()
    definerlists_element_value=list()

    main_file=open('Compiled1.cpp', 'w')

    check=bool(raw_input("Do you want to check the  message system it through Shafay's Compiler!(in python for c++)?"))

    if check is True:

        print ("ALL RIGHT RESERVED TO MUHAMMAD SHAFAY AMJAD 454-BSCS-13 PythonWorkspace")

        FILE=open('DATA.cpp', 'r')

        Main_codeFile=FILE.readlines()

        linenumber=0

        for line in Main_codeFile:

            linenumber += 1

            characterposition = 0

            Line_Compilation(line,linenumber,characterposition,check,ifchecker)

            print (str(linenumber)+' linenumber compiled'+'  on Time'+str(current_time))

        #Closing the File which is edited
        #main_file.close()
        #Write the code of the matching string and replacting the string
        #Final_filereplacment=open()
        main_file.close()

except ValueError:

    print ('An error occured while compiling this program !')

