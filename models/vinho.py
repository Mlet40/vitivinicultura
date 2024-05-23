class Vinho:
    def __init__(self, nome, tipo, ano):
        self.nome = nome
        self.tipo = tipo
        self.ano = ano

    def to_dict(self):
        return {
            'nome': self.nome,
            'tipo': self.tipo,
            'ano': self.ano
        }