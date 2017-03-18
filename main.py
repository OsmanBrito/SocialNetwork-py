import lib

matrizPerson = [
    ["Santos", "casado", "11998876644", "santos@email.com", "10/10/1995", "SP"],
    ["Gremio", "solteiro", "51978786565", "gremio@email.com", "15/01/1986", "RS"],
    ["Internacional", "namorando", "51901234422", "internacional.2@email.com", "02/05/1998", "RS"],
    ["Barcelona", "casado", "21987765544", "barcelona@email.com", "30/01/1976", "RJ"],
    ["Real Madrid", "solteiro", "11987654455", "real@email.com", "30/02/1977", "SP"],
    ["Portuguesa", "viuvo", "11933445214", "lusa@email.com", "23/09/1997", "SP"],
]

# 1 = Familia 2 = Amigos 3 = Conhecido
matrizDeLigacoes = [
    [0, 1, 2],
    [0, 5, 2],
    [3, 1, 3],
    [0, 3, 1],
    [4, 1, 2],
    [2, 1, 1],
]

lib.dashboard( matrizDeLigacoes, matrizPerson)