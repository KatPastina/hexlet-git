from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Функция работаетневерно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
