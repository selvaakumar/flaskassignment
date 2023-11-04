from flask import Flask, jsonify, render_template,request,redirect,url_for
import sqlite3
app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    # Add more sample books here...
]

conn = sqlite3.connect('books.db')
c = conn.cursor()

# Create a books table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT)''')
conn.commit()

def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def get_book(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    print(book_id)
    book = get_book(book_id)
    if book:
        return render_template('book.html', book=book)
    return "Book not found", 404

@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            conn = sqlite3.connect('books.db')
            c = conn.cursor()
            c.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            conn.commit()
            c.execute('SELECT * FROM books')
            books = c.fetchall()
            conn.close()
            return redirect(url_for('get_books', books = books))
        return render_template('create.html')
   

@app.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    if book:
        if request.method == 'POST':
            title = request.form['title']
            author = request.form['author']
            conn.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, book_id))
            conn.commit()
            conn.close()
            return redirect(url_for('get_book', book_id=book_id))
        conn.close()
        return render_template('edit.html', book=book)
    return "Book not found", 404

@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_books'))





if __name__=="__main__":
    app.run(host="0.0.0.0",port=8005)
