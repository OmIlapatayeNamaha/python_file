class A:
    def greet(self):
        print("Hello from A!")
class B(A):
    def greet(self):
        print("Hello from B!")
        super().greet()
class C(A):
    def greet(self):
        print("Hello from C!")
        super().greet()
class D(B, C):
    pass

d=D()
d.greet()