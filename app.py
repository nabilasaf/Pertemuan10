from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        name = request.form['name']  # Mengambil data dari form
        message = f'Hello, {name}!'  # Menyimpan pesan untuk ditampilkan
    return render_template("index.html") # Merender halaman HTML dengan pesan

if __name__ == '__main__':
    app.run(debug=True)  # Menjalankan aplikasi dalam mode debug