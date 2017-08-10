class Box:
  def __init__(self, box_width, box_height,box_border):
    self.border = box_border
    self.width = box_width
    self.height = box_height
  def getWidth(self):
    return self.width
  def getHeight(self):
    return self.height
  def getBorder():
    return self.border
  def fillbox (self):
    box = ""
    for i in range(self.width):
      box = box +"#"
    for i in range (self.height):
      #box = box + "#"
      print(box)
  def BorderBox(self):
    box = ""
    tbborder = "#"*(self.width+2*self.border)
    lrborder= ("#"*(self.border))+(" "*self.width)+("#"*(self.border))
    for i in range(self.height+2*self.border):
      if i >=self.border and i<=self.height+self.border-1:
        print(lrborder)
      else:
        print(tbborder)



b1 = Box(10,5,1)
b1.fillbox()
b1.BorderBox()
