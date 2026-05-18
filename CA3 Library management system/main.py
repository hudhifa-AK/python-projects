import random
import datetime #https://www.w3schools.com/python/python_datetime.asp

class Item(object):
    def __init__(self, title, year, author, library_id, available=True):
        self.item_id = self.generate_id()
        self.title = title
        self.year = year
        self.author = author
        self.available = available
        self.library_id = library_id

    def save_item(self):
        """Saves an item to the items.txt file"""

        item_type = self.__class__.__name__ #get name of class (Book, Article, etc.)

        line = (f"{self.item_id} | "
                f"{item_type} | "
                f"{self.title} | "
                f"{self.author} | "
                f"{self.year} | "
                f"{self.available} | "
                f"{self.library_id}")

        extra_info = self.get_extra_info() #Subclasses have extra attributes and this method will get them

        if extra_info:
            line += f" | {extra_info}"

        line += "\n" #new line added in the end even if there wasn't extra info

        with open("items.txt", "a") as save_file:
            save_file.write(line)

    def get_extra_info(self):
        """Returns extra info about the item from subclasses"""
        return ""

    def generate_id(self):
        """Generates a unique id consisting of the first letter of a class (e.g. I for Item) and three digits"""
        id_list = [] #populate a list with all saved IDs
        with open("items.txt", "r") as save_file:
            for line in save_file:
                line = line.strip()
                id_list.append(line.split(" | ")[0])

        while True: #make a random ID not in the list
            random_number = random.randint(0, 999)
            new_id = f"{self.__class__.__name__[0]}{random_number:03d}"

            if new_id not in id_list:
                return new_id

    def change_title(self, new_title: str):
        """Changes the title of the item"""
        self.title = new_title

    def change_author(self, new_author: str):
        """Changes the author of the item"""
        self.author = new_author

    def change_year(self, new_year: int):
        """Changes the year of the item"""
        try:
            new_year = int(new_year)

            if new_year > datetime.date.today().year:
                print("Invalid year")
            else:
                self.year = new_year

        except ValueError:
            print("Year must be a number")

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.item_id == other.item_id

        return False

    def __str__(self):
        return (f"Available: {self.available}\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}\n")


class Book(Item):
    def __init__(self, title, year, author, library_id, isbn, pages, available=True):
        Item.__init__(self, title, year, author, library_id, available)
        self.isbn = isbn
        self.__pages = pages

    def how_many_pages(self):
        """Returns the number of pages in the book"""
        return self.__pages

    def get_extra_info(self):
        """Returns ISBN and page number of the book"""
        return f"{self.isbn} | {self.how_many_pages()}"

    def __str__(self):
        return (f"{Item.__str__(self)}"
                f"Pages: {self.how_many_pages()}\n"
                f"ISBN: {self.isbn}\n")

class Article(Item):
    def __init__(self, title, year, author, library_id, journal, issue, available=True):
        Item.__init__(self, title, year, author, library_id, available)
        self.journal = journal
        self.issue = issue

    def get_extra_info(self):
        """Returns journal and issue that the article is in"""
        return f"{self.journal} | {self.issue}"

    def __str__(self):
        return (f"{Item.__str__(self)}"
                f"Journal: {self.journal}\n"
                f"Issue: {self.issue}\n")

class DigitalMedia(Item):
    def __init__(self, title, year, author, library_id, media_format, available=True):
        Item.__init__(self, title, year, author, library_id, available)
        self.media_format = media_format

    def get_extra_info(self):
        """Returns media format of the Digital Media Item"""
        return self.media_format

    def __str__(self):
        return (f"{Item.__str__(self)}"
                f"Media format: {self.media_format}\n")

