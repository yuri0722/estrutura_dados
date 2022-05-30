from no import No

class Lista_duplamente_encadeada:

  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def __vazia(self):
    return self.primeiro == None

  def mostrar(self):
    if (self.primeiro == None):
      print("A lista esta vazia")
      return None
      
    atual = self.primeiro
    while (atual != None):
      atual.get_no()
      atual = atual.proximo

  def inserir_inicio(self, valor):
    novo = No(valor)
    if (self.__vazia()):
      self.ultimo = novo
    else:
      self.primeiro.anterior = novo
    novo.proximo = self.primeiro
    self.primeiro = novo

  def inserir_final(self, valor):
    novo = No(valor)
    if (self.__vazia()):
      self.primeiro = novo
    else:
      self.ultimo.proximo = novo
      novo.anterior = self.ultimo
    self.ultimo = novo

  def excluir_inicio(self):
    if (self.__vazia()):
      print("Lista Vazia")
    else:
      if (self.primeiro.proximo == None):
        self.primeiro = None
      else:
        self.primeiro = self.primeiro.proximo
      self.primeiro.anterior = None

  def excluir_final(self):
    if (self.__vazia()):
      print("Lista Vazia")
    else:
      if (self.primeiro.proximo == None):
        self.primeiro = None
      else:
        self.ultimo.anterior.proximo = None
      self.ultimo = self.ultimo.anterior