from textblob import TextBlob

def autocorrect(text):
    return str(TextBlob(text).correct())

print(autocorrect("Ths is an exmple of autcorect"))