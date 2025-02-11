from utils import load_data, load_template 

def index():
    # Carrega o template de cada anotação:
    note_template = load_template('components/note.html')         
    
    # Monta a lista de anotações formatadas:
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]                                                             
    
    # Une tudo em uma única string:
    notes = '\n'.join(notes_li)                                   

    # Retorna o HTML principal com as anotações:
    return load_template('index.html').format(notes=notes)        

def submit(titulo, detalhes):
    # Importa a função para adicionar anotações:
    from utils import add_note                                    
    
    # Adiciona a nova anotação ao arquivo JSON:
    add_note(titulo, detalhes)                                    
