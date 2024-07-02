class Book:
    def __init__(self, judul, penulis, tahun):
        self.title = judul
        self.author = penulis
        self.year = tahun

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, judul):
        result = [book for book in self.books if book.judul.lower() == judul.lower()]
        return result

    def search_by_author(self, penulis):
        result = [book for book in self.books if book.penulis.lower() == penulis.lower()]
        return result

    def search_by_year(self, tahun):
        result = [book for book in self.books if book.tahun == tahun]
        return result

def main():
    collection = BookCollection()

    # untuk menginput buku
    for _ in range(5):  # 5 penulis
        penulis = input("Masukkan nama penulis: ")
        for i in range(1, 4):  # 3 buku per penulis
            judul = input(f"Masukkan judul buku ke-{i} dari {penulis}: ")
            tahun = int(input(f"Masukkan tahun terbit buku ke-{i} dari {penulis}: "))
            collection.add_book(Book(judul, penulis , tahun))

    while True:
        print("\nMenu Pencarian:")
        print("1. Cari berdasarkan judul")
        print("2. Cari berdasarkan penulis")
        print("3. Cari berdasarkan tahun")
        print("4. Keluar")
        
        choice = int(input("Pilih opsi pencarian (1/2/3/4): "))

        if choice == 1:
            search_judul = input("Masukkan judul buku yang ingin dicari: ")
            result_judul = collection.search_by_judul(search_judul)
            if result_judul:
                print(f"Hasil pencarian berdasarkan judul '{search_judul}':")
                for book in result_judul:
                    print(f"Judul: {book.judul}, Penulis: {book.penulis}, Tahun: {book.tahun}")
            else:
                print(f"Tidak ada buku dengan judul '{search_judul}' ditemukan.")
        
        elif choice == 2:
            search_penulis = input("Masukkan nama penulis yang ingin dicari: ")
            result_penulis = collection.search_by_penulis(search_penulis)
            if result_penulis:
                print(f"Hasil pencarian berdasarkan penulis '{search_penulis}':")
                for book in result_penulis:
                    print(f"Judul: {book.judul}, Penulis: {book.penulis}, Tahun: {book.tahun}")
            else:
                print(f"Tidak ada buku dengan penulis '{search_penulis}' ditemukan.")
        
        elif choice == 3:
            search_tahun = int(input("Masukkan tahun terbit buku yang ingin dicari: "))
            result_tahun = collection.search_by_tahun(search_tahun)
            if result_tahun:
                print(f"Hasil pencarian berdasarkan tahun '{search_tahun}':")
                for book in result_tahun:
                    print(f"Judul: {book.judul}, Penulis: {book.penulis}, Tahun: {book.tahun}")
            else:
                print(f"Tidak ada buku dengan tahun '{search_tahun}' ditemukan.")
        
        elif choice == 4:
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()