class Member(object):
    def __init__(self, name, email, phone):
        self.member_id = self.generate_id()
        self.name = name
        self.email = email
        self.phone = phone
        self.join_date = datetime.date.today().strftime('%d/%m/%Y') #gets today's date
        self.__fines = 0

    def generate_id(self):
        """Generates a unique id consisting of the first letter of a class (e.g. I for Item) and three digits"""
        id_list = [] #populate a list with all saved IDs
        with open("members.txt", "r") as save_file:
            for line in save_file:
                line = line.strip()
                id_list.append(line.split(" | ")[0])

        while True: #make a random ID not in the list
            random_number = random.randint(0, 999)
            new_id = f"{self.__class__.__name__[0]}{random_number:03d}"

            if new_id not in id_list:
                return new_id

    def save_member(self):
        """Saves a new member to the members.txt file"""

        membership_type = self.__class__.__name__

        line = (f"{self.member_id} | "
                f"{membership_type} | "
                f"{self.name} | "
                f"{self.email} | "
                f"{self.phone} | "
                f"{self.join_date} | "
                f"{self.__fines}\n")

        with open("members.txt", "a") as save_file:
            save_file.write(line)

    def update_fines(self, return_date:str):
        """Checks how late the return is in days and adds a fine for every 7 days passed plus a base fine"""
        # getting amount of days and calculating difference
        return_date_days = return_date.split("/")
        return_date_days = int(return_date_days[0]) + int(return_date_days[1]) * 30 + int(return_date_days[2]) * 365
        todays_date = datetime.date.today()
        todays_date_days = todays_date.year * 365 + todays_date.month * 30 + todays_date.day

        late_days = todays_date_days - return_date_days

        if late_days >= 1:
            self.__fines = late_days // 7 * 10 + 10

    def get_fines(self):
        return self.__fines

    def set_fines(self, amount: int):
        self.__fines = amount

    def pay_fines(self, payment):
        """Takes payment and updates member's fines"""

        if payment <= 0:
            print("Invalid payment")
            return

        self.__fines -= payment

        if self.__fines < 0:
            print("Payment successful!")
            print("You have overpaid by ", -self.__fines)
            print("Please collect the remainder of your balance.")
            self.__fines = 0
            print("Payment: ", payment)
            print("Remaining Fines Due: ", self.__fines)
            print("Your account is clear!")

        elif self.__fines > 0:
            print("Payment successful!")
            print("Payment: ", payment)
            print("Remaining Fines Due: ", self.__fines)

        else:
            print("Payment successful!")
            print("Payment: ", payment)
            print("Remaining Fines Due: ", self.__fines)
            print("Your account is clear!")

    def change_name(self, new_name):
        self.name = new_name

    def change_email(self, new_email):
        self.email = new_email

    def change_phone(self, new_phone):

        if len(new_phone) != 10:
            print("Invalid phone number")

        else:
            self.phone = new_phone

    def __eq__(self, other):
        if isinstance(other, Member):
            return self.member_id == other.member_id

        return False

    def __str__(self):
        return (f"ID: {self.member_id}\n"
                f"Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n"
                f"Join Date: {self.join_date}\n")

