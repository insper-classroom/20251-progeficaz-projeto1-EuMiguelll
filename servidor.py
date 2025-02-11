from flask import Flask, render_template_string, request, redirect
import views                                                        

# Cria a aplicação Flask:
app = Flask(__name__)                                              

# Define a pasta de arquivos estáticos:
app.static_folder = 'static'                                   

#Rota da pagina principal:
@app.route('/')
def index():
    # Renderiza a string HTML gerada pela função index():
    return render_template_string(views.index())

# Define a rota quando postar o formulario:
@app.route('/submit', methods=['POST'])
def submit_form():
    # Lê o valor do campo 'titulo' e 'detalhes' do formulário:
    titulo = request.form.get('titulo')    
    detalhes = request.form.get('detalhes')

    # Chama a função que adiciona a nova anotação:
    views.submit(titulo, detalhes) 

    # Redireciona de volta para a rota principal:        
    return redirect('/')               

# Executa a aplicação em modo de debug:
if __name__ == '__main__':
    app.run(debug=True)                    