from empresa_dao import EmpresaDAO
from empresa_duplicada_exception import EmpresaDuplicadaException
from empresa import Empresa


class ControladorSistemaEmpresas():

    def __init__(self):
        self.__empresa_dao = EmpresaDAO()

    def inclui_empresa(self, empresa: Empresa):
        if not self.__empresa_dao.get_cnpj(empresa.cnpj):
            return self.__empresa_dao.add_empresa(empresa)
        else:
            raise EmpresaDuplicadaException()

    def exclui_empresa(self, empresa: Empresa):
        if self.__empresa_dao.get_cnpj(empresa.cnpj):
            self.__empresa_dao.remove(empresa)

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        if self.__empresa_dao.get_cnpj(cnpj):
            return self.__empresa_dao.get_cnpj(cnpj)

    @property
    def empresas(self) -> list:
        lista_empresas = []
        for empresa in self.__empresa_dao.get_all():
            lista_empresas.append(empresa)
        return lista_empresas

    '''
    Calcula o total de impostos de todas as empresas.
    Invoca a operacao total_impostos() de cada uma
    das empresas cadastradas no Dicionario, somando os resultados
    Utiliza a EmpresaDAO para buscar as empresas
    @return somatorio dos impostos de todas as empresas cadastradas
    '''
    def calcula_total_impostos(self) -> float:
        somatorio = 0.0
        for empresa in self.__empresa_dao.get_all():
            somatorio += empresa.total_impostos()
        return somatorio
