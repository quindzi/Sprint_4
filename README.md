qa_python
Отчёт:
Мной были реализованы 10 тестов и выполнена параметризация
test_add_new_book_length_and_empty проверяет граничные случаи длины названия и пустую строку.
test_add_new_book_same_name проверяет дублируется ли книга с повтором в названии
test_set_book_genre_valid корректная установка жанра для существующей книги
test_get_books_with_specific_genre фильтрация книг по жанру и проверка возврата названия, соответствующего жанру
test_get_books_for_children проверяет логику формирования подборки детских книг
test_add_book_in_favorites_valid проверка добавления существующей книги в избранное
test_add_book_in_favorites_nonexistent проверка попытки добавления в избранное несуществующей книги
test_add_book_in_favorites_repeat проверка повторного добавления одной и той же книги, дубликата быть не должно
test_delete_book_from_favorites_existing проверка удаления существующей книги книги из избранного
test_delete_book_from_favorites_not_in_list проверка возможности удаления книги, которой нет в избранном
Все тексты независимы друг от друга за счёт нового экземпляра collector = BooksCollector()
