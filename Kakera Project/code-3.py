#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-03 10:36 UTC+0  #
#==============================================#
#  This code is improvements to code-2.py and  #
#   reads JSON files which give us more info   #
#      on all the messages and reactions       #
#==============================================#

# Imports
from collections import defaultdict as ddict
import json

# List of files that the program will read through
# Should be a JSON file
# We recommend compiling your data using DiscordChatExporter
files = [
"flood-7.json"
]

# A dictionary of all the kakera emojis
# that the Mudae bots use for reactions
# this lowers the reat of error a lot 
# since noboy has access to the emoji servers
kakera = {
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

# Initialising a default dict to store the reactions
dct = ddict(int)

# IDs of the Mudae Bots that counld be used
# You can add more if you have a different 
# Maid/Butler in the server your data is from
MudaDict = {
"Mudae":"432610292342587392",
"Mudamaid2":"488711695640821760"
}

# Runs through all the desired files
for File in files:
  searchfile = open(File, "r") # Opening the next File, read only
  data = json.load(searchfile) # Compiles the JSON data so python can read it

  # Reads through all the message data (ignores the rest of the file)
  for message in data['messages']: 
    # Checking if the message is from our desired BOT 
    if message["author"]["id"] == MudaDict["Mudamaid2"]: # Change to another BOT if needed
      # Scans the message reactions (Ignores the message if there are no reactions
      if message["reactions"] != []:
        # Puts all the reaction emoji into the default dict
        for i in message["reactions"]:
          dct[i["emoji"]["id"]] += 1

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
for i in kakera: 
  reactionValues[kakera[i]] += dct[i]

# Prints the resaults in a good looking format
print("Purple:", reactionValues["kakeraP"], "\nBlue:", reactionValues["kakera"], "\nTeal:", reactionValues["kakeraT"], 
"\nGreen:", reactionValues["kakeraG"], "\nYellow:", reactionValues["kakeraY"], "\nOrange:", reactionValues["kakeraO"], 
"\nRed:", reactionValues["kakeraR"], "\nRainbow:", reactionValues["kakeraW"], "\nLight:", reactionValues["kakeraL"])
