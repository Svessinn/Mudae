#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-03 10:33 UTC+0  #
#==============================================#

# I used this to get the list of all different kakera reaction emotes so I could go through them and see if they were used by the bot at some point

from collections import defaultdict as ddict
import json

files = [
"flood-7.json"
]

Mudae = "432610292342587392"
Mudamaid2 = "488711695640821760"

emotes = ddict(str)

dct = ddict(int)
for File in files:
  searchfile = open(File,)
  data = json.load(searchfile)

  for message in data['messages']:
    if message["author"]["id"] == Mudamaid2:
      if message["reactions"] != []:
        for i in message["reactions"]:
          dct[i["emoji"]["id"]] += 1
          emotes[i["emoji"]["id"]] = i["emoji"]["name"]

  searchfile.close()

for emote in emotes:
  if 'kakera' in emotes[emote]:
    print('<:'+str(emotes[emote])+':'+str(emote)+'>')


