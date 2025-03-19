import json
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

FILE_PATH = "contacts.json"

# Завантаження або створення файлу довідника
def load_contacts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

def application(environ, start_response):
    contacts = load_contacts()
    query = parse_qs(environ.get("QUERY_STRING", ""))

    action = query.get("action", [""])[0]
    name = query.get("name", [""])[0]
    phone = query.get("phone", [""])[0]

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

    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return [f"<h1>{response_text}</h1>".encode("utf-8")]

if __name__ == "__main__":
    port = 8000
    print(f"Running on http://127.0.0.1:{port}/?action=add&name=John&phone=123456")
    server = make_server("", port, application)
    server.serve_forever()
