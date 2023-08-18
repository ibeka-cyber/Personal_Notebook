class Notes:
    def __init__(self):
        self.titles=[]
        self.notes = []

    def add_notes(self, title, note):
        self.titles.append(title)
        self.notes.append(note)
        print("Not eklendi!")

    def show_notes(self):
        for i in range(len(self.notes)):
            print(f"{i+1}. Başlık: {self.titles[i]}")
            print(f"  İçerik: {self.notes[i]}")

    def delete_notes(self, title):
        if title in self.titles:
            index = self.titles.index(title)
            content=self.notes[index]
            self.titles.pop(index)
            self.notes.pop(index)
            print(f"Başlığı {title} olan '{content}' içeriğine sahip notu sildik! :)  ")
        else:
            print("Şey biz aradığın şeyi bulamadık :(")