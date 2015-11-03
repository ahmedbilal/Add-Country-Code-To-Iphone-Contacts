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
def GetPhoneNumber(line):
    """ Return the Telephone Number
       Arguments: line """
    if line.find("TEL") != -1:
        return line[line.rfind(":") + 1:]
    
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

    # If number begins with a single 0, get rid of it.
    # (This assumes that hasCountryCode has already been called to check for 00)
    if (no.find("0") == 0):
        no = no.replace("0","",1)

    return countryCode + no

def correctFileName(filename):
    newFileName = ""
	# Remove unnecessary quotes which could cause false negatives
    filename = filename.replace("\"", "")
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

def correctCountryCode(countryCode):
    # Ensure country code starts with either "00" or "+".
    if (countryCode.find("+") != 0 and countryCode.find("00") != 0):
        countryCode = "+" + countryCode
    return countryCode


# Input
filename = ""
while True:
    filename = correctFileName(input("Enter vcf filename: "))
    if filename != -1:
        break
    
while True:
    countryCode = input("Enter preferred Country Code: ")
    countryCode = correctCountryCode(countryCode)
    response = input("Country Code " + countryCode + " will be added to all numbers that don't already begin with + or 00. \n\nOK? (y/n)")
    if response == "y":
        break

file = open(filename,'r')
newContent = [];

# Computation

for line in file:
    if line != None:
        phoneNumber = GetPhoneNumber(line)

        if phoneNumber is None or hasCountryCode(phoneNumber):
            newContent.append(line)
        else:
            newNumber = addCountryCode(phoneNumber,countryCode)
            print("Old:\t" + phoneNumber)
            print("\tNew:\t" + newNumber + "\n")
            newContent.append(line.replace(phoneNumber, newNumber, 1))

# Output
outputFilename = filename.replace(".vcf", "-updated.vcf", 1)
outputFile = open(outputFilename,'w')
outputFile.writelines(newContent)
outputFile.close();

print("Country Code added to Numbers Successfully\nOutput File:" + outputFilename)
