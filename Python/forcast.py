class Forcast:

  def __init__(self, mode = "F"):

    if mode == "C" or mode == "F" or mode == "K":

      self.mode = mode

      weekly_forcast = {"Mon":-61,"Tue":-40,"Wed":-69, "Thu":88,"Fri":43,"Sat":44,"Sun":66}

      self.weekly_forcast = weekly_forcast

  def __F2C__(self, n):
      C = (5/9.0) * (n-32)
      return C

  def __F2K__(self, n):
      K = (5.0/9) * (n-32) + 273.15
      return K

  def __C2K__(self, n):
      K = n + 273.15
      return K

  def __K2C__(self, n):
      C = n - 273.15
      return C

  def setMode(self, new_mode):
    if new_mode == "C" or new_mode == "F" or new_mode == "K":
      self.mode = new_mode

    else:
      pass

  def getMonTemp(self):
    r = self.weekly_forcast["Mon"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode =="K":
      return self.__F2K__(r)
    else:
      return r

  def getTueTemp(self):
    r = self.weekly_forcast["Tue"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode == "K":
      return self.__F2K__(r)
    else:
      return r

  def getWedTemp(self):
    r = self.weekly_forcast["Wed"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode == "K":
      return self.__F2K__(r)
    else:
      return r

  def getThuTemp(self):
    r = self.weekly_forcast["Tue"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode == "K":
      return self.__F2K__(r)
    else:
      return r

  def getFriTemp(self):
    r = self.weekly_forcast["Tue"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode == "K":
      return self.__F2K__(r)
    else:
      return r

  def getSatTemp(self):
    r = self.weekly_forcast["Tue"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode == "K":
      return self.__F2K__(r)
    else:
      return r

  def getSunTemp(self):
    r = self.weekly_forcast["Tue"]
    if self.mode == "C":
      return self.__F2C__(r)
    elif self.mode == "K":
      return self.__F2K__(r)
    else:
      return r

def WeekForcast(Fc):
    S = "Mon:" + str(round(Fc.getMonTemp(),2)) + "Tue:" + str(round(Fc.getTueTemp(),2))
    S = S + "Wed:" + str(round(Fc.getWedTemp(),2)) + "Thu:" + str(round(Fc.getThuTemp(),2))
    S = S + "Fri:" + str(round(Fc.getFriTemp(),2)) + "Sat:" + str(round(Fc.getSatTemp(),2))
    S = S + "sun:" + str(round(Fc.getSunTemp(),2))
    if Fc.mode == "F":
        S = S + "\nfahrenheit"
    elif Fc.mode == "C":
        S = S + "\ncelsius"
    else:
        S = S + "\nkelvin"
    return S

F1 = Forcast("K")
print(F1.getMonTemp())
F1.setMode("C")
print(F1.getMonTemp())
F1.setMode("F")
print(F1.getMonTemp())

F1 = Forcast("K")
print(F1.getTueTemp())
F1.setMode("C")
print(F1.getTueTemp())
F1.setMode("F")
print(F1.getTueTemp())

F1 = Forcast("K")
print(F1.getWedTemp())
F1.setMode("C")
print(F1.getWedTemp())

F1 = Forcast("K")
print(F1.getThuTemp())
F1.setMode("C")
print(F1.getThuTemp())

F1 = Forcast("K")
print(F1.getFriTemp())
F1.setMode("C")
print(F1.getFriTemp())

F1 = Forcast("K")
print(F1.getSatTemp())
F1.setMode("C")
print(F1.getSatTemp())

F1 = Forcast("K")
print(F1.getSunTemp())
F1.setMode("C")
print(F1.getSunTemp())
print(WeekForcast(F1))
