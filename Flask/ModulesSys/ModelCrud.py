""" 02-08-25 ModelCrud
    Esse arquivo armazena a lógica que Cria, Lê, Atualiza e Deleta um módulo apartir de sua raiz.


"""
# Utilizar "testUser" para realizar testes!!!
from datetime import datetime
import os
import json
def createModuleRoot(guideName, username, language):
    path = None

    if createNewGuideFolder(username, guideName):
        path = os.path.join('static', 'users', username, 'guides', guideName, 'guide')

    timeNow = str(datetime.now()) # Obtem YYYY-MM-DD hh-mm-ss.ssssss
    rootModule = {
            "guideName": guideName,     # Nome do guia
            "dateCreated": timeNow,     # Data e hora atual
            "lastModified": timeNow,    # Data e hora atual
            "owner": username,          # Quem detem o guia e portanto acesso absoluto
            "language": language,       # Em que língua o Guia esta escrito
            "colaborators": {},         # Quem tem acesso ao guia e em que nível
            "child": {                  # Espaço para submódulos

            }
    } 

    try:
        jsonPath = os.path.join(path, "root.json")
        with open(jsonPath, "w", encoding="utf-8") as f:
            json.dump(rootModule, f, ensure_ascii=False, indent=4)
    except:
        # WIP Criar mensagem de erro que retorne ao fontEnd
        return print("error User not exist")


def createNewGuideFolder(username, guideName):
    #Vai até a pasta guia
    # Verifica se existe guia com mesmo nome
        # Se sim, Retorna que guia com nome já existe e que não é possivel criar dois guias com mesmo nome.
        # Se não, Gera pasta com nome dado ao Guia, pasta para LOGs para imagens e Reports
    folders = ['guide','logs','images','reports']
    path = os.path.join('static', 'users', username, 'guides')
    try:
        os.mkdir(path + "/" + guideName)
    except:
        # WIP implementar resposta ao front ou retornar algo
        print ("Guia de nome igual já existe!!!")
        return False
    path = os.path.join('static', 'users', username, 'guides', guideName)
    for i in folders:
        os.mkdir(path + "/" + i)
    # WIP implementar resposta ao front ou retornar algo
    return True

createModuleRoot("precisoCorrigirCaracteresEspeciais", "testUser", "pt-br")