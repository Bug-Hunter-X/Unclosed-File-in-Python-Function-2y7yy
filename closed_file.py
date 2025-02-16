def function_with_closed_file(filename):
    with open(filename, 'r') as f:
        # ... some code that processes the file ...
        processed_data = f.read()
    return processed_data