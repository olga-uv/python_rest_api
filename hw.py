import pytest
from assertpy import assert_that


def test_not_long_string(string_to_check):
    assert len(string_to_check) <= 30, f'{string_to_check} contains more than 30 symbols'


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [fruit + 's' for fruit in fruits if 'a' in fruit]

# for fruit in fruits:
#     if 'a' in fruit:
#         new_list.append(fruit)
print(new_list)


response_content = [
    {
        "name": "John",
        "user_id": 18463,
        "created": "2022-06-17T10:22:16.782655"
    },
    {
        "name": "Ivan",
        "user_id": 384682,
        "created": "2022-06-17T10:23:03.209473"
    }

]
response = [11, 22]

user_ids=[user['user_id'] for user in response_content]
print(user_ids)


def test_assert_name():
    assert_that(response_content).extracting('name').contains('Ivan').is_length(2)
    #assert_that(user_ids).extracting(0).is_length(6)
    assert_that(response).extracting(0).is_length(2)
