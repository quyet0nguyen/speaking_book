import csv
import os
from remove_accents import remove_accents

locations = []
with open('location_entity/_entity_.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    locations.append(lines[0].rstrip())


intents = os.listdir("location_entity")
intents.remove('_entity_.csv')


def read_file(file_name:str = ""):
  lines = []
  with open(file_name, mode ='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
      lines.append(line[0]) 

  return lines 

with open("results/nlu.yml", "w") as file1:
    # Writing data to a file

  file1.write("version: \"3.1\"\n")
  file1.write("\nnlu:")

  for intent in intents:
    intent_name = intent.split(".")[0]
    file1.write("\n\n")
    file1.write("- intent: "+str(intent_name))
    file1.write("\n  examples: |\n")

    intent_data = read_file("location_entity/" + intent)

    anchor_point = int(len(locations)/len(intent_data))
    print(intent)    

    iter = -1

    for i,location in enumerate(locations):
      if (i % anchor_point == 0):
        if iter < len(intent_data) - 1:
          iter += 1
        else:
          iter = 0
        text = intent_data[iter]
      
      if text.find('---') != -1:
        text1, text2 = text.split('---')
        file1.write("    "+ text1 + location + text2 + "\n")
        file1.write("    "+ text1.lower() + location.lower() + text2.lower() + "\n")
        file1.write("    "+ text1 + location.lower() + text2 + "\n")
      else:
        file1.write("    "+ text + "\n")

with open("results/rules.yml", "w") as file:
    file.write("version: \"3.1\"\n")
    file.write("\nrules:")

    for intent in intents:
      intent_name = intent.split(".")[0]
      file.write("\n\n")
      file.write("- rule: Rule to map \'" + str(intent_name) + "\' intent to \'action_" + str (intent_name) + "\' action. \n")
      file.write("  steps:\n")
      file.write("  - intent: " + str(intent_name) +"\n")
      file.write("  - action: " + "action_" + str(intent_name))
                 
with open("results/stories.yml", "w") as file:
    file.write("version: \"3.1\"\n")
    file.write("\nstories:")

    for intent in intents:
      intent_name = intent.split(".")[0]
      file.write("\n\n")
      file.write("- story: " + str(intent_name)+"\n")
      file.write("  steps:\n")
      file.write("  - intent: " + str(intent_name) + "\n")
      file.write("  - action: " + "action_" + str(intent_name))
