from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class ISS(Imposto):
    def __init__(self, aliquota, incidencia_imposto):
        super().__init__(aliquota, incidencia_imposto)
        self.__servicos = []

    def inclui_servico(self, nome: str):
        if nome not in self.__servicos:
            self.__servicos.append(nome)
        else:
            return

    def exclui_servico(self, nome: str):
        if nome in self.__servicos:
            self.__servicos.remove(nome)
        else:
            return

    def calcula_aliquota(self):
        reducao = len(self.__servicos) / 10
        return self.aliquota - reducao
