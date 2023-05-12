import csv
import os

intents = os.listdir("location_entity")
intents.remove('_entity_.csv')

labels = []

for intent in intents:
    labels.append(intent.split(".")[0])

for label in labels:
    print("- " + label+":")
    print("    use_entities:")
    print("      - location")

print("------------------")

for label in labels:
    print("- " + "action_" + label)