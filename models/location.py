class Location():
  def __init__(self, id, name, address):
      self.id = id
      self.name = name
      self.address = address

  def _repr_(self):
      return f"Where is {self.name}"
