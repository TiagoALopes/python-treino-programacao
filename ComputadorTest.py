import unittest
from entity.Computador import Computador

class ComputadorTest(unittest.TestCase):
    def setUp(self):
        self.computador1 = Computador('Asus', '256 Gb', 'AMD Force')
        self.computador2 = Computador('Intel', '128 Mb', 'Pentium')

    def test_deve_validar_computador_ligado_com_sucesso(self):
        self.assertEquals(self.computador1.ligar(),'Estou ligando...')
        self.assertEquals(self.computador2.ligar(), 'Estou ligando...')

#Este passo abaixo permite que sejam executados todos os testes.
if __name__ == '__main__':
    unittest.main()