import csv

def intro():
    print('********************************************************************************************')
    print('Welcome to the Spanish and French translator app.\n\nPlease enter an English word and press the "Enter" key.')
    print('\nType "done" at any time to exit\n')
    print('********************************************************************************************')

    
def exit():
    print('\nThanks for using the translator app.  Have a great day!')
    
translations = {}

with open('translations.csv', mode='r') as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
        english = line['English'].lower()
        spanish = line['Spanish'].lower()
        french = line['French'].lower()
        translations[english] = [spanish, french]
      

done = False

#print('Type "done" at any time to exit')

intro()
while not done:
    word = input("\nWhat English word would you like to translate? ")
    word = word.lower()
    if word == "done":
        done=True
        exit()
    elif word in translations:
        #print(translations[word])
        print(f'\nSPANISH:{translations[word][0]}')
        print(f'\nFRENCH:{translations[word][1]}')
    else:
        print("Word is not in translation dictionary")