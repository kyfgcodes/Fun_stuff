#Program to rename files

import os


folder = r'C:/Users/kfgwo/Music/Anime running'

for file_name in os.listdir(folder):

  source = file_name
  change = source.replace("[SPOTIFY-DOWNLOADER.COM]", "")
  
  
  os.rename(f'{folder}/{source}',f'{folder}/{change}' )

  
  print(change)








# print("All files renamed")

# print("New names are:")

# res = os.listdir(folder)

# print(res)