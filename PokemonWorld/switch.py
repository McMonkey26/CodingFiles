class switchClass:
  def __init__(self, var):
    self.var = var
  def case(self, testVar):
    if self.var == testVar:
      return True
switch = switchClass(' ')
def switch(var):
  switch.var = var
def case(testVar):
  return testVar == switch.var
def switchprint(*args, **kwargs):
  import os, inspect, builtins
  builtins.print('{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_lineno}')+' '.join(list(map(lambda x:str(x).replace('\n', '\n{:20}'.format(lineFile)), args))))