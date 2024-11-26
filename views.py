# import renderizador pelo codigo django
from django.shortcuts import render

# import dados dos models
from .models import Usuario

# Crie suas views aqui tipo um controller usando funções
def home(request):
    return render(request, 'usuarios/home.html')

def usuario(request):
    # Essa função manda o model Usuario salvar 
    # pegando o novo usuario da tela para o proximo registro
    # na tabela usuarios do banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # vamos dar um select na tabels e salva um vetor de objetos para 
    # exibir todos os usuarios em uma nova pagina.
    usuarios = {
       'usuarios': Usuario.objects.all()
   }
   #Retorna o vetor roteando para a pagina usuarios.html
   
    return render(request, 'usuarios/usuarios.html', usuarios)