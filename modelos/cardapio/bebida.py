from modelos.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def aplicar_desconto(self, desconto):
        self._preco *= 1 - (desconto/100)
        
    def __str__(self):
        string_base = super().__str__()
        return f'{string_base} | {self._tamanho}'