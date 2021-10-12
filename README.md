## Movie Rental Refactoring Example

This [refactoring example][refactoring_pdf] is from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

There are two branches in this repository:

* `java` contains Java source code, updated to use current Java features
* `python` contains Python source, translated from the Java code

The Java code has been updated to use features such as a List with type
parameter instead of Vector and type casts, and the for-each loop. 
I also removed the leading underscore on attribute names (`name` instead of `_name`),
which is more typical of current coding conventions.

The runnable Main class (or Python `main.py`) creates a customer and prints 
a statement.

The [PDF from Chapter 1][refactoring_pdf] explains the 
motivation for each refactoring and how to do it.

## Instructions

- Check out either the `java` or `python` branch (your choice).
- Perform the 5 refactorings listed below, and optionally the 6th "missing" refactoring.
- Before starting to refactor, run the units tests. They should all pass.
- After each refactoring **run the unit tests** again. They should still pass.
- After a refactoring passes tests and your own code review, commit it to your personal repo.
- When done everything, push your solution to Github.

The refactorings are (filenames refer to Java version):

1. *Extract Method*.  In Customer.statement() extract the code that calculates the price of each rental.
   - Make it a separate method.
2. *Move Method*. After extracting a method to calculate the price of a rental,
Fowler observes that the method uses information about the rental but not 
about the customer.  Hence, the method should be in the `Rental` class instead
of `Customer` class. 
   - Move the method to the `Rental` class. A good IDE has a refactoring tool to do this for you.
   - After the change, verify that the method is referenced correctly in code.  It changes from:
    ```java
    // Customer class:
    public double amountFor(Rental rental) { ... }
    
    charge = amountFor(rental);
    ```
    to:
    ```java
    // Rental class:
    public double getCharge() { ... }
    // Customer class:
    charge = rental.getCharge();
    ```
    - write a unit test for this method.
3. *Replace Temp Variable with a Query*.  Instead of using `charge = rental.getCharge()` (assign to a temp variable) and using `charge` in the code, directly invoke `rental.getCharge()` wherever the value is needed. 
   - This removes the local variable but results to multiple method calls for the same thing.
   - Personally, I prefer using a temporary variable instead of duplicate method calls.
4. *Extract Method*. Refactor summation of frequent renter points to a separate method.
   - write a unit test for this new method
5. *Replace Conditional Logic with Polymorphism*.  Replaces the "switch" statement for movie price codes with polymorphism, in two steps.
   - The first step is to make the Movie class compute its own frequent renter points.
   - The second step is have it delegate that task to a Strategy object.
   - You define an interface (e.g. PriceStrategy) and concrete implementations for RegularPrice, ChildrensPrice, NewReleasePrice. The strategy interface also computes frequent renter points.
   - Replace the constant for price code with objects from the strategy classes. 
   - In Fowler's article, this is a long refactoring because he first uses inheritance and then explains why that's a poor solution.
   - This refactoring uses the design principle "*Prefer composition over inheritance*".

6. *The Missing Refactoring*.  In the final code the `Customer` class still needs a *Move Method* refactoring to remove some unrelated behavior, in my opinion.  
   - What do you think?

### Python Version

In Python, the refactoring are the same, but some details are different.

* method names should use Python naming convention
* Python does not require creating an interface for strategy. If you want to write code like Java, you can create an abstract superclass (`PriceStrategy`) for the interface with methods that return 0.  `RegularPrice`, etc., are concrete subclasses of `PriceStrategy`. 
* Another way to implement Strategy in Python is to use an Enum. 
  - Each member of the enum is one pricing strategy (normal, childrens, new\_release).
  - Each enum member is a dict, and the *values* in the dict are lambdas to compute the price and frequent renter points.  In this way, each number member can define it's own function for pricing and frequent renter points.
    ```python
    from enum import Enum

    class PriceCode(Enum):
        """An enumeration for different kinds of movies and their behavior"""
        new_release = { "price": lambda days: 3.0*days, 
                        "frp": lambda days: days
                      }
        normal = { "price": lambda days: ...,
                   "frp": lambda days: ...
                 }
        childrens = { ... 
                 }

        def price(self, days: int) -> float:
            "Return the rental price for a given number of days"""
            pricing = self.value["price"]    # the enum member's price formula
            return pricing(days)
    ```
   - The Enum provides methods for `price` and renter points, and *delegates* those methods to the enum member (which is referenced by `self`).  The `price` metho (shown above) uses the enum member's dict (`values`) to get a lambda expression it should use to compute the rental price, then uses that lambda to compute the actual price.
   - To reference a member of the PriceCode enum, you write:
     ```python
     movie_type = PriceCode.new_release
     # invoke a method of PriceCode
     print("Rental price for 3 days:", movie_type.price(3))
     ```

[refactoring_pdf]: https://cpske.github.io/ISP/refactoring/refactoring-movierental.pdf

## Resources

* [Refactoring, First Example][refactoring_pdf] extract from Martin Fowler's *Refactoring* book. 
* [Refactoring slides from U. Colorado](https://www.cs.colorado.edu/~kena/classes/6448/s05/lectures/lecture19.pdf) step-by-step instructions for Java version of this example, including UML class diagram of progress.
