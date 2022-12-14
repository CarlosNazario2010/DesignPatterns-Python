from abc import ABCMeta, abstractmethod


class Template_de_imposto_condicional(object):

    __metaclass__ = ABCMeta                  

    def calcula(self, orcamento):
        
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass                                   
                                                
    @abstractmethod                               
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ICMS(object):                         
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ISS(object):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
                                

class IPI(Template_de_imposto_condicional):       
  
    def deve_usar_maxima_taxacao(self, orcamento):                                     
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):       
        return orcamento.valor * 0.07               
                                         
    def minima_taxacao(self, orcamento):     
        return orcamento.valor * 0.05


class IOF(Template_de_imposto_condicional):

    def __tem_item_maior_cem_reais(orcamento):   
        for item in orcamento.obter_item():       
            return item.valor > 100                     

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and \
            self.__tem_item_maior_cem_reais(orcamento)                                       

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1                    
    
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06
