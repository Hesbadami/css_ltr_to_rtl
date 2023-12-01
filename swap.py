import re
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

with open(inputfile, 'r') as f:
    css = f.read()

to_switch = re.findall(r'(?:margin|padding)(?:\s+)?:(?:\s+)?(?:-?\.?\d+(?:px|rem|em|%|cm|in|pc|pt|mm|ex)?|auto|inherit)\s+(?:-?\.?\d+(?:px|rem|em|%|cm|in|pc|pt|mm|ex)?|auto|inherit)\s+(?:-?\.?\d+(?:px|rem|em|%|cm|in|pc|pt|mm|ex)?|auto|inherit)\s+(?:-?\.?\d+(?:px|rem|em|%|cm|in|pc|pt|mm|ex)?|auto|inherit)(?:\s+)?;?', css)
to_switch = [item.strip(' ;\n') for item in to_switch]

switch_with = []
for i, item in enumerate(to_switch):
    split = item.split(':')
    key = split[0].strip(' \n')
    values = split[1].strip(' ;\n').split(' ')

    tmp = values[3]
    values[3] = values[1]
    values[1] = tmp

    switch_with.append(key + ': ' + ' '.join(values))

hold_temp = {}
hold_counter = 1
for i, item in enumerate(to_switch):
    if switch_with[i] not in to_switch:  # to make sure we don't accidentally swap back what we have already changed
        css = css.replace(item, switch_with[i])
    else:
        hold_phrase = f't3mp0r4ry_{hold_counter}'
        hold_temp[hold_phrase] = switch_with[i]
        css = css.replace(item, hold_phrase)
        hold_counter += 1

for p in hold_temp:
    css = css.replace(p, hold_temp[p])

css = css.replace('left', 't3mP0r4rY_r1gHT')
css = css.replace('right', 'left')
css = css.replace('t3mP0r4rY_r1gHT', 'right')

css = css.replace('ltr', 't3mP0r4rY_rT1')
css = css.replace('rtl', 'ltr')
css = css.replace('t3mP0r4rY_rT1', 'rtl')

with open(outputfile, 'w') as f:
    f.write(css)