from main import BooksCollector

import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        assert collector.books_genre["Гордость и предубеждение и зомби"] == ""

    @pytest.mark.parametrize('title', ['', 'Очень длинное название длиной в 41 символ','Трудно быть богом'])
    def test_add_new_book_incorrect_title(self, title):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": ""}
        collector.add_new_book(title)
        assert collector.books_genre == {"Трудно быть богом": ""}

    def test_set_book_genre_for_existing_title_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Трудно быть богом")
        collector.set_book_genre("Трудно быть богом", "Фантастика")
        assert collector.books_genre["Трудно быть богом"] == "Фантастика"

    def test_set_book_genre_for_not_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фэнтези")
        assert collector.books_genre["Властелин колец"] == ""

    @pytest.mark.parametrize('title', ["Трудно быть богом", "Приключения Шурика", "Дело о пропавшем слоне"])
    def test_get_book_genre_in_books_genre(self, title):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "Фантастика", "Приключения Шурика": "Комедии", "Лабиринт отражений": "Фантастика", "Дело о пропавшем слоне": ""}
        assert collector.get_book_genre(title) == collector.books_genre[title]

    @pytest.mark.parametrize('genre', ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_get_books_with_specific_genre_existing_genre(self, genre):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "Фантастика", "Приключения Шурика": "Комедии", "Лабиринт отражений": "Фантастика", "Дело о пропавшем слоне": ""}
        assert collector.get_books_with_specific_genre(genre) == [key for key, value in collector.books_genre.items() if value == genre]
        # как найти все значения по ключу подсказал ИИ

    def test_get_books_with_specific_genre_not_existing_genre(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "Фантастика", "Приключения Шурика": "Комедии", "Властелин колец": "Фэнтези"}
        assert collector.get_books_with_specific_genre("Фэнтези") == []

    def test_get_books_genre_not_empty(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "Фантастика"}
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_not_in_age_rating(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "", "Приключения Шурика": "Комедии", "Гордость и предубеждение и зомби": "Ужасы"}
        for i in collector.get_books_for_children():          
            assert collector.get_book_genre(i) not in collector.genre_age_rating

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "", "Приключения Шурика": "Комедии", "Лабиринт отражений": "Фантастика"}
        collector.add_book_in_favorites("Трудно быть богом")
        collector.add_book_in_favorites("Приключения Шурика")
        assert collector.favorites == ["Трудно быть богом", "Приключения Шурика"]

    def test_add_book_in_favorites_add_book_two_times(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": "", "Приключения Шурика": "Комедии"}
        collector.add_book_in_favorites("Трудно быть богом")
        collector.add_book_in_favorites("Трудно быть богом")
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": ""}
        collector.add_book_in_favorites("Трудно быть богом")
        collector.delete_book_from_favorites("Трудно быть богом")
        assert collector.favorites == []

    def test_get_list_of_favorites_books_not_empty(self):
        collector = BooksCollector()
        collector.books_genre = {"Трудно быть богом": ""}
        collector.add_book_in_favorites("Трудно быть богом")
        assert collector.get_list_of_favorites_books() == collector.favorites
