from random import seed,choice,randrange

WORDS = ["процессор",
        "катя",
        "миша",
        "петя",
        "коля",
        "дидзя"
]
seed()
words = choice(WORDS)
corect = words
ana = ''
while words: 
    pos = randrange(len(words))
    ana += words[pos]
    words = words[:pos] + words[pos+1:]
print( '''  
        Это анаграмма 


'''+ 'угадай слово: ',ana.upper())
item = input("VV SLOWO: ").casefold()

while item != corect and item != '':
    print("Не верно "+ " Попробуй ещё раз ")
    item = input("vvvv   ").casefold()
if corect == item:
    print("Молодец ")
input("Enter")


    



