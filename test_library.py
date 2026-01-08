from library import format_book_details

def test_format_book_details():
    result = format_book_details(
        book_id=101,
        book_title="Python Programming",
        author_name="Guido van Rossum",
        year_of_publication=2020
    )

    expected_output = (
        "Book ID: 101\n"
        "Book Title: Python Programming\n"
        "Author Name: Guido van Rossum\n"
        "Year of Publication: 2020"
    )

    assert result == expected_output
