from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("Praça", "Gourmet")
coca = Bebida('Coca-Zero', 5, 'P')
carne = Prato('Carne Suína', 20.0, 'Selecionada e rica em proteína!')
restaurante_praca.adicionar_item_cardapio(coca)
restaurante_praca.adicionar_item_cardapio(carne)
coca.aplicar_desconto(10)
def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()