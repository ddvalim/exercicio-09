class EmpresaDuplicadaException(Exception):
    def __init__(self):
        super().__init__('Essa empresa já foi cadastrada!')
