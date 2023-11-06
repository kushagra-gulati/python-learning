import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    match = re.search(string, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))

        #2nd
        import re

silly_string = "the cat in the hat"
pattern = "the"
lt = re.finditer(pattern,silly_string)
print(next(lt))
print(next(lt))
for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    print(s)