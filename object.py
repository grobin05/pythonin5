class Person:
    def speak(self, words):
        print(words)
    def __init__(self):
        print("New Person")

p = Person()
p.speak("tree flowers")

class Francis(Person):
    def __init__(self):
        super().__init__()
        print("My name is Francis")

f = Francis()
f.speak("garbage can")
