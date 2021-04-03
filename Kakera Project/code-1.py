#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-03 10:32 UTC+0  #
#==============================================#

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

"resources-1/flood-1.txt",
"resources-1/flood-2.txt",
"resources-1/flood-3.txt",
"resources-1/flood-4.txt",
"resources-1/flood-5.txt",
"resources-1/flood-6.txt",
"resources-1/flood-7.txt",
"resources-1/flood-8.txt",
"resources-1/flood-9.txt",
"resources-1/flood-husbando.txt",
"resources-1/flood-waifu.txt",
"resources-1/marry-roulette.txt"
]

sm = 0 # Counter for the number of Light kakera

# IDs of the Mudae Bots that counld be used
# You can add more if you have a different 
# Maid/Butler in the server your data is from
MudaDict = {
"Mudae":"Mudae#0807",
"Mudamaid2":"Mudamaid2#2147"
}

# Runs through all the desired files
for File in files:
  searchfile = open(File, "r") # Opening the next File, read only
  lastLine = '' # Initialising a last line to be able to find the reactions later

  # Reads through each line
  for line in searchfile:
    # Checkin if a Message by your specific MudaBOT is a response to a kakeraL reaction
    if ":kakeraL:breaks down into:" in line and MudaDict["Mudamaid2"] in lastLine:
      sm+=1 # Adds to the Light kakera counter
      # Strips the line into the kakera emotes and then
      # splits the line into a list of the kakera broken
      # down from the kakeraL reaction
      lst = list(line[26:-1].split(': =>')[0].split(':+:'))
      # Adding the kakera breakdown to the dict
      for i in lst:
        dct[i]+=1

    lastLine = line # Updates the lastLine variable

  searchfile.close() # Closing the read File so it's ready for the next one

# Summing the number of kakera that the
# Light kakera broke down into
dctsm = 0

for i in dct:
  dctsm += dct[i]

print(dct) # Prints out the raw data

print('\nPurple:', dct['kakeraP'], '\nBlue:', dct['kakera '], '\nTeal:', dct['kakeraT'], 
'\nGreen:', dct['kakeraG'], '\nYellow:', dct['kakeraY'], '\nOrange:', dct['kakeraO'], 
'\nRed:', dct['kakeraR'], '\nRainbow:', dct['kakeraW'], '\nFor a total of',
 dctsm, 'kakera\nBroken down from', sm, 'Light kakera')
