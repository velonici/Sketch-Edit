# -*- coding: utf-8 -*-
"""Created on Fri Nov 27 00:33:27 2020
edited on Sunday Nov 29 00:13:12 2020
@author: Tracy Groller
edited by: Jesse Davidson
#image too sketch
"""
import cv2
import os

bl1 = int(25)
bl2 = int(25)

fileDir = input("Enter directory path:  ")

filelist = []

#Get list of files only, not folders
filelist = [f for f in os.listdir(fileDir) if os.path.isfile(os.path.join(fileDir, f))]

for eachFile in filelist:
    #Remove file extension for folder creation
    folderName = eachFile.rsplit('.')[0]
    newFolder = os.path.join(fileDir, folderName)
    #Create new folder for picture
    os.makedirs(newFolder, exist_ok=True)
    filename = eachFile
    file = os.path.join(fileDir, filename)
    img=cv2.imread(file)
    cv2.imshow('test', img)
    
    # Maintain output window until
    # user presses a key
    cv2.waitKey(0)
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    
    #Convert to greyscale
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    filename = folderName + ' gray.png'
    file = os.path.join(newFolder, filename)
    cv2.imwrite(file, gray)
    # Maintain output window until
    # user presses a key
    cv2.waitKey(0)
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    
    
    #invert image as a negative
    img_invert=cv2.bitwise_not(gray)
    cv2.imshow('invert', img_invert)
    filename = folderName + ' invert.png'
    file = os.path.join(newFolder, filename)
    cv2.imwrite(file, img_invert)
    # Maintain output window until
    # user presses a key
    cv2.waitKey(0)      
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    
    #Smoothe Image Gaussian blur
    gblur_img=cv2.GaussianBlur(img_invert,(bl1,bl2),sigmaX=0,sigmaY=0)
    cv2.imshow('blur', gblur_img)
    filename = folderName + ' smoothe.png'
    file = os.path.join(newFolder, filename)
    cv2.imwrite(file, gblur_img)
    # Maintain output window until
    # user presses a key
    cv2.waitKey(0)  
    # Destroying present windows on screen
    cv2.destroyAllWindows()
    
    #Dodge and Burn
    def dodge_img(x,y):
        return cv2.divide(x,255-y,scale=256)
    
    def burn_img(image, mask):
        return 255 - cv2.divide(255-image, 255-mask, scale=256)
    
    
    filename = folderName + ' sketch.png'   
    file = os.path.join(newFolder, filename)
    dodged_img=dodge_img(gray,gblur_img)
    final_img=burn_img(dodged_img,gblur_img)
    cv2.imshow('burn',final_img)
    cv2.imwrite(file, final_img)
    #Maintain output window until
    # user presses a key
    cv2.waitKey(0)
    # Destroying present windows on screen
    cv2.destroyAllWindows()


