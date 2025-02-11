import json  
import os    

def load_data(filename_data):
    # Monta o caminho para o arquivo JSON:
    file_path = os.path.join("static", "data", filename_data)
    
    # Abre o arquivo no modo leitura:
    with open(file_path, "r", encoding="utf-8") as file:        
        # Carrega o conteúdo JSON em um dicionário/lista:
        data = json.load(file)                                  
    
    # Retorna a estrutura de dados carregada:
    return data                                                 

def load_template(filename_template):
    # Monta o caminho para o arquivo HTML:
    file_path = os.path.join("static", "templates", filename_template)  
    
    # Abre o arquivo no modo leitura
    with open(file_path, "r", encoding="utf-8") as file:        
        # Retorna o conteúdo do arquivo como string:
        return file.read()                                      

def add_note(titulo, detalhes):
    # Monta o caminho para o notes.json:                                           
    file_path = os.path.join("static", "data", "notes.json")    
    
    # Carrega a lista de anotações existentes:
    data = load_data("notes.json")                              
    
    # Adiciona um novo dicionário com título e detalhes:
    data.append({"titulo": titulo, "detalhes": detalhes})       
    
    # Abre o arquivo no modo escrita:
    with open(file_path, "w", encoding="utf-8") as file:        
        # Salva o conteúdo novamente em formato JSON:
        json.dump(data, file, ensure_ascii=False, indent=2)     
