#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-04 09:55 UTC+0  #
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
# Server: Mudae World
# After Light kakera was added
# Uses Emoji Names

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
# Server: Mudae World
# Before Light kakera was added
# Uses Emoji Names

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
# Servers in File Path
# After Light kakera was added
# Uses Emoji IDs

"resources-3/Mudae-World/flood-1.txt",
"resources-3/Mudae-World/flood-2.txt",
"resources-3/Mudae-World/flood-3.txt",
"resources-3/Mudae-World/flood-4.txt",
"resources-3/Mudae-World/flood-5.txt",
"resources-3/Mudae-World/flood-6.txt",
"resources-3/Mudae-World/flood-7.txt",
"resources-3/Mudae-World/flood-8.txt",
"resources-3/Mudae-World/flood-9.txt",
"resources-3/Mudae-World/flood-husbando.txt",
"resources-3/Mudae-World/flood-waifu.txt",
"resources-3/Mudae-World/marry-roulette.txt",
"resources-3/Rollsdae-World/rolls-1.txt",
"resources-3/Rollsdae-World/rolls-2.txt",
"resources-3/Rollsdae-World/rolls-3.txt",
"resources-3/Rollsdae-World/rolls-4.txt",
"resources-3/Rollsdae-World/rolls-5.txt",
"resources-3/Rollsdae-World/rolls-6.txt",
"resources-3/Rollsdae-World/rolls-7.txt",
"resources-3/Rollsdae-World/rolls-8.txt",
"resources-3/Rollsdae-World/rolls-9.txt",
"resources-3/Rollsdae-World/rolls-10.txt",
"resources-3/Rollsdae-World/rolls-11.txt",
"resources-3/Rollsdae-World/rolls-12.txt",
"resources-3/Rollsdae-World/rolls-13.txt",
"resources-3/Rollsdae-World/rolls-14.txt",
"resources-3/Rollsdae-World/rolls-15.txt",
"resources-3/Rollsdae-World/rolls-16.txt",
"resources-3/Rollsdae-World/rolls-17.txt",
"resources-3/Rollsdae-World/rolls-18.txt",
"resources-3/Rollsdae-World/rolls-oui-rolls.txt",
"resources-3/Rollsdae-World/rolls-sim-rolls.txt",
"resources-3/Rollsdae-World/rolls-yes-rolls.txt",
"resources-3/Shadbase/mudae-rolls-spam.txt",
"resources-3/Dyrus/waifu-gacha.txt"
]

# A dictionary of all the kakera emojis
# that the Mudae bots uses/used for reactions
# this lowers the reat of error a lot 
# since "nobody" has access to the emoji servers
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
# that the Mudae bots uses/used for reactions
#
# Added this since it lowers False Posives
# that appear when people react to messages
# using the Mudae World :kakera: emoji
#
# Since dictionaries don't hold their order
# and we need the Mudae World :kakera: amoji to
# be the last item checked to lower False positives
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
  
  # Reads through each line of the File and checks it for rections
  for line in searchfile:
    # Checks for reactions on messages with 'Belongs to '
    # This prevents user messages with kakera reactions from easily slipping through
    if '{Reactions}' in lastLine and 'Belongs to ' in lastLine3:
      # Checks if reaction is a kakera
      for i in kakeraList:
        if i in line:
          dct[i] += 1
          # Breaking here ensures that if there is a reaction 
          # using the Mudae World :kakera: emoji it wont get past
          # since it's the last element in out kakeraList
          # it also prevents
          break 
    
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

# Prints out the raw data
#print(dct)

# Prints the data in an organised format
print('\nPurple:', reactionValues['kakeraP'], '\nBlue:', reactionValues['kakera'], '\nTeal:', reactionValues['kakeraT'], 
'\nGreen:', reactionValues['kakeraG'], '\nYellow:', reactionValues['kakeraY'], '\nOrange:', reactionValues['kakeraO'], 
'\nRed:', reactionValues['kakeraR'], '\nRainbow:', reactionValues['kakeraW'], '\nLight:', reactionValues['kakeraL'], '\n\nA total of', cnt, 'kakera ractions')

print('\nSpawn chnances of kakera:\n\nPurple Spawn rate: ', format(round(100*reactionValues['kakeraP']/cnt, 6), '.4f'), '%', 
#'\nBlue Spawn rate: ', format(round(100*reactionValues['kakera']/cnt, 6), '.4f'), '%', 
#'\nTeal Spawn rate: ', format(round(100*reactionValues['kakeraT']/cnt, 6), '.4f'), '%', 
#'\nGreen Spawn rate: ', format(round(100*reactionValues['kakeraG']/cnt, 6), '.4f'), '%', 
#'\nYellow Spawn rate: ', format(round(100*reactionValues['kakeraY']/cnt, 6), '.4f'), '%', 
#'\nOrange Spawn rate: ', format(round(100*reactionValues['kakeraO']/cnt, 6), '.4f'), '%', 
'\nRed Spawn rate: ', format(round(100*reactionValues['kakeraR']/cnt, 6), '.4f'), '%', 
'\nRainbow Spawn rate: ', format(round(100*reactionValues['kakeraW']/cnt, 6), '.4f'), '%', 
'\nLight Spawn rate: ', format(round(100*reactionValues['kakeraL']/cnt, 6), '.4f'), '%', sep='')


print('\nCombined kakera due to Sapphire 4 and 3 keys:\n\nBlue & Yellow Spawn rate: ', format(round((100*reactionValues['kakera']+100*reactionValues['kakeraY'])/cnt, 6), '.4f'), '%', 
'\nTeal, Green & Orange Spawn rate: ', format(round((100*reactionValues['kakeraT']+100*reactionValues['kakeraG']+100*reactionValues['kakeraO'])/cnt, 6), '.4f'), '%', sep='')

