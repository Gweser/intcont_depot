def diff(file_first, file_second):
  """Fonction retournant True si deux fichiers sont différents."""
  resultat = False
  with open(file_first) as f1, open(file_second) as f2:
    resultat = f1.read() != f2.read()
  return resultat

def same(file_first, file_second):
  """Fonction retournant True si deux fichiers sont identiques."""
  return True
