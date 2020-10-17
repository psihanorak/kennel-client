class Employee():
  def __init__(self, id, name, address, location_id):
      self.id = id
      self.name = name
      self.address = address
      self.location_id = location_id

  def _repr_(self):
      return f"{self.name} works here at this store"
