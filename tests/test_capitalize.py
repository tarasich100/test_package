from package_name.capitalize import capitalize


def test_capitalize():
    assert capitalize('') == '', 'Функция работает неверно!'
    assert capitalize('hello') == 'Hello', 'Функция работает неверно!'
    assert capitalize(' #_225643') == ' #_225643', 'Функция работает неверно!'
    print('Все тесты пройдены!')


test_capitalize()
