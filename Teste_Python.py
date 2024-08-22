# Definição de Classe e Instanciação

class Livro:
    def __init__(self, titulo, autor):       # INICIALIZA A FUNÇÃO 
        self._titulo = titulo                # ENCAPSULAMENTO - DEIXAR PRIVADO OS OS ATRIBUTOS UTILIZANDO O (_)
        self._autor = autor
        
    def get_titulo(self):
        return self._titulo

    def set_titulo(self):                    
        return self._titulo                  # METODO GET E SET PARA PERMITIR A LEITIRA E ALTERAÇÃO DESSES VALORES DE FORMA CONTROLADA.
                                           
    def get_autor(self):
        return self._autor

    def set_autor(self):
        return self._autor

    def descrever(self):
        print(f"O livro {self._titulo} foi escrito por {self._autor}.")

livro = Livro("As Crônicas de Gelo e Fogo","George R. R. Martin")
livro.descrever()

# HERANÇA

class Ebook(Livro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)     # O super chama o construtor init da classe livro, que herda os atributos.
        self.formato = formato
    
    def descrever(self):
        print(f"O livro {self._titulo} foi escrito por {self._autor}, no formato {self.formato}")

ebook = Ebook("As Crônicas de Gelo e Fogo","George R. R. Martin",".PDF")
ebook.descrever()

def imprimir_descricao(livro):
    livro.descrever()

imprimir_descricao(livro)
imprimir_descricao(ebook)