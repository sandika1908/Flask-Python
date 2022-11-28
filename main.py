from flask import Flask, render_template, url_for, redirect, flash, session
from flask import request
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import mysql.connector
import werkzeug

application = Flask(__name__)

application.secret_key = 'abc123'
application.config['MYSQL_HOST'] = 'localhost'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = ''
application.config['MYSQL_DB'] = 'rumahsakit'
mysql = MySQL(application)

    
@application.route('/')
@application.route('/index')
def index():
    return render_template("index.html")

def fungsiGet(querry):
    cursor = mysql.connection.cursor()
    cursor.execute(querry)
    output_json = cursor.fetchall()
    cursor.close()
    return output_json

def fungsiPost(querry):
    cursor = mysql.connection.cursor()
    print(querry)
    cursor.execute(querry)
    output_json = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    cursor.close()
    return output_json

@application.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM akses WHERE email=%s",(email,))
        user = curl.fetchone()
        curl.close()

        if user is not None and len(user) > 0 :
            if bcrypt.hashpw(password, user['password'].encode('utf-8')) == user['password'].encode('utf-8'):
                session['name'] = user ['name']
                session['email'] = user['email']
                return redirect(url_for('index'))
            else :
                flash("Gagal, Email atau Password Salah",'danger')
                return redirect(url_for('login'))
        else :
            flash("Isi Login Terlebih dahulu",'danger')
            return redirect(url_for('login'))
    else: 
        return render_template("login.html")

@application.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else :
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM akses WHERE name=%s OR email=%s',(name, email, ))
        user = cur.fetchone()
        if user is None:
            cur.execute("INSERT INTO akses (name,email,password) VALUES (%s,%s,%s)" ,(name, email, hash_password)) 
            mysql.connection.commit()
            flash('Registrasi Behasil, Silahkan Klik Tombol Login!','success')
        else:
            flash('Username atau email sudah ada','danger') 
        return redirect(url_for('register'))

@application.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

    # Rekam Medis Section
@application.route('/dashboard')
def read():
        sqlstr = "SELECT * from rekam_medis"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('dashboard.html',kalimat=output_json)

@application.route('/dashboard', methods=['GET','POST'])
def create():
    print(request.method)
    if request.method == 'GET':
        return render_template('dashboard.html')
    else: 
        request.method == 'POST'
        tanggal = request.form['tanggal']
        keluhan = request.form['keluhan']
        pemeriksaan = request.form['pemeriksaan']
        pengobatan = request.form['pengobatan']
        cursor = mysql.connection.cursor()
        sukses = "Data Berhasil Ditambahkan"
        sqlstr = "INSERT INTO rekam_medis (tanggal, keluhan, pemeriksaan, pengobatan) VALUES ('"+tanggal+"','"+keluhan+"','"+pemeriksaan+"','"+pengobatan+"')"
        print(sqlstr)
        cursor.execute(sqlstr)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('dashboard'))

@application.route('/update',methods=["POST"])
def update():
        id_rekam_medis = request.form['id_rekam_medis']
        tanggal = request.form['tanggal']
        keluhan = request.form['keluhan']
        pemeriksaan = request.form['pemeriksaan']
        pengobatan = request.form['pengobatan']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE rekam_medis SET tanggal=%s,keluhan=%s,pemeriksaan=%s,pengobatan=%s WHERE id_rekam_medis=%s", (tanggal,keluhan,pemeriksaan,pengobatan,id_rekam_medis,))
        mysql.connection.commit()
        return redirect(url_for('dashboard'))

@application.route('/hapus/<string:id_rekam_medis>',methods=["GET"])
def hapus(id_rekam_medis):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM rekam_medis WHERE id_rekam_medis=%s", (id_rekam_medis,))
        mysql.connection.commit()
        return redirect(url_for('dashboard'))

        # Pasien Section

