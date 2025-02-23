from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome: str, categoria: str, ativo: bool = False):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = ativo
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Atividade:")
        resultado = [f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante._ativo}' for restaurante in cls.restaurantes]
        print('\n'.join(resultado))

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        return round(sum(avaliacao._nota for avaliacao in self._avaliacao)/len(self._avaliacao), 1)

    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        if nota < 0 or nota > 5:
            return
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        string_cardapio = [f'{index + 1}. {item._nome.ljust(20)} | R${item._preco:<6.2f} | {item._descricao if hasattr(item, '_descricao') else item._tamanho}' for index, item in enumerate(self._cardapio)]
        print('\n'.join(string_cardapio))

    def __str__(self):
        return f"{self._nome} | {self._categoria} | {self._ativo}"
