import tkinter as tk

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book, borrow_time, book_location):
        if book not in self.books:
            self.books[book] = {"borrow_time": borrow_time, "location": book_location}
            return f"添加書籍：{book}"
        else:
            return f"{book} 已經被借出"

    def drop(self, book):
        if book in self.books:
            del self.books[book]
            return f"歸還書籍：{book}"
        else:
            return f"{book} 並不在圖書館內"

    def find_book(self, book_name):
        if book_name in self.books:
            book_info = self.books[book_name]
            borrow_time = book_info["borrow_time"]
            book_location = book_info["location"]
            return f"{book_name} 的書已借出，借出時間為：{borrow_time} 圖書位置: {book_location}"
        else:
            return f"{book_name} 的書未被借出或不存在於圖書館"

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("圖書館管理系統")

        self.library = Library()

        self.label_book = tk.Label(root, text="書名：")
        self.label_book.pack()

        self.entry_book = tk.Entry(root)
        self.entry_book.pack()

        self.label_borrow_time = tk.Label(root, text="借出時間：")
        self.label_borrow_time.pack()

        self.entry_borrow_time = tk.Entry(root)
        self.entry_borrow_time.pack()

        self.label_location = tk.Label(root, text="書籍位置：")
        self.label_location.pack()

        self.entry_location = tk.Entry(root)
        self.entry_location.pack()

        self.add_book_button = tk.Button(root, text="添加書籍", command=self.add_book)
        self.add_book_button.pack()

        self.find_book_button = tk.Button(root, text="查找書籍", command=self.find_book)
        self.find_book_button.pack()

        self.drop_book_button = tk.Button(root, text="歸還書籍", command=self.drop_book)
        self.drop_book_button.pack()

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

    def add_book(self):
        book = self.entry_book.get()
        borrow_time = self.entry_borrow_time.get()
        book_location = self.entry_location.get()
        result = self.library.add_book(book, borrow_time, book_location)
        self.output_label.config(text=result)

    def find_book(self):
        book = self.entry_book.get()
        result = self.library.find_book(book)
        self.output_label.config(text=result)

    def drop_book(self):
        book = self.entry_book.get()
        result = self.library.drop(book)
        self.output_label.config(text=result)

root = tk.Tk()
app = LibraryGUI(root)
root.mainloop()
