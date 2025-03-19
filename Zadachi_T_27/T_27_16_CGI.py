#!/usr/bin/env python3
import cgi
import json

FILE_PATH = "contacts.json"

def load_contacts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

contacts = load_contacts()

print("Content-type: text/html\n")

form = cgi.FieldStorage()
action = form.getvalue("action", "")
name = form.getvalue("name", "")
phone = form.getvalue("phone", "")

response_text = "Invalid request"

if action == "add" and name and phone:
    contacts[name] = phone
    save_contacts(contacts)
    response_text = f"Added: {name} - {phone}"

elif action == "edit" and name and phone:
    if name in contacts:
        contacts[name] = phone
        save_contacts(contacts)
        response_text = f"Updated: {name} - {phone}"
    else:
        response_text = "Contact not found"

elif action == "search" and name:
    response_text = f"{name}: {contacts.get(name, 'Not found')}"

print(f"<h1>{response_text}</h1>")
