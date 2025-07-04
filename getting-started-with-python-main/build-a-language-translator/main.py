translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento"
}

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

