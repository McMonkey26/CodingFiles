def fibonnaci():
  lastVal, n = (0, 1)
  while True:
    yield n
    lastVal, n = (n, n+lastVal)
class iterTest:
  def __init__(self, start, maxVal):
    self.n = start
    self.max = maxVal
  def __iter__(self):
    return self
  def __next__(self):
    if self.n <= self.max:
      self.n += 2
      return self.n - 2
    else:
      raise StopIteration
test = iterTest(3, 90)