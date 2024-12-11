from flask import Flask, render_template, request  

app = Flask(__name__)  

# Variabel untuk menyimpan daftar buku  
books = []  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    if request.method == 'POST':  
        book_title = request.form.get('book_title')  
        book_author = request.form.get('book_author')  
        if book_title and book_author:  
            books.append({'title': book_title, 'author': book_author})  

    return render_template('index.html', books=books)  

if __name__ == '__main__':  
    app.run(debug=True)