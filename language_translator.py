from translate import Translator

# A simple language traslator using translate module.
inp = str(input("ENTER language1: ")) # From 
inp2 = str(input("ENTER language2: ")) # To
inp3 = str(input("ENTER TEXT: "))

translator = Translator(from_lang = inp, to_lang = inp2)
result = translator.translate(inp3)
print(result)