import sqlite3
#main menu
def show_main_menu():
    print("""****** NOT DEFTERİ UYGULAMASI ****** 
             
    1) Notları Görüntüle 
    2) Not Ekle 
    3) Not Sil 5
    4) Çıkış""")
#not operasyonları 
class Notes:
    def __init__(self, db_path='not_defteri.db'):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()
    
    #veritabanı yoksa oluşturma
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                note_title TEXT NOT NULL,
                note_content TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    #not ekleme
    def add_notes(self, title, note):
        if title in self.get_titles():
            print("Daha önce bu başlıkta bir not yazmıştın. Hadi daha iyisini deneyelim :)")
        else:
            self.cursor.execute('''
                INSERT INTO customer_notes (note_title, note_content)
                VALUES (?, ?)
            ''', (title, note))
            self.connection.commit()
            print("Not eklendi!")

    #not görüntüleme
    def show_notes(self):
        self.cursor.execute('SELECT * FROM customer_notes')
        notes = self.cursor.fetchall()
        for note in notes:
            print(f"Başlık: {note[1]}")
            print(f"İçerik: {note[2]}")
            print()

    #not silme
    def delete_notes(self, title):
        self.cursor.execute('DELETE FROM customer_notes WHERE note_title = ?', (title,))
        if self.connection.total_changes > 0:
            print(f"Başlığı {title} olan notu sildik! :) ")
        else:
            print("Şey, aradığın şeyi bulamadık :(")

    #bu metot veritabanındaki başlıkları getirir ve yeni yazılacak not başlığı veritabanında var mı diye kontrol eder.
    def get_titles(self): 
        self.cursor.execute('SELECT note_title FROM customer_notes')
        titles = self.cursor.fetchall()
        return [title[0] for title in titles]

    def close_connection(self):
        self.connection.close()

if __name__ == '__main__':
    note_class = Notes()

    while True:
        show_main_menu()
        choice = input("Seçiminizi yapınız: ")
       
        if choice == "1":
            note_class.show_notes()

        elif choice == "2":
            title = input("Not başlığı ne olsun? : ")
            note = input("Not içeriğini girebilirsin bakmıyoruz :) : ")
            note_class.add_notes(title, note)

        elif choice == "3":
            del_note = input("Silmek istediğiniz notun başlığını giriniz: ")
            note_class.delete_notes(del_note)

        elif choice == "4":
            note_class.close_connection()
            break

        else:
            print("\nGirdiğiniz şey hakkında bir fikrimiz yok :') ")
