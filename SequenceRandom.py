#Import needed libraries
import json     #to process JSON structures
import socket   #to communicate with MAX using UDP
import time     #to use the time delay
import random   #to use ramdom choice

#Initialize variables to communicate with MAX
MAX_UDP_IP = "127.0.0.1"     #IP address where MAX is running
MAX_UDP_PORT = 7404     #port on MAX patch ansering to UDP requests

#Initialize variables that control the face on MAX
MAX_Facial_Expression_Neutral = "50 50 50 50 50 50 50 0 0 50 60 40 50"
MAX_Facial_Expression_Happy = "60 50 60 50 40 40 80 0 0 100 100 0 75"
MAX_Facial_Expression_Stern = "40 100 40 100 66 66 30 0 0 50 0 30 25"
MAX_Facial_Expression_Angry = "0 100 0 100 40 40 0 0 0 30 0 60 25"
MAX_Facial_Expression_Disgusted = "20 100 100 35 70 40 50 0 0 0 0 68 47"
MAX_Facial_Expression_Surprised = "65 0 65 0 0 0 50 0 0 22 50 85 92"
MAX_Facial_Expression_Afraid = "100 60 100 60 0 0 50 0 0 0 0 77 62"
MAX_Facial_Expression_Sad = "100 100 100 100 45 45 50 0 0 0 40 100 0"
MAX_Facial_Expression_Tired = "70 90 70 90 80 80 50 0 0 50 0 40 50"



#Function to call MAX
def callMAX(outputToMAX, MAX_UDP_IP, MAX_UDP_PORT):
    #using try and except to possibly detect errors
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(bytes(outputToMAX, "utf-8"), (MAX_UDP_IP, MAX_UDP_PORT))
    except:
        print("It was not possible to communicate with MAX")
    return



#Function to initialize values to send to MAX based on the analysis of the text
def getMAXValues(value):
    #initialize with a neutral value in case there is no correspondence between the Wtason API and MAX
    MAXValue = MAX_Facial_Expression_Neutral
    #Prepare values to send to MAX based on the tone word expressions choosen
    if value == "Neutral":
        MAXValue = MAX_Facial_Expression_Neutral
    if value == "Happy":
        MAXValue = MAX_Facial_Expression_Happy
    if value == "Stern":
        MAXValue = MAX_Facial_Expression_Stern
    if value == "Angry":
        MAXValue = MAX_Facial_Expression_Angry
    if value == "Disgusted":
        MAXValue = MAX_Facial_Expression_Disgusted
    if value == "Surprised":
        MAXValue = MAX_Facial_Expression_Surprised
    if value == "Afraid":
        MAXValue = MAX_Facial_Expression_Afraid
    if value == "Sad":
        MAXValue = MAX_Facial_Expression_Sad
    if value == "Tired":
        MAXValue = MAX_Facial_Expression_Tired
    return(MAXValue)



#MAIN PROGRAM
text1 = ""
while text1!="EXIT":
    #Define the pharse to pick words randomly
    phrase=["Neutral", "Happy", "Stern", "Angry", "Disgusted", "Surprised", "Afraid", "Sad", "Tired"]
    text1 = random.choice(phrase)
    text2 = random.choice(phrase)
    text3 = random.choice(phrase)
    while text1 == text2:
        text2 = random.choice(phrase)
    print("I have choosen ", text1, ",", text2, " and ", text3, "to modify the face")
    Continue = input("Do you want to continue? [Y/N]: ")
    if Continue=="N":
        break
    #send first 13 values  to MAX
    callMAX(getMAXValues(text1), MAX_UDP_IP, MAX_UDP_PORT)
    #defines the number of seconds to wait before sending new values to MAX
    time.sleep(6)
    #send second 13 values to MAX
    callMAX(getMAXValues(text2), MAX_UDP_IP, MAX_UDP_PORT)
    
    time.sleep(6)
    
    callMAX(getMAXValues(text3), MAX_UDP_IP, MAX_UDP_PORT)