#from book_class import Book
#from library_system import Book, EBook, PrintBook, Library
#from polymorphism_demo import Shape, Rectangle, Circle
from class_static_methods_demo import Calculator
def main():
    # Creating an instance of Book
    #my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    
    #print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    #print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    #del my_book



    #my_library = Library()

    #classic_book = Book("Pride and Prejudice", "Jane Austen")
    #digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    #paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    #my_library.add_book(classic_book)
    #my_library.add_book(digital_novel)
    #my_library.add_book(paper_novel)

    #my_library.list_books()
    
    # main.py



    #shapes = [
       # Rectangle(10, 5),
       # Circle(7)
    #]

   # for shape in shapes:
        #print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

    

    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
if __name__ == "__main__":
    main()