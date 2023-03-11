from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def recent_books_list(books_data):
    recent_books = InlineKeyboardMarkup(row_width=5)
    inline_buttons = [InlineKeyboardButton(text=f"{i+1}", callback_data=f"id_{books_data[i]['id']}")
                      for i in range(len(books_data))]
    recent_books.add(*inline_buttons)
    return recent_books

def book_keyboard(url, download):
    recent_book_markup = InlineKeyboardMarkup(row_width=1)
    url_button = InlineKeyboardButton(text="↗️Url", url=url)
    download_button = InlineKeyboardButton(text="📥 Download", url=download)

    recent_book_markup.add(url_button, download_button)

    return recent_book_markup