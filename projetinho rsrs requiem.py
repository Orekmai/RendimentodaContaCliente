class ContaCliente:
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    def CalculoRendimento(self):
        pass


class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)

    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)


class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)

    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido -= (self.valorinvestido * (self.IOF + 0.01))

cl1 = ContaComum('2-634', 0.0038, 0.2, 1050, 0.05)
print("Conta Comum\n")
print("Valor antes do rendimento:", cl1.valorinvestido)
cl1.CalculoRendimento()
print("Valor depois do rendimento:", cl1.valorinvestido)

cl2 = ContaRemunerada('0-634', 0.0038, 0.2, 1050, 0.05)
print("Conta Remunerada\n")
print("Valor antes do rendimento:", cl2.valorinvestido)
cl2.CalculoRendimento()
print("Valor depois do rendimento:", cl2.valorinvestido)