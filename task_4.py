def pretty_message(input_string):
    return re.sub(r'((\w){1,}?)(\1+)', r'\1', input_string)
