from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'name, expected',
        [
            ('Книга', True),
            ('А' * 40, True),
            ('А' * 41, False),
            ('', False)
        ],
    )
    def test_add_new_book_length_and_empty(self, name, expected):
        collector = BooksCollector()
        initial_len=len(collector.books_genre)
        collector.add_new_book(name)
        assert (len(collector.books_genre) == initial_len +1) == expected

    def test_add_new_book_same_name(self):
        collector = BooksCollector()
        name = 'Повторение книги'
        collector.add_new_book(name)
        collector_len = len(collector.books_genre)
        collector.add_new_book(name)
        assert len(collector.books_genre) == collector_len

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        name = 'Любимая книга'
        genre = 'Фантастика'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('genre, expected_books' , [('Фантастика', ['Книга 1','Книга 3']), ('Ужасы', ['Книга 2']), ('Неизвестная', [])])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()

        books= [('Книга 1','Фантастика'), ('Книга 2','Ужасы') , ('Книга 3','Фантастика')]

        for name , g in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, g)

        result = collector.get_books_with_specific_genre(genre)
        assert result == expected_books

    def test_get_books_for_children(self):
        collector = BooksCollector()

        books =[('Детские шутки', 'Комедии'), ('Смешарики','Мультфильмы'), ('Хоррор','Ужасы'), ('История','Детективы'), ('Сказка','Фантастика')]

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        result = collector.get_books_for_children()
        expected = ['Детские шутки', 'Смешарики', 'Сказка']
        assert sorted(result) == sorted(expected)

    def test_add_book_in_favorites_valid(self):
        collector = BooksCollector()
        name = 'Любимая книга'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent(self):
        collector = BooksCollector()
        nonexistent_name = 'Отсутствующая'

        collector.add_book_in_favorites(nonexistent_name)

        assert nonexistent_name not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_repeat(self):
        collector = BooksCollector()
        name = 'Повтор книги'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)

        favorites = collector.get_list_of_favorites_books()
        assert favorites.count(name) == 1

    def test_delete_book_from_favorites_existing(self):
        collector = BooksCollector()
        name= 'Избранная'

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_list(self):
        collector = BooksCollector()
        not_in_favorites = 'Не Избранная'

        before_len=len(collector.get_list_of_favorites_books())
        collector.delete_book_from_favorites(not_in_favorites)
        after_len=len(collector.get_list_of_favorites_books())

        assert before_len == after_len