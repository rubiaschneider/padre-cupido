class Pessoa:
    
    def __init__(self, id: int, nome: str) -> None:
        self.id = id
        self.nome = nome
        self.prefs = []
        self.par = None
        
    def satisfacao(self, p):
        return len(self.prefs) - self.prefs.index(p)
    
    def solteiro(self):
        return self.par == None

    def __repr__(self) -> str:
        return self.nome


def testar_casamento(homem: Pessoa, mulher: Pessoa) -> int:
    return homem.satisfacao(mulher) + mulher.satisfacao(homem)


def casar(homem: Pessoa, mulher: Pessoa):
    homem.par = mulher
    mulher.par = homem


def criar_casais(homens: list, mulheres: list):
    n = len(homens)
    pontuacao_geral = 0
    for pontuacao_atual in range(n * 2, 1, -1):
        for h in homens:
            for m in mulheres:
                if testar_casamento(h,m) == pontuacao_atual and h.solteiro() and m.solteiro():
                    casar(h,m)
                    pontuacao_geral += pontuacao_atual 
                    #print(f'{h.nome} casou com {m.nome} {pontuacao_atual}')  
    return pontuacao_geral

def ler_entrada():
    homens = []
    mulheres = []
    n = int(input())
    for i in range(1, n + 1):
        linha = input()
        nome = linha[linha.index(' ') + 1:]
        h = Pessoa(i, nome)
        homens.append(h)
    for i in range(1, n + 1):
        linha = input()
        nome = linha[linha.index(' ') + 1:]
        mulheres.append(Pessoa(i, nome))  
    for h in homens:
        linha = input()
        ids = linha.split(' ')
        for id_str in ids:
            id = int(id_str)
            h.prefs.append(mulheres[id - 1])
    for m in mulheres:
        for id in input().split(' '):
            m.prefs.append(homens[int(id) - 1])
    return homens, mulheres
    

def main():
    homens, mulheres = ler_entrada()
    pontuacao = criar_casais(homens, mulheres)
    print(pontuacao)


if __name__ == '__main__':
    main()