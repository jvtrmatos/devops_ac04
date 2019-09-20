from unittest import TestCase
from com.Joao.operacoes import Operacoes


class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
	
	def test_mult(self):
		self.assertEqual(self.operacoes.mult(2,5), 10)