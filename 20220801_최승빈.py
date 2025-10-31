#===========================================
# Node 클래스
#===========================================
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node

#===========================================
# Book 클래스
#===========================================
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[책 번호: {self.book_id} / 제목: {self.title} / 저자: {self.author} / 출판 연도: {self.year}]"

#===========================================
# LinkedList 클래스
#===========================================
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, book):   # 노드 삽입

        if self.find_by_id(book.book_id):  # 책 번호 중복
            print("중복된 책 번호입니다.")
            return False

        if self.find_by_title(book.title): # 책 제목 중복
            print("중복된 책 제목입니다.")
            return False

        new_node = Node(book)
        if self.isEmpty():
            self.head = new_node
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = new_node
        print("도서가 추가되었습니다.")
        return True

    def find_by_id(self, book_id):  # 책 번호로 검색
        current = self.head
        while current:
            if current.data.book_id == book_id:
                return current.data
            current = current.link
        return None

    def find_by_title(self, title):  # 책 제목으로 검색
        current = self.head
        while current:
            if current.data.title == title:
                return current.data
            current = current.link
        return None

    def find_pos_by_title(self, title):  # 책 제목으로 위치 찾기
        current = self.head
        prev = None
        while current:
            if current.data.title == title:
                return prev, current
            prev = current
            current = current.link
        return None, None

    def deleted_by_title(self, title):  # 책 제목으로 삭제
        prev, current = self.find_pos_by_title(title)
        if current is None:
            print("도서를 찾을 수 없습니다.")
            return False
        if prev is None:
            self.head = current.link
        else:
            prev.link = current.link
        print("도서가 삭제되었습니다.")
        return True

    def display_all(self):  # 전체 리스트 출력
        if self.isEmpty():
            print("등록된 도서가 없습니다.")
            return
        current = self.head
        print("등록된 도서 목록: \n")
        while current:
            print(current.data)
            current = current.link

#===========================================
# BookManagement 클래스
#===========================================
class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):  # 책 추가
        book = Book(book_id, title, author, year)
        self.books.insert(book)

    def remove_book(self, title):  # 책 삭제
        self.books.deleted_by_title(title)

    def search_book(self, title):  # 책 검색
        book = self.books.find_by_title(title)
        if book:
            print(f"조회 결과: \n{book}")
        else:
            print("도서를 찾을 수 없습니다.")

    def display_books(self):  # 전체 책 리스트 출력
        self.books.display_all()

    def run(self):  # 인터페이스
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")

            choice = input("메뉴를 선택하세요: ")

            if choice == '1':
                try:
                    book_id = int(input("책 번호: "))
                    title = input("책 제목: ")
                    author = input("저자: ")
                    year = int(input("출판 연도: "))
                    self.add_book(book_id, title, author, year)
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력하세요.")

            elif choice == '2':
                title = input("삭제할 책 제목: ")
                self.remove_book(title)

            elif choice == '3':
                title = input("조회할 책 제목: ")
                self.search_book(title)

            elif choice == '4':
                self.display_books()

            elif choice == '5':
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 1~5 사이의 번호를 입력하세요.")

#===========================================
# 메인
#===========================================
if __name__ == "__main__":
    B = BookManagement()
    B.run()




