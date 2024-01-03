
class Library:
    def __init__(self, id, year, author):
        self.id = id
        self.year = year
        self.author = author
        self.books = {}

    def add_book(self, book, borrow_time, book_location):
        if book not in self.books:
            self.books[book] = {"borrow_time": borrow_time, "location": book_location}
            print(f"借閱：{book} ID: {self.id} 年份: {self.year} 作者: {self.author} 借出時間: {borrow_time}  館藏位置: {book_location}")
        else:
            print(f"{book} 已經被借出")

    def drop(self, book):
        if book in self.books:
            del self.books[book]
            print(f"還書：{book} ID: {self.id} 年份: {self.year} 作者: {self.author}")
        else:
            print(f"{book} 並不在圖書館內")

    def find_book(self, book_name):
        if book_name in self.books:
            book_info = self.books[book_name]
            borrow_time = book_info["borrow_time"]
            book_location = book_info["location"]
            print(f"{book_name} 的書已借出，借出時間為：{borrow_time} 圖書位置: {book_location}")
        else:
            print(f"{book_name} 的書未被借出或不存在於圖書館")



student1 = Library("s001", "2022", "Peter")
student2 = Library("s002", "2023", "John")


student1.add_book("AI", "2024.01.04", "3F-02")
student2.add_book("Python", "2024.01.01", "2F-03")

student1.find_book("AI")
student2.find_book("Python")


student1.drop("AI")
student1.find_book("AI")
