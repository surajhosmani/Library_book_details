def format_book_details(book_id, book_title, author_name, year_of_publication):
    """
    Accepts library book details and returns them
    as a neatly formatted multi-line string.
    """
    return (
        f"Book ID: {book_id}\n"
        f"Book Title: {book_title}\n"
        f"Author Name: {author_name}\n"
        f"Year of Publication: {year_of_publication}"
    )