class Library(object):
    def __init__(self):
        self.items = {}
        self.members = {}
        self.borrowing_members = {}
        self.borrowed_items = {}
        self.transactions = {}

    def load_items(self):
        """Processes items.txt into objects and adds them to a dict"""
        self.items = {}
        with open("items.txt", "r") as save_file:
            for line in save_file:
                line = line.strip().split(" | ")

                item_id = line[0]
                item_type = line[1]
                title = line[2]
                author = line[3]
                year = int(line[4])
                available = line[5] == 'True'
                library_id = line[6]

                if item_type == "Book":

                    isbn = line[7]
                    pages = int(line[8])

                    item = Book(
                                title,
                                year,
                                author,
                                library_id,
                                isbn,
                                pages,
                                available
                            )

                elif item_type == "Article":

                    journal = line[7]
                    issue = line[8]

                    item = Article(
                                    title,
                                    year,
                                    author,
                                    library_id,
                                    journal,
                                    issue,
                                    available
                                )

                elif item_type == "DigitalMedia":

                    media_format = line[7]

                    item = DigitalMedia(
                                        title,
                                        year,
                                        author,
                                        library_id,
                                        media_format,
                                        available
                                    )

                else:
                    continue

                # restore original ID because initialising new Items generates a new ID
                item.item_id = item_id
                self.items[item_id] = item

    def save_items(self):
        """Updates the items.txt file"""
        open("items.txt", "w").close() # Clears items.txt
        for item in self.items.values():
            item.save_item()

    def add_new_item(self, item):
        """Adds a new item to the current library instance's items list"""
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        """Removes an item using its ID"""

        item_borrowed = self.borrowed_items.get(item_id)

        if item_borrowed and item_borrowed[5] == "False":
            print("Can't remove borrowed item")
            return False

        elif item_id in self.items:
            del self.items[item_id]
            return True

        else:
            print("Item not found.")
            return False

    def load_members(self):
        """Processes members.txt into objects and adds them to a dict"""
        self.members = {}
        with open("members.txt", "r") as save_file:
            for line in save_file:
                line = line.strip().split(" | ")

                member_id = line[0]
                # membership_type = line[1] # Not used yet (for making member subclasses)
                name = line[2]
                email = line[3]
                phone = line[4]
                join_date = line[5]
                fine = int(line[6])

                member = Member(
                                name,
                                email,
                                phone
                               )

                # restore original information because initialising new members changes data
                member.member_id = member_id
                member.join_date = join_date
                member.set_fines(fine)

                self.members[member_id] = member

    def get_member(self, member_id):
        """Gets a member using their ID"""
        return self.members.get(member_id)

    def save_members(self):
        """Updates the members.txt file"""
        open("members.txt", "w").close() # Clears members.txt
        for member in self.members.values():
            member.save_member()

    def remove_member(self, member_id):
        """Removes a member using their ID"""

        if member_id in self.borrowing_members and member_id in self.members:
            print("Error: Can't remove member until they return borrowed items")
            return False

        elif member_id in self.members:
            del self.members[member_id]
            print("Member removed.")
            return True

        else:
            print("Error: Member not found.")
            return False

    def __iter__(self):
        """Iterates through the items only. Doesn't iterate through the members"""
        return iter(self.items.values())

    def __contains__(self, other):

        if isinstance(other, Item):
            return other.item_id in self.items

        elif isinstance(other, Member):
            return other.member_id in self.members

        return False

    def load_transactions(self):
        """Processes transactions.txt into a dict"""
        self.transactions = {}
        self.borrowing_members = {}
        self.borrowed_items = {}
        with open("borrowing.txt", "r") as save_file:
            for line in save_file:
                line = line.strip().split(" | ")

                transaction_id = line[0]
                member_id = line[1]
                item_id = line[2]
                # borrow_date = line[3]
                return_date = line[4]
                returned = line[5]

                # Add line to dicts
                self.borrowed_items[item_id] = line
                self.transactions[transaction_id] = line

                # updating member fines:
                if returned == "False":
                    member = self.members.get(member_id)
                    member.update_fines(return_date)

                    # Adding members who haven't returned to dict
                    if member_id in self.borrowing_members:
                        self.borrowing_members[member_id].add(item_id)
                    else:
                        self.borrowing_members[member_id] = {item_id}

    def save_transactions(self):
        """Updates the transactions.txt file"""
        with open("borrowing.txt", "w") as save_file:
            for line in self.transactions.values():

                transaction_id = line[0]
                member_id = line[1]
                item_id = line[2]
                borrow_date = line[3]
                return_date = line[4]
                returned = line[5]

                line = (f"{transaction_id} | "
                        f"{member_id} | "
                        f"{item_id} | "
                        f"{borrow_date} | "
                        f"{return_date} | "
                        f"{returned}\n")

                save_file.write(line)

    def borrow_item(self, member_id, item_id):
        """Borrows an item from the library and adds record in borrowing.txt"""

        # Get member and item. If they don't exist then it will give None
        member = self.members.get(member_id)
        item = self.items.get(item_id)

        # Initial checks
        if member is None:
            print("Member not found.")
            return False

        if item is None:
            print("Item not found.")
            return False

        if item.available:
            item.available = False
        else:
            print("Item is already borrowed.")
            return False

        # Get today's date
        borrow_date = datetime.datetime.now().strftime('%d/%m/%Y')
        # Add 14 days to today's date using timedelta https://www.geeksforgeeks.org/python/python-datetime-timedelta-function/
        return_date = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime('%d/%m/%Y')

        returned = False # becomes true when item is returned

        # simple sequential ID system
        total_transactions = 0
        with open("borrowing.txt", "r") as save_file:
            for line in save_file:
                total_transactions += 1

        transaction_id = f"T{total_transactions + 1:06d}"

        line = (f"{transaction_id} | "
                f"{member_id} | "
                f"{item_id} | "
                f"{borrow_date} | "
                f"{return_date} | "
                f"{returned}\n")

        with open("borrowing.txt", "a") as save_file:
            save_file.write(line)

        # Add transaction to the dict
        transaction = [
            transaction_id,
            member_id,
            item_id,
            borrow_date,
            return_date,
            returned
        ]

        self.borrowed_items[item_id] = transaction
        self.transactions[transaction_id] = transaction

        if member_id in self.borrowing_members:
            self.borrowing_members[member_id].add(item_id)
        else:
            self.borrowing_members[member_id] = {item_id}

        return True

    def return_item(self, item_id):
        """Return borrowed item to Library. Updates borrowed items dict and item object"""
        # ---Item---

        # Initial check then update borrow dict
        item_borrowed = self.borrowed_items.get(item_id)

        if item_borrowed is None:
            print("Item not found.")
            return False

        transaction_id = item_borrowed[0]
        transaction = self.transactions.get(transaction_id)

        if transaction is None:
            print("Transaction not found.")
            return False

        # update the borrowed items and transactions dicts
        transaction[5] = "True" # returned
        self.transactions.update({transaction_id: transaction})
        self.borrowed_items.pop(item_id)

        # Update item
        item = self.items.get(item_id)

        if not item.available:
            item.available = True

        # ---Member---

        member_id = transaction[1]

        if member_id in self.borrowing_members:
            self.borrowing_members[member_id].discard(item_id)

            # if member doesn't have borrowed items then del
            if not self.borrowing_members[member_id]:
                del self.borrowing_members[member_id]

        return True

    def edit_item(self, item_id, option, new_value):
        """Change Item Title, Author, or Year"""
        item = self.items.get(item_id)

        if item is None:
            print("Item not found.")
            return False

        if option == "Title":
            item.change_title(new_value)
            self.items.update({item_id: item})
            return True

        elif option == "Author":
            item.change_author(new_value)
            self.items.update({item_id: item})
            return True

        elif option == "Year":
            item.change_year(new_value)
            self.items.update({item_id: item})
            return True

        else:
            return False

    def edit_member(self, member_id, option, new_value):
        """Change Member Name, Email, or Phone"""
        member = self.members.get(member_id)

        if member is None:
            print("Member not found.")
            return False

        if option == "Name":
            member.change_name(new_value)
            self.members.update({member_id: member})
            return True

        elif option == "Email":
            member.change_email(new_value)
            self.members.update({member_id: member})
            return True

        elif option == "Phone":
            member.change_phone(new_value)
            self.members.update({member_id: member})
            return True

        else:
            return False

