import csv

translations = {}

with open('translations.csv', mode='r') as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
        english = line['English'].lower()
        spanish = line['Spanish'].lower()
        french = line['French'].lower()
        translations[english] = [spanish, french]
      

done = False

print('Type "done" at any time to exit')

while not done:
    word = input("What English word would you like to translate?")
    word = word.lower()
    if word == "done":
        done=True
    elif word in translations:
        print(translations[word])
    else:
        print("Word is not in translation dictionary")