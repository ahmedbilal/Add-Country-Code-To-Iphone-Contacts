"""
Author: Ahmed Bilal
Add Country Code to your iphone contacts file .vcf

Input:
    Filename
    Prefferred Country Code

Algorithm:
    Take all content from the file and load it into memory
    Replace All VOICE:0 with Country Code
    Replace All pref:0  with Country Code
    Reads weather a country code all ready exists in the phone no.
         If exists THEN Ignore
         ELSE add country code
"""
import os

# Function Definations
def GetNo(line):
    """ Return the Number or Email
       Arguments: line """
    if line.find("pref:") != -1:
        return line[line.find("pref:") + 5:]
    if line.find("VOICE:") != -1:
        return line[line.find("VOICE:") + 6:]
    
def hasCountryCode(no):
    """ Returns True if the number already has country code Otherwise False
        Arguments: number """
    if no != None:
        if (str(no[0:2]) == "00") or (str(no[0:1]) == "+"):
            return True
        else:
            return False

def addCountryCode(no,countryCode):
    """ Return Number with Country Code
        Arguments: Number, Country Code """
    return no.replace("0",countryCode,1)

def correctFileName(filename):
    newFileName = ""
    if filename == "":
        print("Please enter a filename!")
        return -1
    if filename[len(filename) - 4 : ] == ".vcf":
        newFileName = filename
    elif filename.find('.') == -1:
        newFileName = filename + ".vcf"
    elif filename[len(filename) - 4 : ] != ".vcf":
        print("Please enter a .vcf filename!")
        return -1

    if os.path.exists(newFileName) == True:
        return newFileName
    else:
        print("File Not Found!")
        return -1


# Input
filename = ""
lineLength = 0
while True:
    filename = correctFileName(input("Enter vcf filename: "))
    if filename != -1:
        break
    

countryCode = input("Enter preferred Country Code: ")
file = open(filename,'r')
newContent = [];

# Computation

for line in file:
    lineLength = len(line)
    number = str(GetNo(line))
    if number != None and line != None:
        if hasCountryCode(number) == False:
            newContent.append(line.replace(number, addCountryCode(number,countryCode),1))
        else:
            newContent.append(line)
    else:
        newContent.append(line)

# Output

outputFile = open('output.vcf','w')
outputFile.writelines(newContent)
outputFile.close();

print("Country Code added to Numbers Successfully\nOutput File:output.vcf")
input("Press Enter to Exit")
