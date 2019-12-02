import pickle


class EmpresaDAO:
    def __init__(self, datasource='empresa.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}
        
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as d_file:
            pickle.dump(self.__object_cache, d_file)

    def __load(self):
        with open(self.__datasource, 'rb') as l_file:
            self.__object_cache = pickle.load(l_file)

    def add_empresa(self, empresa):
        self.__object_cache[empresa.cnpj] = empresa
        self.__dump()
    
    def get_cnpj(self, cnpj):
        try:
            return self.__object_cache.get(cnpj)
        except KeyError:
            return None
            
    def remove(self, empresa):
        self.__object_cache.pop(empresa.cnpj)
    
    def get_all(self):
        return list(self.__object_cache.values())
        