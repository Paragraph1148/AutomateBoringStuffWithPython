import pyperclip

text = pyperclip.paste()
alt_text = ''
make_uppercase = False
for char in text:
    if make_uppercase:
        alt_text += char.upper()
    else:
        alt_text += char.lower()
    make_uppercase = not make_uppercase

print(alt_text)
pyperclip.copy(alt_text)