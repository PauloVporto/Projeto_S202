class AvaliacaoCRUD:
    def __init__(self, database):
        self.db = database

    def create_person(self, name, idade, sexo):
        query = "CREATE (:Pessoa {name: $name, idade: $idade, sexo: $sexo})"
        parameters = {"name": name, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)

    def create_game(self, name, ano_lanc, desenvolvedor, genero):
        query = "CREATE (:Jogo {name: $name, ano_lanc: $ano_lanc, desenvolvedor: $desenvolvedor, genero: $genero})"
        parameters = {"name": name, "ano_lanc": ano_lanc, "desenvolvedor": desenvolvedor, "genero": genero}
        self.db.execute_query(query, parameters)

    def create_aval(self, name_pessoa, name_jogo, nota, comentario):
        query = "MATCH (p:Pessoa {name: $name_pessoa}), (j:Jogo {name: $name_jogo}) CREATE (p)-[:AVALIOU {nota: $nota, comentario: $comentario}]->(j)"
        parameters = {"name_pessoa": name_pessoa, "name_jogo": name_jogo, "nota": nota, "comentario": comentario}
        self.db.execute_query(query, parameters)

    def update_aval(self, name_pessoa, name_jogo, newNota, newComentario):
        query = "MATCH (p:Pessoa {name: $name_pessoa})-[a:AVALIOU]->(j:Jogo {name: $name_jogo}) SET a.nota = $newNota, a.comentario = $newComentario"
        parameters = {"name_pessoa": name_pessoa, "name_jogo": name_jogo, "newNota": newNota,
                      "newComentario": newComentario}
        self.db.execute_query(query, parameters)

    def read_person(self, name):
        query = "MATCH (p:Pessoa {name: $name}) RETURN p.name AS pessoa_name, p.idade AS pessoa_idade, p.sexo AS pessoa_sexo"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        pessoa_name = str([result["pessoa_name"] for result in results])
        pessoa_idade = str([result["pessoa_idade"] for result in results])
        pessoa_sexo = str([result["pessoa_sexo"] for result in results])
        return ["O nome da pessoa é: " + pessoa_name + ", a idade é: " + pessoa_idade + " e o sexo é: " + pessoa_sexo]

    def read_game(self, name):
        query = "MATCH (j:Jogo {name: $name}) RETURN j.name AS jogo_name, j.ano_lanc AS jogo_ano_lanc, j.desenvolvedor AS jogo_desenvolvedor, j.genero AS jogo_genero"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        jogo_name = str([result["jogo_name"] for result in results])
        jogo_ano_lanc = str([result["jogo_ano_lanc"] for result in results])
        jogo_desenvolvedor = str([result["jogo_desenvolvedor"] for result in results])
        jogo_genero = str([result["jogo_genero"] for result in results])
        return [
            "O nome do jogo é: " + jogo_name + ", o ano de lançamento é: " + jogo_ano_lanc + ", o desenvolvedor é: " + jogo_desenvolvedor + " e o gênero é: " + jogo_genero]

    def read_aval(self, name, jogo):
        query = "MATCH (p:Pessoa {name: $name})-[a:AVALIOU]->(j:Jogo {name: $jogo}) RETURN a.nota AS jogo_nota, a.comentario AS jogo_comentario"
        parameters = {"name": name, "jogo": jogo}
        results = self.db.execute_query(query, parameters)
        jogo_nota = str([result["jogo_nota"] for result in results])
        jogo_comentario = str([result["jogo_comentario"] for result in results])
        return [
            "A pessoa " + name + " deu nota " + jogo_nota + " e comentou: " + jogo_comentario + " sobre o jogo " + jogo]

    def delete_game(self, name):
        query = "MATCH (j:Jogo {name: $name}) DETACH DELETE j"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_person(self, name):
        query = "MATCH (p:Pessoa {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_aval(self, name_pessoa, name_jogo):
        query = "MATCH (p:Pessoa {name: $name_pessoa})-[a:AVALIOU]->(j:Jogo {name: $name_jogo}) DELETE a"
        parameters = {"name_pessoa": name_pessoa, "name_jogo": name_jogo}
        self.db.execute_query(query, parameters)
