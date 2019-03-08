import pickle

def salvar(arquivo, dados):
    pickle.dump(dados, open(arquivo, "wb"))

def listar(arquivo):
    nova_lista = pickle.load(open(arquivo, "rb"))
    return nova_lista
