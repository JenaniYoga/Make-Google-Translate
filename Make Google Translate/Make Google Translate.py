from googletrans import Translator
sen=str(input('Enter the Sentence:'))
k=Translator()
lang=str(input('Your Language:'))
convert=str(input('Which Language:'))
output=k.translate(sen,src=lang,dest=convert)
print(output.text)