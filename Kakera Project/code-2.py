#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-03 10:21 UTC+0  #
#==============================================#

################################################
#                  DISCLAIMER                  #
#   This code is not good for 1 major reason   #
#     We are unable to see if the reactions    #
#     are on messages from the Mudae BOTs      #
#   So any reaction on any message is counted  #
#       and therefore this code will not       #
#      return a close to correct resault       #
################################################

# Imports
from collections import defaultdict as ddict

# Initialising a default dict to store the reactions
dct = ddict(int)

# List of files that the program will read through
# Should be .txt files
# We recommend compiling your data using DiscordChatExporter
files = [

# Dataset 1 
# 2021-03-15 22:00 UTC - 2021-03-31 07:26 UTC
# After Light kakera was added

#"resources-1/flood-1.txt",
#"resources-1/flood-2.txt",
#"resources-1/flood-3.txt",
#"resources-1/flood-4.txt",
#"resources-1/flood-5.txt",
#"resources-1/flood-6.txt",
#"resources-1/flood-7.txt"
#"resources-1/flood-8.txt",
#"resources-1/flood-9.txt",
#"resources-1/flood-husbando.txt",
#"resources-1/flood-waifu.txt",
#"resources-1/marry-roulette.txt"

# Dataset 2
# 2020-12-31 22:00 UTC - 2021-02-28 22:00 UTC
# Before Light kakera was added

"resources-2/flood-1.txt",
"resources-2/flood-2.txt",
"resources-2/flood-3.txt",
"resources-2/flood-4.txt",
"resources-2/flood-5.txt",
"resources-2/flood-6.txt",
"resources-2/flood-7.txt",
"resources-2/flood-8.txt",
"resources-2/flood-9.txt",
"resources-2/flood-husbando.txt",
"resources-2/flood-waifu.txt",
"resources-2/marry-roulette.txt"
]

# Function to filter the kakera reactions
def getReaction(l):
  if l =='kakeraP': 
    dct[l] += 1
    return True
  elif l =='kakera ': 
    dct[l] += 1
    return True
  elif l =='kakeraT': 
    dct[l] += 1
    return True
  elif l =='kakeraG': 
    dct[l] += 1
    return True
  elif l =='kakeraY': 
    dct[l] += 1
    return True
  elif l =='kakeraO': 
    dct[l] += 1
    return True
  elif l =='kakeraR': 
    dct[l] += 1
    return True
  elif l =='kakeraW': 
    dct[l] += 1
    return True
  elif l =='kakeraL': 
    dct[l] += 1
    return True
  else: 
    return False

sm = 0 # Counter of kakera

# Runs through all the desired files
for File in files:
  searchfile = open(File, "r") # Opening the next File, read only
  lastLine = '' # Initialising a last line to be able to find the reactions later
  
  # Reads through each line
  for line in searchfile:
    # Checking for kakera reactions
    if "kakera" in line and '{Reactions}' in lastLine:
      # Passes the reaction through the filter 
      # and adds to the counter if it passes the check
      if getReaction(line[0:7]): sm+=1
      #else: print(line, File) # Uncomment this to see what made it to the filter but failed to get through

    lastLine = line # Updates the lastLine variable

  searchfile.close() # Closing the read File so it's ready for the next one

# Prints the data disorganised
#for i in dct:
#  print(i, dct[i])

print(dct) # Prints out the raw data

# Prints the data in an organised format
print('\nPurple:', dct['kakeraP'], '\nBlue:', dct['kakera '], '\nTeal:', dct['kakeraT'], 
'\nGreen:', dct['kakeraG'], '\nYellow:', dct['kakeraY'], '\nOrange:', dct['kakeraO'], 
'\nRed:', dct['kakeraR'], '\nRainbow:', dct['kakeraW'], '\nLight:', dct['kakeraL'], 
'\nFor a total of', sm, 'kakera reactions')
