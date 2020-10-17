class Customer():
  def __init__(self, id, name, address, email = "", password = ""):
      self.id = id
      self.name = name
      self.address = address
      self.email = email
      self.password = password

  def _repr_ (self):
    return f"{self.name} lives at this {self.address}"
