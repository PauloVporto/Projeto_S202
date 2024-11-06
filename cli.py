class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class AvaliacaoCLI(SimpleCLI):
    def __init__(self, avaliacao_model):
        super().__init__()
        self.avaliacao_model = avaliacao_model
        self.add_command("create_person", self.create_person)
        self.add_command("create_game", self.create_game)
        self.add_command("create_aval", self.create_aval)
        self.add_command("update_aval", self.update_aval)
        self.add_command("read_person", self.read_person)
        self.add_command("read_game", self.read_game)
        self.add_command("read_aval", self.read_aval)
        self.add_command("delete_person", self.delete_person)
        self.add_command("delete_game", self.delete_game)
        self.add_command("delete_aval", self.delete_aval)

    def create_person(self):
        name = input("Entre com o nome da pessoa: ")
        idade = input("Entre com a idade da pessoa: ")
        sexo = input("Entre com o sexo da pessoa: ")
        self.avaliacao_model.create_person(name, idade, sexo)

    def create_game(self):
        name = input("Entre com o nome do jogo: ")
        ano_lanc = input("Entre com o ano de lançamento do jogo: ")
        desenvolvedor = input("Entre com o desenvolvedor do jogo: ")
        genero = input("Entre com o gênero do jogo: ")
        self.avaliacao_model.create_game(name, ano_lanc, desenvolvedor, genero)

    def create_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_game = input("Entre com o nome do jogo: ")
        nota = input("Entre com a nota do jogo: ")
        comentario = input("Entre com o comentário do jogo: ")
        self.avaliacao_model.create_aval(name_pessoa, name_game, nota, comentario)

    def update_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_game = input("Entre com o nome do jogo: ")
        new_nota = input("Entre com a nova nota do jogo: ")
        new_comentario = input("Entre com o novo comentário do jogo: ")
        self.avaliacao_model.update_aval(name_pessoa, name_game, new_nota, new_comentario)

    def read_person(self):
        name = input("Entre com o nome da pessoa: ")
        print(self.avaliacao_model.read_person(name))

    def read_game(self):
        name = input("Entre com o nome do jogo: ")
        print(self.avaliacao_model.read_game(name))

    def read_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_game = input("Entre com o nome do jogo: ")
        print(self.avaliacao_model.read_aval(name_pessoa, name_game))

    def delete_person(self):
        name = input("Entre com o nome da pessoa: ")
        self.avaliacao_model.delete_person(name)

    def delete_game(self):
        name = input("Entre com o nome do jogo: ")
        self.avaliacao_model.delete_game(name)

    def delete_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_game = input("Entre com o nome do jogo: ")
        self.avaliacao_model.delete_aval(name_pessoa, name_game)

    def run(self):
        print("Welcome to the Game CLI!")
        print("Available commands: {}".format(list(self.commands.keys())))
        super().run()
