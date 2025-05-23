def __int__(sefl, nome, raca, idade, cor):
    self.nome = nome
    self.raca = raca
    self.idade = idade
    self.cor = cor
    cachorro.cachorros_cadastrado.append(self)


    @classmethod
    def listar_cachorros(cls):
        if not cls.cachorros_cadastrado:
            print("Nenhum Cadastrado")
            return


            print ("\n --- Cachorros Cadastrados ---")
            for i, cachorro in emurate(cls.cachorros_cadastrado,1):
                print(f"{i}. {cachorro.nome} | {cachorro.raca} | {cachorro.idade} | {cachorro.cor}")
                print("-------------------------------")
