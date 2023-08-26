import unittest
from entity.Piloto import Piloto

class PilotoTest(unittest.TestCase):
    def setUp(self): #Criando os pilotos e seus respectivos dados.
        self.piloto1 = Piloto('Ayrton','Sena', 4000)
        self.piloto2 = Piloto('Louis','Hamilton', 10000)
        self.piloto3 = Piloto('Alain','Prost', 4000)

    def test_deve_validar_email_com_sucesso(self):
        self.assertEqual(self.piloto1.email(), 'Ayrton.Sena@email.com.br')
        self.assertEqual(self.piloto2.email(), 'Louis.Hamilton@email.com.br')
        self.assertEqual(self.piloto3.email(), 'Alain.Prost@email.com.br')

        self.piloto3.nome = 'Roberto'
        self.piloto3.sobrenome = 'Moreno'

        self.assertEqual(self.piloto3.email(), 'Roberto.Moreno@email.com.br')

    def test_deve_validar_nome_completo_com_sucesso(self):
        self.assertEqual(self.piloto1.nomecompleto(), 'Ayrton Sena')
        self.assertEqual(self.piloto2.nomecompleto(), 'Louis Hamilton')
        self.assertEqual(self.piloto3.nomecompleto(), 'Alain Prost')

    def test_deve_validar_aumento_com_sucesso(self):
        self.assertEqual(4400, self.piloto1.aumento(10))
        self.assertEqual(11800, self.piloto2.aumento(18))
        self.assertEqual(5600, self.piloto3.aumento(40))

#Este passo abaixo permite que sejam executados todos os testes.
if __name__ == '__main__':
    unittest.main()






