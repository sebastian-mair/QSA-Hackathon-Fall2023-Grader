import importlib  
hackathon = importlib.import_module("QSA-Hackathon-Fall2023.adder")

def test_add():
  assert hackathon.add(3, 4) == 7
