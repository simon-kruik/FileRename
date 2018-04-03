#
#   Simon Kruik
#   Season Renamer
#   2018-04-03
#

import os
import re

#Get current directory
cwd = os.getcwd()
#Compile a regular expression to match
pattern = re.compile("\s[0-9]{2,3}")
while True:
    folder = input("Please enter the exact title of the folder, within which you wish to rename: ")
    titles_list = os.listdir(folder)
    print ("Files currently include: ")
    for title in  titles_list:
            print (title)
    season_number = input("What would you like to add before the episode number: ")
    for title in titles_list:
        ### Was checking what result was#print (pattern.search(title))
        ### Was checking what title was#print ("Comparing: " + title + "against (\s[0-9]{2,3})")
        if pattern.search(title):
            location = pattern.search(title)
            new_title = title[:location.start() + 1] + season_number + title[location.start() + 1:]
            os.rename(folder + "/" + title, folder + "/" + new_title)
            print ("Renaming: " + title + " to " + new_title)
        os.chdir(cwd)
    new_titles = os.listdir(folder)
    print ("New titles: ")
    for title in new_titles:
        print (title)

