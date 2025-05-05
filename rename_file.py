#Program to rename files

import os

#Add your folder path here
folder = r'/home/kyle/Documents/Test'

ep_counter = 1;
for file_name in os.listdir(folder):


  source = file_name
  change = source.replace(file_name, f"Ep {ep_counter}")
  
  
  os.rename(f'{folder}/{source}',f'{folder}/{change}' )

  ep_counter += 1;
  print(change)








# print("All files renamed")

# print("New names are:")

# res = os.listdir(folder)

# print(res)
