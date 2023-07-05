import importlib  
hackathon = importlib.import_module("QSA-Hackathon-Fall2023")

def test_add():
  assert hackathon.adder.add(3, 4) == 7
