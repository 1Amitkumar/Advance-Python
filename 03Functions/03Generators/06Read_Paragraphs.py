def readpara(iterable):
    para = ""
    for line in iterable:
        if line.strip() == '' and para:
            yield para[1:]
            para = ""
        else:
            para += " " + line
    if para:
        yield para[1:]


text = """This is text and
it contains 3 paragraphs.

Each paragraph contains multiple lines.

After every paragraph,
there is line.""".split('\n')

for paraline in readpara(text):
    print(paraline)
    print('-' * 42)

