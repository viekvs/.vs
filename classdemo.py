class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def personinfo(self):
    print(self.name +" is "+str(self.age)+" year(s) old.")
  def birth(self):
    self.age+=5
  def setAfriend(self,friend):
    self.friend=friend
    friend.friend=self
class student(person):
  def __init__(self,name,age,rno):
    super().__init__(name,age)
    self.roll=rno
  def personinfo(self):
      super().personinfo()
      print("and the roll number is ",self.roll)
  def birthday(self):
     super().birthday()

s1=student("navin",23,76)
s1.personinfo()
print("xxxxxxxxxx")
p1=person("vivek",34)
p1.personinfo()
print("##########")
s1.birthday()
s1.personinfo()