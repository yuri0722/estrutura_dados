class No:

  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    self.anterior = None

  def get_no(self):
    print(self.valor)