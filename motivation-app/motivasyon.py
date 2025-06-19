import datetime
import random
import json
import os

# Sabit söz listesi (istersen bunu dışarıdan JSON olarak da alabiliriz)
default_quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "You are capable of amazing things.",
    "Believe you can and you're halfway there.",
    "Push yourself, because no one else is going to do it for you.",
    "Do something today that your future self will thank you for."
]

QUOTE_FILE = "quotes.json"

def load_quotes():
    if os.path.exists(QUOTE_FILE):
        with open(QUOTE_FILE, "r") as file:
            return json.load(file)
    else:
        return default_quotes

def save_quotes(quotes):
    with open(QUOTE_FILE, "w") as file:
        json.dump(quotes, file, indent=4)

def get_quote_of_the_day(quotes):
    day_number = datetime.datetime.now().timetuple().tm_yday
    index = day_number % len(quotes)
    return quotes[index]

def add_custom_quote(quotes):
    new_quote = input("Enter your motivational quote: ").strip()
    if new_quote:
        quotes.append(new_quote)
        save_quotes(quotes)
        print("Quote added successfully!")

def main():
    quotes = load_quotes()
    print("\n🌟 Today's Motivational Quote 🌟")
    print("----------------------------------")
    print(get_quote_of_the_day(quotes))
    
    while True:
        choice = input("\nWant another random quote? (y/n) or (a)dd your own: ").lower()
        if choice == "y":
            print("\n💬", random.choice(quotes))
        elif choice == "a":
            add_custom_quote(quotes)
        elif choice == "n":
            print("Stay motivated! 💪")
            break
        else:
            print("Please enter y, n or a.")

if __name__ == "__main__":
    main()
