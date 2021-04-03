#!/usr/bin/env python3

#==============================================#
#         Created By: Svess#8004               #
#  Last Modification:  2021-03-03 10:34 UTC+0  #
#==============================================#

# We used this to get a list of the reinbow kakera reactions so we could check if code-3 was working properly

from collections import defaultdict as ddict
import json

files = [
"flood-7.json"
]

Mudae = "432610292342587392"
Mudamaid2 = "488711695640821760"

lst = []

for File in files:
  searchfile = open(File,)
  data = json.load(searchfile)

  for message in data['messages']:
    if message["author"]["id"] == Mudamaid2:
      if message["reactions"] != []:
        for i in message["reactions"]:
          if i["emoji"]["name"] == 'kakeraW':
            lst.append((message['timestamp'], message['embeds'][0]['author']))

  searchfile.close()

print(*lst, sep="\n\n")
