import random
print("Hangman...Start your guessings!")
print("You have only 6 lives!")
word=["apple","pillow","holidays","mobile","keyboard"]
gen_word=random.choice(word)
len_word=len(gen_word)
bs=[]
for i in range(len_word):
    bs.append("_")
print(bs)
print()
wrong_guess=0
game_over=False
fin_word=""
while not game_over:
    let=input("Guess the letter: ")
    for pos in range(len_word):   #pos=1,2,3,4,5,6.....
        letter=gen_word[pos]
        if letter==let:
            bs[pos]=let
            print(bs)
            print("That's the correct guess!!!")
            print()
            fin_word+=let
            if len(fin_word)==len_word:
                print("You Won🤩🤩")

                game_over=True
    if let not in gen_word:
        print(bs)
        print("Wrong guess")
        print()
        wrong_guess+=1
        if wrong_guess>=6:
            game_over=True
            print("Game Over😵‍💫😵‍💫")



