class MyClass:
  """example class"""
  def __init__(self, my_name):
    self.name = my_name

  def getName(self):
    return 'hello ' + self.name
M1 = MyClass("foo")
M2 = MyClass("bar")
print(M1.getName())
print(M2.getName())
