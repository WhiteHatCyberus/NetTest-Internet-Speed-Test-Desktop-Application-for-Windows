'''
This is a project implementing a simple speedtest application using python
Author: WHCyberus (06/09/2022)
Windows version: 11
Python version:3.10
pip version: 22.2.2
'''
import time # to pause the screen for a given amount of time
import sys #to close the program in the end
import subprocess #to install necessary modules
print("Note: Make sure your system has Python3 installed! \n")
print("Installing required libraries..... may take a few moments")
subprocess.run(["python", "-m", "pip", "install", "speedtest-cli"]) # equivalent of 'pip install speedtest-cli' into cmd; installs speedtest module
import speedtest       
st=speedtest.Speedtest()    #initialising the speedtest module to var st
print("\n")
print("      Welcome to the Speedtest application \n") #Title
print("      --------------------------------------")
choice="Y"
while (choice =='Y' or choice == 'y'):
        print("\n") #Menu starts from here
        print("1. Download speed \n")
        print("2. Upload Speed \n")
        print("3.Exit \n")
        option = int(input("Your choice:"))
        if option == 1: #Download speed
            print("Checking.... May take a few seconds")
            down=st.download()/1000000 #conversion of bps(speed-cli default) to Mbps by dividing the value by 10^6
            print("Download speed:",round(down,2),"Mbps") #minimizing value to a precision of 2 decimal places
        elif option == 2: #Upload speed
            print("Checking.... May take a few seconds")
            up=st.upload()/1000000 #conversion of bps(speed-cli default) to Mbps by dividing the value by 10^6
            print("Upload Speed:",round(up,2),"Mbps") #minimizing value to a precision of 2 decimal places
        elif option == 3:
            choice = 'N'
            break
        else:
            print("Invalid choice!")
        print("\n")
        choice=input("Do you want to try again? (Y/N):")
print("\n")
print("Thank you for using this application!! \n")
print("Connect with me on LinkedIn: https://www.linkedin.com/in/whcyberus/ (for feedbacks/information) \n")
print("\n")
print("This window will close in",end=" ")
i=15    #countdown counter
while(i!=0):    #exits only at the 0th second
    print(i,end=" ") #prints current value of counter
    i=i-1       #decrements counter
    time.sleep(1) #pauses the screen for 1s for every iteration to give a countdown effect
sys.exit() #closes the window