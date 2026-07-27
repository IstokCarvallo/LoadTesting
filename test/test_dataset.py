from datasets import DatasetProvider

provider = DatasetProvider()

for i in range(10):
    usuario = provider.next_user()
    consulta = provider.next_consulta()

    print(usuario)
    print(consulta)

    print("----------------")