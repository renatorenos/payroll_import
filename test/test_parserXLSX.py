import settings
from src import parserXLSX

file = 'test/Ferias022024.xlsx'

print(type(file))

print(parserXLSX.parserFile_list(file))