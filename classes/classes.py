class Book:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.title = ""
        self.publisher = ""
        self.author = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page


#*******************************#

# To create an instance of the class, you type the name of the class and put parenthesis after it.
# You should always store the object instance in a variable.

mockingbird = Book()

mockingbird.title = "To Kill a Mockingbird"
mockingbird.publisher = "Penguin Books"
mockingbird.author = "Harper Lee"
mockingbird.year_published = 1960
mockingbird.publisher = "J. B. Lippincott & Co."

for prop, value in mockingbird.__dict__.items():
    print(f'{prop}:\n{value}\n')

'''
title:
To Kill a Mockingbird

publisher:
J. B. Lippincott & Co.

author:
Harper Lee

current_page:
1

year_published:
1960

currently_reading:
False
'''
