'''
Getters in Python are methods that are used to access the values of an object's properties.
They are used to return the value of a specific property, and are typically defined using the @property decorator.

Getters do not take any parameters and we cannot set the value through getter method.
For that we need setter method which can be added by decorating method with @property_name.setter

Conclusion: Getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden.
This can be useful for encapsulation and data validation.
'''


class Getter_and_Setter:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    # getter
    @property
    def ten_value(self):
        return 10 * self.value

    # setter
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value / 10


gs = Getter_and_Setter(10)
gs.show()
print(gs.ten_value)
gs.ten_value = 67  # setting value
print(gs.ten_value)
gs.show()
