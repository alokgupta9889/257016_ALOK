#Task
#write a python code on book system
# make function and store the data in dictionary atleast five books 
# user call the number of the book and that book need to be displayd

def book_system ():
    books = {  
        1:"Rich dad poor dad",
        2:"The rise of hindus",
        3:"The Ramcharitmannas",
        4:"The naga warriors",
        5:"psychology of money",
    }
    print("available books")
    num=int(input("enter:"))

    if num in books:
        print(f"Book is {books[num]}")
    else:
        print("Not Availabel")
book_system()