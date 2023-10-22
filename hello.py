# Ask user for their name
name = input("What's is your name? ").strip().title()

# Split user's name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first} {last}")
