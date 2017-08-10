class MyClass:
  """example class"""
  def __init__(self):
    self.name = 'Brooklyn NY'

  def getName(self):
    return 'hello ' + self.name
myObject = MyClass()
print(myObject.getName())
