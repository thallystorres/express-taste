from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        self._descricao = descricao

    def aplicar_desconto(self, desconto):
        self._preco *= 1 - (desconto/100)

    def __str__(self):
        string_base = super().__str__()
        return f'{string_base} | {self._descricao}'