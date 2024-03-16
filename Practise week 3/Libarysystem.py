class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []

    def borrow_item(self, item):
        self.borrowed_items.append(item)

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            return True
        else:
            return False
    
class Item:
    def __init__(self, title, item_id, item_category):
        self.title = title
        self.item_id = item_id
        self.item_category = item_category

class Library:
    def __init__(self):
        self.members = []
        self.items = []

    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)

    def add_item(self, title, item_id, item_category):
        item = Item(title, item_id, item_category)
        self.items.append(item)

    def get_member_with_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    def get_item_with_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None
    
    def search_members(self, query):
        results = []
        for member in self.members:
            if query.lower() in member.name.lower() or str(query) == str(member.member_id):
                results.append(member)
        return results
    
    def search_items(self, query):
        results = []
        for item in self.items:
            if query.lower() in item.title.lower() or str(query) == str(item.item_id):
                results.append(item)
        return results

    def search_library(self):
        search_type = input("Enter 'M' to search for members, 'I' to search for items: ").strip().upper()
        query = input("Enter your search question: ").strip()
        if search_type == 'M':
            results = self.search_members(query)
            print("Search results for members:")
            for member in results:
                print(f"Name: {member.name}, ID: {member.member_id}")
        elif search_type == 'I':
            results = self.search_items(query)
            print("Search results for items:")
            for item in results:
                print(f"Title: {item.title}, ID: {item.item_id}")
        else:
            print("Invalid search type.")

if __name__ == "__main__":
    library = Library()

    library.add_member("Danielle Ronnen", 1)
    library.add_member("John Doe", 2)
    library.add_member("Jane Doe", 3)

    library.add_item("IT for dummies", 1001, "book")
    library.add_item("Programming for beginners", 102, "book")
    library.add_item("Penny", 301, "magazine")

    member = library.get_member_with_id(1)
    item = library.get_item_with_id(1001)
    member.borrow_item(item)

    member = library.get_member_with_id(1)
    item = library.get_item_with_id(1001)
    returned = member.return_item(item)
    if returned:
        print("Item returned")
    else:
        print("Item not found in borrowed items")

    library.search_library()
