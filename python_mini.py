import pywhatkit as py
import webbrowser as w
import pygame as pg
import time as t
import random as r
from PIL import Image
import speech_recognition as sr
import urllib.parse


# 1. News
def news():
    print("Opening News...")
    w.open("https://news.google.com")


# 2. Cartoons
def cartoons():
    print("Opening Cartoons...")
    w.open("https://www.youtube.com/results?search_query=cartoons")


# 3. Series
def series():
    print("Opening Series...")
    w.open("https://www.netflix.com")


# 4. Songs
def songs():
    name = input("Enter song name: ")
    py.playonyt(name)


# 5. Games
def game():
    print("Opening Games...🎮")
    print("Its a Number Guessing Game")

    count = 0   # ✅ keep outside loop

    for i in range(1, 11):
        print(f"\nRound {i}")

        answer = r.randint(1, 10)
        user_answer = int(input("Enter your answer (1-10): "))

        if user_answer == answer:
            print("Correct! 🎉")
            count += 1
        else:
            print("Oops! Wrong Answer.🥹")
            print("Correct answer is:", answer)

    print("\nGame Over 🎯")
    print("Your Score:", count, "/ 10")

    name = input("Enter your name: ")
    phone_no = input("Enter phone number(+91...): ")

    msg = f"Hiii {name}, your score in Number Guessing Game is {count}/10 🎮"

    try:
        py.sendwhatmsg_instantly(phone_no, msg)
    except:
        print("WhatsApp sending failed")

# 6. Movies
def movies():
    name = input("Enter movie: ")
    w.open(f"https://www.google.com/search?q={name}+movie")


# 7. Sports
def sports():
    print("Opening Sports...")
    w.open("https://www.espn.in")


# 8. YouTube
def youtube():
    w.open("https://www.youtube.com")


# 9. WhatsApp
def whatsapp():
    w.open("https://web.whatsapp.com")


# 10. Google Search
def google_search():
    q = input("Search: ")
    w.open(f"https://www.google.com/search?q={q}")


# 11. Weather
def weather():
    w.open("https://www.google.com/search?q=weather today")


# 12. Jokes
def jokes():
    w.open("https://www.rd.com/jokes")


# 13. Quotes
def quotes():
    w.open("https://www.brainyquote.com")


# 14. Timer
def timer():
    sec = int(input("Enter seconds: "))
    print("Timer started...")
    t.sleep(sec)
    print("Time up!")


# 15. Calculator
def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operator: ")

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        print(a / b)
    elif operator == "%":
        print(a % b)
    elif operator == "//":
        print(a // b)
    else:
        print("Please enter valid operator")


# 16. Alarm
def alarm():
    print("Alarm after 5 seconds...")
    t.sleep(5)
    print("Wake up!")


# 17. Instagram
def instagram():
    w.open("https://www.instagram.com")


# 18. Facebook
def facebook():
    w.open("https://www.facebook.com")


# 19. Coding
def coding():
    w.open("https://www.w3schools.com")


# 20. Maps
def maps():
    place = input("Enter place: ")
    w.open(f"https://www.google.com/maps/search/{place}")


# 21. Email
def email():
    w.open("https://mail.google.com")


# 22. Dictionary
def dictionary():
    word = input("Enter word: ")
    w.open(f"https://www.dictionary.com/browse/{word}")


# 23. Translate
def translate():
    text = input("Enter text: ")
    lang = input("Enter language: ")
    text = urllib.parse.quote(text)

    url = f"https://translate.google.com/?sl=auto&tl={lang}&text={text}&op=translate"
    w.open(url)


# 24. Voice Control
def voice_control():
    r1 = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak your song...")
        audio = r1.listen(source)

    try:
        text = r1.recognize_google(audio)
        print("You said:", text)
        py.playonyt(text)
    except:
        print("Voice not recognized")


# 25. ChatGPT
def chatgpt():
    w.open("https://chat.openai.com")


# Initialize pygame once
pg.init()
pg.mixer.init()
pg.mixer.music.load("C:\\Users\\ELCOT\\Downloads\\A-Broken-Heart.mp3")

while True:
    print("🎥>>>ENTERTAINMENT PLATFORM<<<🎬")
    pg.init()
    pg.mixer.init()
    pg.mixer.music.load("C:\\Users\\ELCOT\\Downloads\\A-Broken-Heart.mp3")
    pg.mixer.music.play()
    t.sleep(30)
    pg.mixer.music.stop()

    img = Image.open("C:\\Users\\ELCOT\\Downloads\\en.jpg")
    img = img.resize((500, 500))
    img.show()

    options = [
        "1. News 🗞️",
        "2. Cartoons 🎬",
        "3. Series 📺",
        "4. Songs 🎵",
        "5. Games 🎮",
        "6. Movies 🎥",
        "7. Sports ⚽",
        "8. YouTube ▶️",
        "9. WhatsApp 💬",
        "10. Google Search 🔍",
        "11. Weather 🌦️",
        "12. Jokes 😂",
        "13. Quotes 💡",
        "14. Timer ⏰",
        "15. Calculator ➕",
        "16. Alarm ⏳",
        "17. Instagram 📸",
        "18. Facebook 👍",
        "19. Coding 💻",
        "20. Maps 🗺️",
        "21. Email 📧",
        "22. Dictionary 📖",
        "23. Translate 🌐",
        "24. Voice Control 🎤",
        "25. ChatGPT 🤖",
        "26. Exit ❌"
    ]

    for i in options:
        print(i)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        news()
    elif choice == 2:
        cartoons()
    elif choice == 3:
        series()
    elif choice == 4:
        songs()
    elif choice == 5:
        game()
    elif choice == 6:
        movies()
    elif choice == 7:
        sports()
    elif choice == 8:
        youtube()
    elif choice == 9:
        whatsapp()
    elif choice == 10:
        google_search()
    elif choice == 11:
        weather()
    elif choice == 12:
        jokes()
    elif choice == 13:
        quotes()
    elif choice == 14:
        timer()
    elif choice == 15:
        calculator()
    elif choice == 16:
        alarm()
    elif choice == 17:
        instagram()
    elif choice == 18:
        facebook()
    elif choice == 19:
        coding()
    elif choice == 20:
        maps()
    elif choice == 21:
        email()
    elif choice == 22:
        dictionary()
    elif choice == 23:
        translate()
    elif choice == 24:
        voice_control()
    elif choice == 25:
        chatgpt()
    elif choice == 26:
        break
    else:
        print("Invalid choice")