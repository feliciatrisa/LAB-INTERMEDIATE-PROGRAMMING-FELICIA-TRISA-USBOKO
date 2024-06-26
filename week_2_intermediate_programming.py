# -*- coding: utf-8 -*-
"""Week 2_Intermediate Programming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1elGiosfz_13jX3zVS6EAartGoedFspmI
"""

mySecretWord = "Felicia"
lives = 6
used = ""

while (lives > 0):
    guess = input("Guess a letter in my secret word: ")
    if len(guess)!=1:
        print("Please guess only ONE letter!")
    else:
        if not guess.isalpha():
            print("Please guess a LETTER!")
        else:
            if guess.lower() in used:
                print("You've used this letter!")
            else:
                used = used + guess.lower()
                if guess.lower() in mySecretWord.lower():
                    print("You've guessed a letter.")
                else:
                    lives = lives - 1
                    print("Sorry wrong guess.")