@application.route('/pasien')
def readPasien():
        sqlstr = "SELECT * from pasien"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('pasien.html',kalimat=output_json)

@application.route('/pasien', methods=['GET','POST'])
def createPasien():
    print(request.method)
    if request.method == 'GET':
        return render_template('pasien.html')
    else: 
        request.method == 'POST'
        nama_pasien = request.form['nama_pasien']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        tanggal_lahir = request.form['tanggal_lahir']
        alamat = request.form['alamat']
        cursor = mysql.connection.cursor()
        sukses = "Data Berhasil Ditambahkan"
        sqlstr = "INSERT INTO pasien (nama_pasien, jenis_kelamin, no_telp, tanggal_lahir, alamat) VALUES ('"+nama_pasien+"','"+jenis_kelamin+"','"+no_telp+"','"+tanggal_lahir+"','"+alamat+"')"
        print(sqlstr)
        cursor.execute(sqlstr)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('pasien'))

@application.route('/updatePasien',methods=["POST"])
def updatePasien():
        id_pasien = request.form['id_pasien']
        nama_pasien = request.form['nama_pasien']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        tanggal_lahir = request.form['tanggal_lahir']
        alamat = request.form['alamat']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE pasien SET nama_pasien=%s,jenis_kelamin=%s,no_telp=%s,tanggal_lahir=%s,alamat=%s WHERE id_pasien=%s", (nama_pasien,jenis_kelamin,no_telp,tanggal_lahir,alamat,id_pasien,))
        mysql.connection.commit()
        return redirect(url_for('pasien'))

@application.route('/hapusPasien/<string:id_pasien>',methods=["GET"])
def hapusPasien(id_pasien):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM pasien WHERE id_pasien=%s", (id_pasien,))
        mysql.connection.commit()
        return redirect(url_for('pasien'))

#         # Perawat Section

@application.route('/perawat')
def readPerawat():
        sqlstr = "SELECT * from perawat"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('perawat.html',kalimat=output_json)

@application.route('/perawat', methods=['GET','POST'])
def createPerawat():
    print(request.method)
    if request.method == 'GET':
        return render_template('perawat.html')
    else: 
        request.method == 'POST'
        nama_perawat = request.form['nama_perawat']
        no_telp = request.form['no_telp']
        jenis_kelamin = request.form['jenis_kelamin']
        cursor = mysql.connection.cursor()
        sukses = "Data Berhasil Ditambahkan"
        sqlstr = "INSERT INTO perawat (nama_perawat, no_telp, jenis_kelamin) VALUES ('"+nama_perawat+"','"+no_telp+"','"+jenis_kelamin+"')"
        print(sqlstr)
        cursor.execute(sqlstr)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('perawat'))

@application.route('/hapusPerawat/<string:id_perawat>',methods=["GET"])
def hapusPerawat(id_perawat):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM perawat WHERE id_perawat=%s", (id_perawat,))
        mysql.connection.commit()
        return redirect(url_for('perawat'))

@application.route('/updatePerawat',methods=["POST"])
def updatePerawat():
        id_perawat = request.form['id_perawat']
        nama_perawat = request.form['nama_perawat']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE perawat SET nama_perawat=%s,no_telp=%s,jenis_kelamin=%s WHERE id_perawat=%s", (nama_perawat,no_telp,jenis_kelamin,id_perawat,))
        mysql.connection.commit()
        return redirect(url_for('perawat'))

#         # Kamar Section

@application.route('/kamar')
def readKamar():
        sqlstr = "SELECT * from kamar"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('kamar.html',kalimat=output_json)

