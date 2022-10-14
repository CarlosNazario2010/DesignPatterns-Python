from datetime import date

from nota_fiscal import NotaFiscal

class CriadorNotaFiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__itens = None
        self.__data_de_emissao = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens 
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_detahes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi_nota(self): 
       
        if self.__razao_social is None:
            raise Exception('RAZAO SOCIAL DEVE SER PREENCHIDA')
        if self.__cnpj is None:
            raise Exception('CNPJ DEVE SER PREENCHIDO')
        if self.__itens is None:
            raise Exception('CAMPO ITENS DEVE SER PREENCHIDO')
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''
       
        return NotaFiscal(razao_social = self.__razao_social, 
                          cnpj = self.__cnpj,
                          itens = self.__itens,
                          data_de_emissao = self.__data_de_emissao,
                          detalhes = self.__detalhes)