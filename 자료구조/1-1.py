class student:
  def __init__(self, name, id):
    self.name = name
    self.id = id
  def gte_nemae(self):
    return self.name
  def get_id(self):
    return self.id
  
best = student('Lee',101)
print(best.get_name())
print(best.get_id())