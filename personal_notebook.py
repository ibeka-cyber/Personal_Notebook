from show_menu import show_main_menu
from note_operations import Notes
note_class= Notes()
def main():
    while True:
        show_main_menu()
        choice=input("Seçiminizi yapınız: ")
        if choice == "1":
            note_class.show_notes()
            
        elif choice == "2":
            while True:
                title = input("Not başlığı ne olsun? : ")
        
                if title in note_class.titles:
                    print("Daha önce bu başlıkta bir not yazmıştın. Hadi daha iyisini deneyelim :)")
                else:
                    note = input("Not içeriğini girebilirsin bakmıyoruz :) : ")
                    note_class.add_notes(title, note)
                    break  
    
        elif choice=="3":
            del_note=input("Silmek istediğiniz notun başlığını giriniz: ")
            note_class.delete_notes(del_note)
            
        elif choice=="4":
            break
        else:
            print("\nGirdiğiniz şey hakkında bir fikrimiz yok :') ")
        

        

