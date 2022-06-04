import pytest
import pdb


books = [
    {"title": "Японские мифы",
     "price": "345", "author": ["Джошуа Фридман"]},
    {"title": "Курочка ряба",
     "price": "200", "author": [""]},
    {"title": "Невский дозор",
     "price": "899.99", "author": ["Игорь Вардунас", "Никита Аверин"]}
    ]


def get_count_of_book_author(books_list, title):
    for i in range(len(books_list)):
        title_in_dict = books_list[i]["title"]
        if title_in_dict == title:
            count_of_book_author = len(books_list[i]["author"])
            return count_of_book_author


def get_books_by_author(books_list, author):
    title_list = []
    for book in books_list:
        author_in_dict = book["author"]
        if author in author_in_dict:
            title_list.append(book["title"])
    return title_list


def total_price(books_list):
    total_books_price = 0
    for book in books_list:
        # pdb.set_trace()
        total_books_price += float(book["price"])
    return total_books_price


print(total_price(books))

print(get_books_by_author(books, "Джошуа Фридман"))


@pytest.mark.parametrize("title, expected_count", [
                        ("Японские мифы", 1), ("Курочка ряба", 0), ("Невский дозор", 2)])
def test_get_count_of_book_author(title, expected_count):
    assert get_count_of_book_author(books, title) == expected_count


