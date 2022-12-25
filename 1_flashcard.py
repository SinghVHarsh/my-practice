class FlashCard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def str(self):
        return self.word+' : '+self.meaning

flash=[]

print("Welcome to the flashcard game")
print("")
while(True):
    word = input("Enter the word : ")
    meaning = input("Enter the meaning : ")
    obj=FlashCard(word,meaning)
    flash.append(obj.str())
    myinput=int(input("press 0 if you do not want to add the flashcard: "))
    print("")
    if(myinput == 0):
        break

print("Here are your flashcards:")
print("")
for i in flash:
    print(i)
    print("")