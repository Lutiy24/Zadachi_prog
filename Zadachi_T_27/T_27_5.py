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

def application(environ, start_response):
    from urllib.parse import parse_qs

    query = parse_qs(environ.get('QUERY_STRING', ''))
    input_text = query.get('text', [''])[0]

    output_text = remove_parentheses_content(input_text)

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [f"<h1>Result: {output_text}</h1>".encode('utf-8')]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    port = 8000
    print(f"Running on http://127.0.0.1:{port}/?text=Hello(World)Test")
    server = make_server('', port, application)
    server.serve_forever()
