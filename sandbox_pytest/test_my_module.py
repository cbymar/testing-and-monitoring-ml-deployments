import sys
import os
x = os.path.dirname(os.path.abspath(__file__))
sys.path.append(x)

from my_module import square


def test_square_returns_correctly():
	# When
	subject = square(2)

	# then
	assert subject == 4
