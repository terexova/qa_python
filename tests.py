from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name',
        [
        '',
        'абвгдеёжзиабвгдеёжзиабвгдеёжзиабвгдеёжзиа',
        'абвгдеёжзиабвгдеёжзиабвгдеёжзиабвгдеёжзиаб',
        'абвгдеёжзиабвгдеёжзиабвгдеёжзиабвгдеёжзиабвгдеёжзи',
    ])
    def test_try_add_not_valid_book(self, name):
        collector = BooksCollector()
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Фантастика'

    def test_get_books_with_specific_genre_fantastic(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        expected = {
            'Гордость и предубеждение': 'Фантастика',
            'Что делать, если ваш кот хочет вас убить': 'Ужасы'
        }

        assert collector.get_books_genre() == expected

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Шурик')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Шурик', 'Комедии')
        expected = ['Гордость и предубеждение', 'Шурик']

        assert collector.get_books_for_children() == expected

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Шурик')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_book_in_favorites('Шурик')

        assert len(collector.get_list_of_favorites_books()) == 2


    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Шурик')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_book_in_favorites('Шурик')
        collector.delete_book_from_favorites('Шурик')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение')

        expected = ['Гордость и предубеждение']

        assert collector.get_list_of_favorites_books() == expected

