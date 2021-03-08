class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

"""
//Instance Methods

Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.
"""

"""
Class Methods

Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.
"""

"""
Static Methods


The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.

This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
"""


#Instance method
obj = MyClass()
obj.method()
"""
When the method is called, Python replaces the self argument with the instance object, obj. We could ignore the syntactic sugar of the dot-call syntax (obj.method()) and pass the instance object manually to get the same result:
"""
MyClass.method(obj)


#class method
obj.classmethod()

"""
Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class MyClass> object, representing the class itself (everything in Python is an object, even classes themselves).

Notice how Python automatically passes the class as the first argument to the function when we call MyClass.classmethod(). Calling a method in Python through the dot syntax triggers this behavior. The self parameter on instance methods works the same way.

Please note that naming these parameters self and cls is just a convention. You could just as easily name them the_object and the_class and get the same result. All that matters is that they’re positioned first in the parameter list for the method.
"""

#static method
obj.staticmethod()

"""
This confirms that static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’s (and every instance’s) namespace.
"""



#Now, let’s take a look at what happens when we attempt to call these methods on the class itself - without creating an object instance beforehand:

"""
>>> MyClass.classmethod()
('class method called', <class 'first_example.MyClass'>)
>>> MyClass.staticmethod()
'static method called'
>>> MyClass.method()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: method() missing 1 required positional argument: 'self'

"""
