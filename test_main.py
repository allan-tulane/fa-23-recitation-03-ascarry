from main import *



## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  assert quadratic_multiply(BinaryNumber(4), BinaryNumber(2)) == 4*2
  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10