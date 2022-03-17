with open("abusive_words.txt") as f:
    content = f.read()


content=content.replace("asshole","$#@#%^&*")

with open("abusive_words.txt","w") as f:
    content = f.write(content)