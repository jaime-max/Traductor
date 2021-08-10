from googletrans import Translator
#translator = Translator()
#result = translator.translate('Mitä sinä teet')
#print(result.src)
#print(result.dest)
#print(result.origin)
#print(result.text)
#print(result.pronunciation)

translator = Translator()
result = translator.translate('Mikä on nimesi', src="https://Pharos.sh.com/text-translation-with-google-translate-api-in-python/fi", dest="https://Pharos.sh.com/text-translation-with-google-translate-api-in-python/fr")

print(result.src)
print(result.dest)
print(result.text)