@application.route('/kamar', methods=['GET','POST'])
def createKamar():
    print(request.method)
    if request.method == 'GET':
        return render_template('kamar.html')
    else: 
        request.method == 'POST'
        no_kamar = request.form['no_kamar']
        nama_kamar = request.form['nama_kamar']
        jenis_kamar = request.form['jenis_kamar']
        kapasitas = request.form['kapasitas']
        fasilitas = request.form['fasilitas']
        harga = request.form['harga']
        mysql.connection.commit()
        sukses = "Data Berhasil Ditambahkan"
        sqlstr = "INSERT INTO kamar (no_kamar, nama_kamar, jenis_kamar, kapasitas, fasilitas, harga) VALUES ('"+no_kamar+"','"+nama_kamar+"','"+jenis_kamar+"','"+kapasitas+"','"+fasilitas+"','"+harga+"')"
        print(sqlstr)
        cursor.execute(sqlstr)
        mysql.connection.commit()
        cursor.close()
        cursor.close()
        return redirect(url_for('kamar'))

@application.route('/updateKamar',methods=["POST"])
def updateKamar():
        no_kamar = request.form['no_kamar']
        nama_kamar = request.form['nama_kamar']
        jenis_kamar = request.form['jenis_kamar']
        kapasitas = request.form['kapasitas']
        fasilitas = request.form['fasilitas']
        harga = request.form['harga']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE kamar SET no_kamar=%s,nama_kamar=%s,jenis_kamar=%s,kapasitas=%s,fasilitas=%s,harga=%s WHERE no_kamar=%s", (no_kamar,nama_kamar,jenis_kamar,kapasitas,fasilitas,harga,no_kamar,))
        mysql.connection.commit()
        return redirect(url_for('kamar'))

@application.route('/hapusKamar/<string:no_kamar>',methods=["GET"])
def hapusKamar(no_kamar):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM kamar WHERE no_kamar=%s", (no_kamar,))
        mysql.connection.commit()
        return redirect(url_for('kamar'))

        # Obat Section

@application.route('/obat')
def readObat():
        sqlstr = "SELECT * from obat"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('obat.html',kalimat=output_json)

@application.route('/obat', methods=['GET','POST'])
def createObat():
    print(request.method)
    if request.method == 'GET':
        return render_template('obat.html')
    else: 
        request.method == 'POST'
        nama_obat = request.form['nama_obat']
        jenis_obat = request.form['jenis_obat']
        tahun_produksi = request.form['tahun_produksi']
        masa_berlaku = request.form['masa_berlaku']
        cursor = mysql.connection.cursor()
        sukses = "Data Berhasil Ditambahkan"
        sqlstr = "INSERT INTO obat (nama_obat, jenis_obat, tahun_produksi, masa_berlaku) VALUES ('"+nama_obat+"','"+jenis_obat+"','"+tahun_produksi+"','"+masa_berlaku+"')"
        print(sqlstr)
        cursor.execute(sqlstr)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('obat'))

@application.route('/updateObat',methods=["POST"])
def updateObat():
        kode_obat = request.form['kode_obat']
        nama_obat = request.form['nama_obat']
        jenis_obat = request.form['jenis_obat']
        tahun_produksi = request.form['tahun_produksi']
        masa_berlaku = request.form['masa_berlaku']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE obat SET nama_obat=%s,jenis_obat=%s,tahun_produksi=%s,masa_berlaku=%s WHERE kode_obat=%s", (nama_obat,jenis_obat,tahun_produksi,masa_berlaku,kode_obat,))
        mysql.connection.commit()
        return redirect(url_for('obat'))

@application.route('/hapusObat/<string:kode_obat>',methods=["GET"])
def hapusObat(kode_obat):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM obat WHERE kode_obat=%s", (kode_obat,))
        mysql.connection.commit()
        return redirect(url_for('obat'))

        # Dokter Section

@application.route('/dokter')
def readDokter():
        sqlstr = "SELECT * from dokter"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('dokter.html',kalimat=output_json)

