# Note that not all the names are seperated into the the name list. This is because of the ' and (author_name_here)' 
# in breaking_down_list I've had a difficult time trying to seperate it out of the list of breaking_down_list
# So name has only the first several authors I'm hoping that this will work regardless of the last author

#Things to work on:
    # Figuring out how to get the last author into the name list




# This is all here so the functions can access them
lists = []
name = []
title = []
breaking_down = "" # this is here to turn the last entry in lists into a string
breaking_down_list = [] # this is to take the breaking_down str using the str split method and holds a list
file = open("research_docs","r")
lines = file.readlines()
for line in lines:
    line = line.strip()
    line = line.replace("\n","")
    splits = line.split((","))
    if ''  not in splits:
        lists.append(splits)


# This function cleans the data till there is only titles left and returns a list of titles
def clean_titles():
    for i in range(len(lists)):
         for j in range(len(lists[i])):
             if "and" in lists[i][j]:
                breaking_down = str(lists[i][j])
                down = breaking_down.split(".")
                breaking_down_list.append(down)
    for i in range(len(breaking_down_list)):
        for j in range(len(breaking_down_list[i])):
            if breaking_down_list[i][j].startswith(' “'):
                title.append(breaking_down_list[i][j])
    print(title)
    return title

 # This function cleans the data till there is only authors left   
def clean_author():
     for i in range(len(lists)):
         for j in range(len(lists[i])):
             if ' “' not in lists[i][j]:
                name.append(lists[i][j])
     print(name)
     return name

# clean_author()
# clean_titles()