# A Fazer
* Permitir que ele fique fixado acima dos outros apps.
  * `root.attributes("-topmost", True) #[Ou False]`
  * Usando o atalho ctrl+espaco ou alt+espaco
  * Adcionar no clique do botão direito
* Permitir que ele fique transparente.
  * root.attributes("-alpha", valor)
  * Adcionar no clique do botão direito com transparencias predefinidas
* Criar abas nas configs pra guardar as configs necessarias dessas alterações
* Arrumar o fast menu e o format menu pra comprimir melhor as informações
* Adcionar um atalho pra inserir o ultimo simbolo usado
* Ver logo de adcionar uma forma de eu importar minhas fontes pro programa, pra ele ter o side prefix 2 compativel com todos os pcs entre outras customizações
* IMPORTANTE! Arrumar o file_operations - Semi concluido - falta uma retrocompatibilidade e b.o na hora de abrir a partir do nada
* Testar varios cenarios
* Limpar o menu de opções (o código)
* Fazer uma limpeza e formatada no código
# Ideias pro Futuro
## Posiveis:
* Separar tudo por frame, pra ter bordas finas e com cor entre os widgets pra copiar mais um poquinho o vs code kkkkk
  * Adcionar botões pra isso no menu de options e fazer um conversor de tema antigo pro novo com as bordas
* Poder inserir imagens nos arquivos
* Formatação avançada
  * inicialmente minha ideia pra isso é uma formatação que além da cor e tamanho etc, pode mudar a fonte daquele trecho tambem
  * Criar uma toplevel pra isso com preview e tals, tipo o color chooser
* Tentar adcionar canvas numa idea de Quadro Negro pra poder desenhar ele usando esquema de inserir widgets no texto
* Permitir que a sideBar consiga criar, deletar e renomear arquivos e pastas
* Tentar fazer uma barra de titulo do zero e talvez um sistema de menu inteiro

# Prototitpos e testes
## Prototipo de multiplos insert index
```py
global insertCount
insertCount = 0;
def insertMark(event):
    global insertCount
    print(insertCount)
    text.mark_set("extraInsert"+str(insertCount), 'current')
    insertCount += 1
    print(insertCount)
root.bind("<Alt-m>", lambda event: insertMark(event))
def teste(event):
    for mark_name in text.mark_names():
        if('extraInsert') in mark_name:
            text.insert(mark_name, event.char)
root.bind("<Key>", lambda event: teste(event))
```