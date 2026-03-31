# Bug count: ? (find them all)
# Topic: for loop, while loop, range(), string methods
# Give after: L06
#
# Scenario: A simple ATM that lets a user try a PIN up to 3 times,
#           then prints a star-masked version of the correct PIN,
#           and counts vowels in the account holder name.
#
# Expected output (if wrong PIN entered 3 times):
#   Attempt 1: wrong
#   Attempt 2: wrong
#   Attempt 3: wrong
#   Card blocked. Correct PIN was: ****
#   Account holder: Nilufar
#   Vowels in name: 3

correct_pin = "1234"
account_holder = "Nilufar"
attempts = 0
max_attempts = 3

while attempts <= max_attempts:  # BUG
    pin = input("Enter PIN: ")
    attempts =+ 1  # BUG
    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        print(f"Attempt {attempts}: wrong")
else:
    masked = "*" * len(correct_pin)
    print(f"Card blocked. Correct PIN was: {masked}")

vowels = "aeiouAEIOU"
vowel_count = 0
for letter in account_holder:
    if letter in vowels:
        vowel_count + 1  # BUG

print(f"Account holder: {account_holder}")
print(f"Vowels in name: {vowel_count}")

