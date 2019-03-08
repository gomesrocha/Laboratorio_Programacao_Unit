import persistencia as p
arquivo = "usuario.pickle"
def cadastro_usuario(usuario, senha, tipo):
    lista_usuario = [usuario, senha, tipo]
    p.salvar(arquivo, lista_usuario)
    return "Usuário cadastrado com sucesso"

def search (lista, valor):
    return [(lista.index(x), x.index(valor)) for x in lista if valor in x]


def login_usuario(usuario):
    lista_usuario = p.listar(arquivo)
    search(lista_usuario, usuario)