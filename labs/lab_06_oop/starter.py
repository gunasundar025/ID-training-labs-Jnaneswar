from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    checked_out: bool = False


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        raise NotImplementedError("Complete lab 06")

    def find_book(self, title: str) -> Book | None:
        raise NotImplementedError("Complete lab 06")

    def check_out(self, title: str) -> bool:
        raise NotImplementedError("Complete lab 06")

    def return_book(self, title: str) -> bool:
        raise NotImplementedError("Complete lab 06")
