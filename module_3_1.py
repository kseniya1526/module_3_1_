calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result
def is_contains(string, list_to_search):
    count_calls()
    for str_ in list_to_search:
        if str_.lower().find(string.lower()) >= 0:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)









