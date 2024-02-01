from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Path ke file JSON
file_path = 'mahasiswa_data.json'

# Fungsi untuk membaca data dari file JSON
def read_data_from_file():
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

# Fungsi untuk menulis data ke file JSON
def write_data_to_file(mahasiswa_list):
    with open(file_path, 'w') as file:
        json.dump(mahasiswa_list, file)

@app.route('/')
def index():
    mahasiswa_list = read_data_from_file()
    return render_template('index.html', mahasiswa_list=mahasiswa_list)

@app.route('/submit', methods=['POST'])
def submit():
    nim = request.form.get('nim')
    nama = request.form.get('nama')
    fakultas = request.form.get('fakultas')

    # Membaca data yang sudah ada dari file
    mahasiswa_list = read_data_from_file()

    # Menambahkan data baru ke list
    mahasiswa_list.append({'nim': nim, 'nama': nama, 'fakultas': fakultas})

    # Melakukan sorting berdasarkan 4 digit terakhir NIM
    mahasiswa_list.sort(key=lambda x: x['nim'][-4:])

    # Menulis data yang sudah diurutkan ke file
    write_data_to_file(mahasiswa_list)

    return render_template('index.html', mahasiswa_list=mahasiswa_list)

if __name__ == '__main__':
    app.run(debug=True)
