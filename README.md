### qa_python
## Тестирование метода **add_new_book**:

1. Проверка кол-ва книг при добавлении двух книг
test_add_new_book_add_two_books

2. Проверка, что при добавлении книги в жанре пустое значение
test_add_new_book_empty_genre

3. Проверка, что нига не добавляется с некорректной длиной названия (0, 41 символ) или если была добавлена ранее
test_add_new_book_incorrect_title

## Тестирование метода **set_book_genre**:
4. Проверка, что жанр устанавливается, если книга есть в books_genre и её жанр входит в список genre
test_set_book_genre_for_existing_title_and_genre

5. Проверка, что жанр НЕ устанавливается, если он НЕ входит в список genre
test_set_book_genre_for_not_in_genre

## Тестирование метода **get_book_genre**:
6. Проверка получения жанра по названию книги из словаря books_genre
test_get_book_genre_in_books_genre

## Тестирование метода **get_books_with_specific_genre**:
7. Проверка получения списка книг с заданным жанром, если жанр входит в список genre
test_get_books_with_specific_genre_existing_genre

8. Проверка получения пустого списка книг с заданным жанром, если жанр НЕ входит в список genre
test_get_books_with_specific_genre_not_existing_genre

## Тестирование метода **get_books_genre**:
9. Проверка получения корректных данных из словаря books_genre
test_get_books_genre_not_empty

## Тестирование метода **get_books_for_children**:
10. Проверка, что в списке для детей отсутствуют жанры из возрастной категории
test_get_books_for_children_not_in_age_rating

## Тестирование метода **add_book_in_favorites**:
11. Проверка добавления двух книг в избранное
test_add_book_in_favorites_add_two_books

12. Проверка, что книга не добавляется в избранное больше одного раза
test_add_book_in_favorites_add_book_two_times

## Тестирование метода **delete_book_from_favorites**:
13. Проверка удаления книги из избранного
test_delete_book_from_favorites_delete_one_book

## Тестирование метода **get_list_of_favorites**:
14. Проверка получения списка книг из избранного
test_get_list_of_favorites_books_not_empty