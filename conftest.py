import datetime

import pytest


@pytest.fixture(autouse=True)
def exact_time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    f = open('C:/Users/leonto/Log.txt', 'w', encoding='utf8')
    f.write(current_time)


@pytest.fixture
def string_to_check():
    #input_string = input().replace(" ", "")
    input_string = "hfjhjkjklj jgh g jkjk"
    return input_string



