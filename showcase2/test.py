
import pprint

# Single line comments start with a number symbol.

""" 
    Multiline strings can be written
    using three "s, and are often used
    as comments
"""

"Hello " + "world!"

print("Hello" * 3)


# A string can be treated like a list of characters
print("This is a string"[0])  # => 'T'
# A newer way to format strings is the format method.
print("{} is a {}".format("This", "placeholder"))
print("{0} can be {1}".format("strings", "formatted"))
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead
"etc" is None  # => False
None is None  # => True

print(bool(0))
print(bool(()))
print(bool(""))
print(type("abc"))
print(eval('1'+'2'))

print("I'm Python. Nice to meet you!")

some_var = 5

if some_var > 10:
    print ("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print( "some_var is smaller than 10.")
else:           # This is optional too.
    print("some_var is indeed 10.")
    
for animal in ["dog", "cat", "mouse"]:
    # You can use {0} to interpolate formatted strings. (See above.)
    print( "{0} is a mammal".format(animal)    )
    
for i in range(4):
    print( i)    
    
for i in range(4, 8):
    print(i)
    
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1    

try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass    # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass    # Multiple exceptions can be handled together, if required.
else:   # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally: #  Execute under all circumstances
    print("We can clean up resources here")    
    
    
with open("myfile.txt") as f:
    for line in f:
        print(line)
    
# Use "def" to create new functions
def add(x, y):
    print("x is {0} and y is {1}".format(x, y))
    return x + y    # Return values with a return statement

print(add(2,5))

add(y=6, x=5)   # Keyword arguments can arrive in any order.

# You can define functions that take a variable number of
# positional args, which will be interpreted as a tuple by using *
def varargs(*args):
    return args

print(varargs(1, 2, 3))   # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword args, as well, which will be interpreted as a dict by using **
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
print(keyword_args(big="foot", loch="ness"))   # => {"big": "foot", "loch": "ness"}

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)   # equivalent to foo(1, 2, 3, 4)
all_the_args(**kwargs)   # equivalent to foo(a=3, b=4)
all_the_args(*args, **kwargs)   # equivalent to foo(1, 2, 3, 4, a=3, b=4)


# Function Scope
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num # => 43
    print( x )# => 43

def set_global_x(num):
    global x
    print(x)# => 5
    x = num # global var x is now set to 6
    print(x) # => 6

set_x(43)
set_global_x(6)


# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)   # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1) # => 5

####################################################
## 5. Classes
####################################################

# We subclass from object to get a class.
class Human(object):

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self.age = 0


    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        return "{0}: {1}".format(self.name, msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument

    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference

    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into an read-only attribute
    # of the same name.

    def age(self):
        return self.age

    # This allows the property to be set

    def age(self, age):
        self.age = age

    # This allows the property to be deleted

    def age(self):
        del self.age


# Instantiate a class
i = Human(name="Ian")
print(i.say("hi"))     # prints out "Ian: hi"

j = Human("Joel")
print(j.say("hello"))  # prints out "Joel: hello"

# Call our class method
i.get_species()   # => "H. sapiens"

# Change the shared attribute
Human.species = "H. neanderthalensis"
i.get_species()   # => "H. neanderthalensis"
j.get_species()   # => "H. neanderthalensis"

# Call the static method
Human.grunt()   # => "*grunt*"

# Update the property
i.age = 42

# Get the property
i.age # => 42

# Delete the property
del i.age
i.age  # => raises an AttributeError

data = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )

print(data)
pprint.pprint(data)