l = Library()

# Load existing data and if it fails create a new txt file
try:
    l.load_items()
except FileNotFoundError:
    open("items.txt", "a").close()

try:
    l.load_members()
except FileNotFoundError:
    open("members.txt", "a").close()

try:
    l.load_transactions()
except FileNotFoundError:
    open("borrowing.txt", "a").close()

while True: # Main menu system
    print("\n====== WELCOME ======")
    print("1. Admin")
    print("2. Member")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        while True: # Admin menu with all functions
            print("\n====== ADMIN MENU ======")
            print("1. View all Items")
            print("2. View Borrowed Items")
            print("3. Add/Edit/Remove Item")
            print("4. Borrow Item")
            print("5. Return Item")
            print("6. View Members")
            print("7. Add/Edit/Remove Member")
            print("8. Back to Start Menu")

            choice = input("Enter choice: ")

            # --- VIEW ITEMS ---
            if choice == "1":
                for item in l.items.values():
                    print("\n----------------")
                    print(item)

            # --- VIEW BORROWED ---
            elif choice == "2":
                for item in l.items.values():
                    if not item.available:
                        print("\n----------------")
                        print(item)


            # --- ADD/EDIT/REMOVE ITEM ---
            elif choice == "3":

                while True:

                    print("\n====== ITEM MENU ======")
                    print("1. Add Book")
                    print("2. Add Article")
                    print("3. Add Digital Media")
                    print("4. Edit an Item")
                    print("5. Remove Item")
                    print("6. Back")

                    choice = input("Enter choice: ")

                    # --- ADD BOOK ---
                    if choice == "1":
                        title = input("Title: ")
                        year = int(input("Year: "))
                        author = input("Author: ")
                        library_id = input("Library ID: ")
                        isbn = input("ISBN: ")
                        pages = int(input("Pages: "))

                        book = Book(title, year, author, library_id, isbn, pages)
                        l.add_new_item(book)
                        l.save_items()
                        print("Book added.")

                    # --- ADD ARTICLE ---
                    elif choice == "2":
                        title = input("Title: ")
                        year = int(input("Year: "))
                        author = input("Author: ")
                        library_id = input("Library ID: ")
                        journal = input("Journal: ")
                        issue = input("Issue: ")

                        article = Article(title, year, author, library_id, journal, issue)
                        l.add_new_item(article)
                        l.save_items()
                        print("Article added.")

                    # --- ADD DIGITAL MEDIA ---
                    elif choice == "3":
                        title = input("Title: ")
                        year = int(input("Year: "))
                        author = input("Author: ")
                        library_id = input("Library ID: ")
                        media_format = input("Format (e.g. PDF, MP3): ")

                        media = DigitalMedia(title, year, author, library_id, media_format)
                        l.add_new_item(media)
                        l.save_items()
                        print("Digital media added.")

                    # --- EDIT ITEM ---
                    elif choice == "4":
                        item_id = input("Item ID: ")
                        print(l.items.get(item_id))

                        option = input("What are you editing?\n"
                                       "1. Item Title\n"
                                       "2. Item Year\n"
                                       "3. Item Author\n")

                        if option == "1":
                            option = "Title"

                        elif option == "2":
                            option = "Year"

                        elif option == "3":
                            option = "Author"

                        else:
                            print("Invalid option. Try again.")

                        print(l.items.get(item_id))

                        new_value = input(f"Enter new {option}: ")

                        if l.edit_item(item_id, option, new_value):
                            l.save_items()
                            print("Item edited successfully.")
                        else:
                            print("Operation failed.")

                    # --- REMOVE ITEM ---
                    elif choice == "5":
                        item_id = input("Item ID: ")

                        if l.remove_item(item_id):
                            l.save_items()
                            print("Item removed successfully.")

                    # --- BACK ---
                    elif choice == "6":
                        l.save_items()
                        break

                    else:
                        print("Invalid option. Try again.")

            # --- BORROW ITEM ---
            elif choice == "4":
                member_id = input("Member ID: ")
                item_id = input("Item ID: ")

                if l.borrow_item(member_id, item_id):
                    l.save_items()
                    l.save_transactions()
                    print("Item borrowed successfully.")

            # --- RETURN ITEM ---
            elif choice == "5":
                item_id = input("Item ID: ")

                if l.return_item(item_id):
                    l.save_items()
                    l.save_transactions()
                    print("Item returned successfully.")

            # --- VIEW MEMBERS ---
            elif choice == "6":
                for member in l.members.values():
                    print("\n----------------")
                    print(member)

                    if member.get_fines() != 0:
                        print("^^ This member has outstanding fines.")
                        print("Fine Total: ", member.get_fines())

                    if member.member_id in l.borrowing_members:
                        print("Member borrowing the following: ")
                        items = l.borrowing_members.get(member.member_id)
                        for item in items:
                            print(l.items.get(item))

            # --- ADD/EDIT/REMOVE MEMBER ---
            elif choice == "7":
                while True:

                    print("\n====== MEMBER MENU ======")
                    print("1. Add Member")
                    print("2. Edit Member")
                    print("3. Remove Member")
                    print("4. Back")

                    choice = input("Enter choice: ")

                    # --- ADD MEMBER ---
                    if choice == "1":
                        name = input("Name: ")
                        email = input("Email: ")
                        phone = input("Phone: ")

                        member = Member(name, email, phone)
                        l.members[member.member_id] = member
                        l.save_members()
                        print("Member added. ID:", member.member_id)

                    # --- EDIT MEMBER ---
                    elif choice == "2":
                        member_id = input("Member ID: ")
                        print(l.members.get(member_id))

                        option = input("What are you editing?\n"
                                       "1. Member Name\n"
                                       "2. Member Email\n"
                                       "3. Member Phone\n")

                        if option == "1":
                            option = "Name"

                        elif option == "2":
                            option = "Email"

                        elif option == "3":
                            option = "Phone"

                        else:
                            print("Invalid option. Try again.")

                        print(l.members.get(member_id))

                        new_value = input(f"Enter new {option}: ")

                        if l.edit_member(member_id, option, new_value):
                            l.save_members()
                            print("Member details edited successfully.")
                        else:
                            print("Operation failed.")

                    # --- REMOVE MEMBER ---
                    elif choice == "3":
                        member_id = input("Member ID: ")

                        if l.remove_member(member_id):
                            l.save_members()
                            print("Success!")
                        else:
                            print("Operation failed.")

                    # --- BACK ---
                    elif choice == "4":
                        l.save_items()
                        break

                    else:
                        print("Invalid option. Try again.")

            # --- BACK TO MAIN MENU ---
            elif choice == "8":
                l.save_items()
                l.save_members()
                l.save_transactions()
                break

            else:
                print("Invalid option. Try again.")

    elif choice == "2":

        while True: # MEMBER MENU
            print("\n====== MEMBER MENU ======")
            print("1. View All Items")
            print("2. View Available Items")
            print("3. Borrow Item")
            print("4. Return Item")
            print("5. Pay fines")
            print("6. Back to Start menu")

            choice = input("Enter choice: ")

            # --- VIEW ITEMS ---
            if choice == "1":
                for item in l.items.values():
                    print("\n----------------")
                    print(item)

            # --- VIEW AVAILABLE ---
            elif choice == "2":
                for item in l.items.values():
                    if item.available:
                        print("\n----------------")
                        print(item)

            # --- BORROW ITEM ---
            elif choice == "3":
                member_id = input("Member ID: ")
                item_id = input("Item ID: ")

                if l.borrow_item(member_id, item_id):
                    l.save_items()
                    l.save_transactions()
                    print("Item borrowed successfully.")

            # --- RETURN ITEM ---
            elif choice == "4":
                item_id = input("Item ID: ")

                if l.return_item(item_id):
                    l.save_items()
                    l.save_transactions()
                    print("Item returned successfully.")

            # --- PAY FINES ---
            elif choice == "5":

                member_id = input("Member ID: ")
                member = l.get_member(member_id)

                if member:
                    print("Current fines:", member.get_fines())
                    if member.get_fines() != 0:
                        amount = int(input("Payment amount: "))
                        member.pay_fines(amount)
                        l.save_members()

                else:
                    print("Member not found.")

            # --- BACK TO MAIN MENU ---
            elif choice == "6":
                l.save_items()
                l.save_members()
                l.save_transactions()
                break

            else:
                print("Invalid option. Try again.")

    elif choice == "3":
        l.save_items()
        l.save_members()
        l.save_transactions()
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