@application.route('/dokterCreate', methods=['GET','POST'])
def createDokter():
    if request.method == 'GET':
        print(request.method)
        id_spesialis = fungsiGet("SELECT id_spesialis FROM spesialis")
        return render_template('dokterCreate.html', kalimat=id_spesialis)
    elif request.method == 'POST':
        nama_dokter = request.form['nama_dokter']
        id_spesialis = request.form['id_spesialis']
        no_telp = request.form['no_telp']
        alamat = request.form['alamat']
        pagi = request.form['pagi']
        fungsiPost("INSERT INTO dokter (nama_dokter, id_spesialis, no_telp, alamat, pagi) VALUES ('"+nama_dokter+"','"+id_spesialis+"','"+no_telp+"','"+alamat+"','"+pagi+"');")
        sukses = "Data Berhasil Ditambahkan"
        return redirect(url_for('dokter'))

@application.route('/updateDokter',methods=["POST"])
def updateDokter():
        id_dokter = request.form['id_dokter']
        nama_dokter = request.form['nama_dokter']
        id_spesialis = request.form['id_spesialis']
        no_telp = request.form['no_telp']
        alamat = request.form['alamat']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE dokter SET nama_dokter=%s,id_spesialis=%s,no_telp=%s,alamat=%s WHERE id_dokter=%s", (nama_dokter,id_spesialis,no_telp,alamat,id_dokter,))
        mysql.connection.commit()
        return redirect(url_for('dokter'))

@application.route('/hapusDokter/<string:id_dokter>',methods=["GET"])
def hapusDokter(id_dokter):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM dokter WHERE id_dokter=%s", (id_dokter,))
        mysql.connection.commit()
        return redirect(url_for('dokter'))

        # Spesialis Section

@application.route('/spesialis')
def readSpesialis():
        sqlstr = "SELECT * from spesialis"
        cursor = mysql.connection.cursor()
        cursor.execute(sqlstr)
        output_json = cursor.fetchall()
        cursor.close()
        return render_template('spesialis.html',kalimat=output_json)

@application.route('/spesialis', methods=['GET','POST'])
def createSpesialis():
    print(request.method)
    if request.method == 'GET':
        return render_template('spesialis.html')
    else: 
        request.method == 'POST'
        spesialis = request.form['spesialis']
        cursor = mysql.connection.cursor()
        sukses = "Data Berhasil Ditambahkan"
        sqlstr = "INSERT INTO spesialis (spesialis) VALUES ('"+spesialis+"')"
        print(sqlstr)
        cursor.execute(sqlstr)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('spesialis'))

@application.route('/updateSpesialis',methods=["POST"])
def updateSpesialis():
        id_spesialis = request.form['id_spesialis']
        spesialis = request.form['spesialis']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE spesialis SET spesialis=%s WHERE id_spesialis=%s", (spesialis,id_spesialis,))
        mysql.connection.commit()
        return redirect(url_for('spesialis'))

@application.route('/hapusSpesialis/<string:id_spesialis>',methods=["GET"])
def hapusSpesialis(id_spesialis):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM spesialis WHERE id_spesialis=%s", (id_spesialis,))
        mysql.connection.commit()
        return redirect(url_for('spesialis'))

# @application.route('/login')
# def login():
#     return render_template("login.html")

@application.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@application.route('/pasien')
def pasien():
    return render_template("pasien.html")

@application.route('/perawat')
def perawat():
    return render_template("perawat.html")

@application.route('/kamar')
def kamar():
    return render_template("kamar.html")

@application.route('/obat')
def obat():
    return render_template("obat.html")

@application.route('/dokter')
def dokter():
    return render_template("dokter.html")

@application.route('/dokterCreate')
def dokterCreate():
    return render_template("dokterCreate.html")

@application.route('/dokterUpdate')
def dokterUpdate():
    return render_template("dokterUpdate.html")

@application.route('/spesialis')
def spesialis():
    return render_template("spesialis.html")

# def getMysqlConnection():
#     return mysql.connector.connect(user='root', host='localhost', port='3306', password='', database='rumahsakit')

if __name__ == '__main__':
    application.run(debug=True)