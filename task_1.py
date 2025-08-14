initial_str = '1h 45m,360s,25m,30m 120s,2h 60s'
initial_str = initial_str.replace(' ', ',')

str_splitted = initial_str.split(sep=',')

result = int()
for element in str_splitted:
    if 'h' in element:
        result += int(element.replace('h', '')) * 60
    elif 's' in element:
        result += int(element.replace('s', '')) / 60
    else: result += int(element.replace('m', ''))

print(result)