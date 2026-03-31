# Bug count: ? (find them all)
# Topic: RegEx, JSON, datetime
# Give after: L09
#
# Scenario: A contact form validator and data archiver for a business app.
#           Validates phone and email, then saves valid contacts as JSON
#           with a timestamp.
#
# Expected output:
#   +998901234567 → valid phone
#   +99891abc5678 → invalid phone
#   user@example.com → valid email
#   user@@example.com → invalid email
#   Saved 2 valid contacts to contacts.json
#   Archived at: 2026-03-31  (date only, no time)

import re
import json
from datetime import datetime

contacts = [
    {"name": "Sardor", "phone": "+998901234567", "email": "sardor@mail.com"},
    {"name": "Broken", "phone": "+99891abc5678", "email": "user@@example.com"},
    {"name": "Nilufar", "phone": "+998997654321", "email": "nilufar@mail.com"},
]

phone_pattern = re.compile(r"^\+998[0-9]{9}$")
email_pattern = re.compile(r"^[\w.-]+@[\w.-]+\.\w{2,}$")

valid_contacts = []

for contact in contacts:
    phone_ok = phone_pattern.match(contact["phone"])
    email_ok = email_pattern.match(contact["email"])

    print(f"{contact['phone']} → {'valid phone' if phone_ok else 'invalid phone'}")
    print(f"{contact['email']} → {'valid email' if email_ok else 'invalid email'}")

    if phone_ok and email_ok:
        valid_contacts.append(contact)

# Add archive timestamp
archive = {
    "archived_at": datetime.now().strftime("%Y-%m-%d"),
    "contacts": valid_contacts
}

with open("contacts.json", "w") as f:
    json.dump(archive, f)  # BUG — should be indented for readability, but not a crash bug
    # The real BUG: contacts have no "archived" flag — add "archived": True to each contact before saving

print(f"Saved {len(valid_contacts)} valid contacts to contacts.json")

# Read back and verify
with open("contacts.json") as f:
    data = json.loads(f)  # BUG
    print(f"Archived at: {data['archived_at']}")

