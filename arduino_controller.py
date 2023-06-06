#!/usr/bin/env python3
import serial
import time

def sendInstruction(serial, instruction):
    serial.write(f"{instruction}\n".encode("utf-8"))
    while serial.in_waiting < 1:
        time.sleep(0.001)
    response = serial.readline().decode("utf-8").rstrip()
    if f"{instruction}" in response:
        if response[-1] == "+":
            value = serial.readline().decode("utf-8").rstrip()
            return 1, value
        else: return 1, "NOVALUE"
    else: return -1, "NOVALUE"

def jumpForward(serial, debug):
    error, value = sendInstruction(serial, 1)
    if error == 1:
        if debug:
            print("Jumping forward")
    elif error == -1:
        if debug:
            print("Error jumping forward")
        
def jumpBackward(serial, debug):
    error, value = sendInstruction(serial, 2)
    if error == 1:
        if debug:
            print("Jumping backward")
    elif error == -1:
        if debug:
            print("Error jumping backward")
        
def stopJumping(serial, debug):
    error, value = sendInstruction(serial, 3)
    if error == 1:
        if debug:
            print("Stopping jump")
    elif error == -1:
        if debug:
            print("Error stopping jump")

def turnRight(serial, debug):
    error, value = sendInstruction(serial, 4)
    if error == 1:
        if debug:
            print("Turning right")
    elif error == -1:
        if debug:
            print("Error turning right")
    
def turnLeft(serial, debug):
    error, value = sendInstruction(serial, 5)
    if error == 1:
        if debug:
            print("Turning left")
    elif error == -1:
        if debug:
            print("Error turning left")
        
def stopTurn(serial, debug):
    error, value = sendInstruction(serial, 6)
    if error == 1:
        if debug:
            print("Stopping turn")
    elif error == -1:
        if debug:
            print("Error stopping turn")
        
def printLCD(serial, text, debug):
    error, value = sendInstruction(serial, 7)
    if error == 1:
        if debug:
            print("Printing LCD")
        ser.write((text + "\n").encode("utf-8"))
    elif error == -1:
        if debug:
            print("Error printing LCD")
        
def getDistance(serial, debug):
    error, value = sendInstruction(serial, 8)
    if error == 1:
        if debug:
            print("Getting distance")
    elif error == -1:
        if debug:
            print("Error getting distance")
    return value
    
def getCompass(serial, debug):
    error, value = sendInstruction(serial, 9)
    if error == 1:
        if debug:
            print("Getting compass")
    elif error == -1:
        if debug:
            print("Error getting compass")
    return value

def getJoystickX(serial, debug):
    error, value = sendInstruction(serial, 11)
    if error == 1:
        if debug:
            print("Getting joystick x")
    elif error == -1:
        if debug:
            print("Error getting joystick x")
    return value

def getJoystickY(serial, debug):
    error, value = sendInstruction(serial, 12)
    if error == 1:
        if debug:
            print("Getting joystick y")
    elif error == -1:
        if debug:
            print("Error getting joystick y")
    return value
        
def openSerial():
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1.0) #crear l'objecte serial
    time.sleep(3) #quan obrim el serial l'arduino es reinicia, esperem 3 segons
    ser.reset_input_buffer() #borrem el buffer
    print("Serial Open")
    return ser
