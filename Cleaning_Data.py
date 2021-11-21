# Note that not all the names are seperated into the the name list. This is because of the ' and (author_name_here)' 
# in breaking_down_list I've had a difficult time trying to seperate it out of the list of breaking_down_list
# So name has only the first several authors I'm hoping that this will work regardless of the last author

#Things to work on:
    # Figuring out how to get the last author into the name list




# This is all here so the functions can access them
lists = []
dict_lines = {}
# named = []
# name = []
# title = []
breaking_down = [] # this is here to turn the last entry in lists into a string
# breaking_down_list = [] # this is to take the breaking_down str using the str split method and holds a list
files = open("research_docs","r")

for lines in files:
    lists.append(lines)
first = []
for line in lists:
    first.append(line.splitlines())
for i in first:
    if '' not in i:
        breaking_down.append(i)


def organization():
    counter = 0
    holder = []
    for lin in breaking_down:
        counter = counter + 1
        line_names = "Line: "+str(counter)
        dict_lines[line_names] = lin
    for i in dict_lines.values():
        for j in range(len(i)):
          i[j] = i[j].replace(".","")
          i[j] = i[j].replace("“","")
          i[j] = i[j].replace("”","")
          i[j] = i[j].replace("and","")
          holder.append(i[j].split(","))
    pass_on = []
    for i in range(len(holder)):
            # for j in range(len(holder[i])):
        pass_on.append(holder[i])
    # print(pass_on)
    for lists in range(len(pass_on)):
        for l in dict_lines.values():
            dict_lines[l] = pass_on[lists]
    print(dict_lines)
    return dict_lines
# This is so I don't have to keep copying an pasting “ ”

# This function cleans the data till there is only titles left and returns a list of titles
def clean_titles():
    title = []
 
#  # This function cleans the data till there is only authors left   
def clean_author():
    cleaner = organization()
    for line in cleaner.values():
        print(line)
#      for i in range(len(lists)):
#          for j in range(len(lists[i])):
#              if ' “' not in lists[i][j]:
#                 named.append(lists[i][j])
#      for elem in named:
#          if elem.strip():
#              print(elem.strip())
#              name.append(elem)

#     #  print(name)
#      return name

# clean_author()
# clean_titles()
organization()