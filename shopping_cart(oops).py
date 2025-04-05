class ShoppingCart:
  def __init__(self):
    self.items = {}
    
  def add_item(self,item,cost):
    self.items[item] = cost
    print("Added Item Successfully")
  
  def remove_item(self,item):
    if item not in self.items:
      print("Item Not Found")
    else:
      del self.items[item]
      print("Removed Item Successfully")
    
  def calculate_total(self):
    print(sum(self.items.values()))
