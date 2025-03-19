#!/usr/bin/env python3
import cgi

def remove_parentheses_content(s):
    result = []
    depth = 0
    for char in s:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif depth == 0:
            result.append(char)
    return ''.join(result)

print("Content-type: text/html\n")

form = cgi.FieldStorage()
text = form.getvalue("text", "")

output_text = remove_parentheses_content(text)

print(f"<h1>Result: {output_text}</h1>")
