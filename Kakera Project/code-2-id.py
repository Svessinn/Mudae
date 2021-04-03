#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-03 16:27 UTC+0  #
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

#"resources-2/flood-1.txt",
#"resources-2/flood-2.txt",
#"resources-2/flood-3.txt",
#"resources-2/flood-4.txt",
#"resources-2/flood-5.txt",
#"resources-2/flood-6.txt",
#"resources-2/flood-7.txt",
#"resources-2/flood-8.txt",
#"resources-2/flood-9.txt",
#"resources-2/flood-husbando.txt",
#"resources-2/flood-waifu.txt",
#"resources-2/marry-roulette.txt"

# Dataset 3
# 2021-03-15 22:00 UTC - 2021-04-02 09:00 UTC
# After Light kakera was added

"resources-3/flood-1.txt",
"resources-3/flood-2.txt",
"resources-3/flood-3.txt",
"resources-3/flood-4.txt",
"resources-3/flood-5.txt",
"resources-3/flood-6.txt",
"resources-3/flood-7.txt",
"resources-3/flood-8.txt",
"resources-3/flood-9.txt",
"resources-3/flood-husbando.txt",
"resources-3/flood-waifu.txt",
"resources-3/marry-roulette.txt"
]

# A dictionary of all the kakera emojis
# that the Mudae bots use for reactions
# this lowers the reat of error a lot 
# since noboy has access to the emoji servers
kakeraDict = {
# ID:EmojiName
"609264156347990016":"kakeraP",
"609264226342797333":"kakeraP",
"469791929106956298":"kakera",
"605364503781310464":"kakera", #This is the :kakera: emoji in Mudae World (Biggest Failiure point)
"609264247645536276":"kakeraT",
"609264180851376132":"kakeraT",
"609264166381027329":"kakeraG",
"609264237780402228":"kakeraG",
"605124267574558720":"kakeraY",
"605112931168026629":"kakeraY",
"605112954391887888":"kakeraO",
"605124259018178560":"kakeraO",
"605124263917256836":"kakeraR",
"605112980295647242":"kakeraR",
"608192076286263297":"kakeraW",
"608193418698686465":"kakeraW",
"815961697918779422":"kakeraL"
}

# A dictionary of all the kakera emojis
# that the Mudae bots use for reactions
# added this since it lowers False Posives
# that appear when people react to messages
# using the Mudae World :kakera: emoji
kakeraList = [
"609264156347990016",
"609264226342797333",
"469791929106956298",
"609264247645536276",
"609264180851376132",
"609264166381027329",
"609264237780402228",
"605124267574558720",
"605112931168026629",
"605112954391887888",
"605124259018178560",
"605124263917256836",
"605112980295647242",
"608192076286263297",
"608193418698686465",
"815961697918779422",
"605364503781310464" #This is the :kakera: emoji in Mudae World (Biggest Failiure point)
]

cnt = 0 # Counter

# Runs through all the desired files
for File in files:
  searchfile = open(File, "r") # Opening the next File, read only
  lastLine = '' # Initialising a last line to be able to find the reactions later
  lastLine2 = '' #
  lastLine3 = '' # We and to be able to see two lines back for a check
  
  # Reads through each line
  for line in searchfile:
    k = True
    # Checks for reactions on messages with 'Belongs to '
    if '{Reactions}' in lastLine and 'Belongs to ' in lastLine3:
      # Checks if reaction is a kakera
      for i in kakeraList:
        if i in line:
          if k:
            dct[i] += 1
            k = False # k is set to false if a kakera reaction is detected

    lastLine3 = lastLine2 # Updates the lastLine3 variable
    lastLine2 = lastLine # Updates the lastLine2 variable
    lastLine = line # Updates the lastLine variable

  searchfile.close() # Closing the read File so it's ready for the next one

# ReactionValues is added here 
# so we can sum up the dufferent emoji ID resaults
# since on 2021-22-02 Mudae changed their kakera emojis
reactionValues = {
"kakeraP":0,
"kakera":0,
"kakeraT":0,
"kakeraG":0,
"kakeraY":0,
"kakeraO":0,
"kakeraR":0,
"kakeraW":0,
"kakeraL":0
}

# Goes throught the kakera IDs 
# and sums them up in the reactionValues dictionary
for i in kakeraDict: 
  reactionValues[kakeraDict[i]] += dct[i]
  cnt += dct[i]

print(dct) # Prints out the raw data

# Prints the data in an organised format
print('\nPurple:', reactionValues['kakeraP'], '\nBlue:', reactionValues['kakera'], '\nTeal:', reactionValues['kakeraT'], 
'\nGreen:', reactionValues['kakeraG'], '\nYellow:', reactionValues['kakeraY'], '\nOrange:', reactionValues['kakeraO'], 
'\nRed:', reactionValues['kakeraR'], '\nRainbow:', reactionValues['kakeraW'], '\nLight:', reactionValues['kakeraL'])
print('A total of', cnt, 'kakera ractions')
