from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class Empresa():
    def __init__(self, cnpj: int, nome_de_fantasia: str):
        self.__cnpj = cnpj
        self.__nome_de_fantasia = nome_de_fantasia
        self.__impostos = []
        self.__faturamento_servicos = 0.0
        self.__faturamento_producao = 0.0
        self.__faturamento_vendas = 0.0

    @property
    def impostos(self) -> list:
        return self.__impostos

    def inclui_imposto(self, imposto: Imposto):
        if isinstance(imposto, Imposto) and imposto not in self.__impostos:
            self.__impostos.append(imposto)
        else:
            return

    def remove_imposto(self, imposto: Imposto):
        if isinstance(imposto, Imposto) and imposto in self.__impostos:
            self.__impostos.remove(imposto)
        else:
            return

    @property
    def faturamento_servicos(self):
        return self.__faturamento_servicos

    @property
    def faturamento_producao(self):
        return self.__faturamento_producao

    @property
    def faturamento_vendas(self):
        return self.__faturamento_vendas

    def faturamento_total(self) -> float:
        return (self.__faturamento_producao + self.__faturamento_servicos + 
                self.__faturamento_vendas)
        
    def total_impostos(self) -> float:
        impostos = 0.0
        for imposto in self.__impostos:
            if imposto.incidencia_imposto == IncidenciaImposto.PRODUCAO:
                impostos += (imposto.calcula_aliquota() / 100 * 
                            self.__faturamento_producao)
            elif imposto.incidencia_imposto == IncidenciaImposto.VENDAS:
                impostos += (imposto.calcula_aliquota() / 100 * 
                            self.__faturamento_vendas)
            elif imposto.incidencia_imposto == IncidenciaImposto.SERVICOS:
                impostos += (imposto.calcula_aliquota() / 100 * 
                            self.__faturamento_servicos)
            elif imposto.incidencia_imposto == IncidenciaImposto.TODOS:
                impostos += (imposto.calcula_aliquota() / 100 * 
                            (self.__faturamento_producao + 
                            self.__faturamento_vendas + 
                            self.__faturamento_servicos))
        return impostos
        
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def nome_de_fantasia(self):
        return self.__nome_de_fantasia

    @nome_de_fantasia.setter
    def nome_de_fantasia(self, nome_de_fantasia: str):
        self.__nome_de_fantasia = nome_de_fantasia

    def set_faturamentos(self,
                         fat_servicos: float,
                         fat_producao: float,
                         fat_vendas: float):
        self.__faturamento_servicos = fat_servicos
        self.__faturamento_producao = fat_producao
        self.__faturamento_vendas = fat_vendas
        