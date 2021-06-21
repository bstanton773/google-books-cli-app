import os
import click
from flask import cli
from flask.cli import AppGroup
import requests
from app.blueprints.main.models import Book, Author
from app import db

blueprint = AppGroup('google')
book_list = []  # moving booklist to the global scope


@blueprint.command("search")
@click.argument('book_name')
def get_booklist(book_name):
    data = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q={book_name}').json()['items'][:5]
    selection_id = 0
    for book in data:
        selection_id += 1
        new_book = {
            'selection_id': selection_id,
            'id': book['id'],
            'title': book['volumeInfo']['title']
        }
        if book['volumeInfo'].get('publisher'):
            new_book.update(publisher=book['volumeInfo']['publisher'])
        if book['volumeInfo'].get('authors'):
            new_book.update(authors=book['volumeInfo']['authors'])
        book_list.append(new_book)

        return book_list


def create(book_name):
    """Use the Google Books API to search for a book."""
    done = False
    while not done:
        try:
            search = input  # what gets typed is passed into get book_list
            booklist = get_booklist()
            # book_list = [] - where booklist originally is

            possible_choices = list(range(1, 6))
            for idx, book in enumerate(Book.query.all()):
                print(book, book.get_authors())

            print('='*40)
            option = input(
                "Here is your current reading list. Press any key to continue, or type 'quit' to exit program. ").lower()
            if option == 'quit':
                break
            for idx, book in enumerate(book_list):
                print(
                    f"{idx+1}: [{book['id']}] {book['title']} by {book['authors']} | Publisher: {book['publisher']}")

            choice = int(input(
                "\nHere are your list of books. Type one of options 1-5 to select a book to add to your reading list. \n"))
            if choice in possible_choices:
                for i in book_list:
                    if choice == i['selection_id']:
                        b = Book(
                            book_id=i['id'], title=i['title'], publisher=i['publisher'])
                        db.session.add(b)
                        for n in i['authors']:
                            a = Author(name=n, book_id=i['id'])
                            db.session.add(a)
                db.session.commit()
            if choice not in possible_choices:
                print(f"That is not an option. Please only select a number from 1-5.")

        except Exception as error:
            print(f"Something went wrong with creating the blueprint")
            print(error)
    return print("Application Exited")

# move some objects outside of the function

    # break into one section creating the book

    # book creation, saving it into the database and the author
    # move displaying of book into it's own

    # put booklist outside of the function in the global scope, take out the fucntionality that creates the booklist
# make a function called get book list that returns a list of books from the search
# make a function that accepts a string of text, string is whatver book youre searching for, that function returns the list of books from the search
