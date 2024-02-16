

label start:
    show fundo1
    with dissolve

    "Todos os dias no Condomínio Laranjeiras chegam encomendas de vários tipos e tamanhos para os moradores."

    hide fundo1
    show fundo2
    with dissolve 
    show personagem9:
        xalign 0.1 
    with moveinleft

    ent "Boa tarde! Encomenda para Ednaldo Pontes do apartamento 305."
    jose "Boa tarde! Só um minuto, por favor."
    jump minijogo1
    return

label minijogo1:

    hide fundo2
    hide personagem9   #sair o porteiro grande
    with dissolve      #com transição de dissolver

    show fundo8     #entra o fundo de jogos
    with dissolve   #com transição de dissolver também

    show personagem8:   #entra o porteiro pequeno
        xalign 0.0 yalign 0.15
    with dissolve       #com transição de dissolver

    menu:
        "O que José deve fazer?"
        "Verificar identidade do morador":
            "Muito bem! Bons porteiros devem ser sempre prevenidos!"
            "Devem acessar o arquivo ou livro de moradores e apartamentos"
            "Para verificar se Ednaldo Pontes é um morador do Condomínio Laranjeiras."
            jump cena2
            return

        "Receber o pacote primeiro":
        #with hpunch   Como colocar o efeito caso ele aperte a opção errada??
            "Resposta errada! E se Ednaldo não for morador deste condomínio?"
            "Existe o risco dele não ser morador e isso trará problemas futuros."
            "Jogue Novamente!"
            jump minijogo1
            return

label cena2:
    hide fundo8        #sai fundo de jogos
    hide personagem8   #sai o Entregador pequeno
    with dissolve      #ambos com transição de dissolver

    show fundo3         #entra a frente da guarita com caixas na direita
    with easeinbottom   #com efeito de baixo para cima

    show personagem2   #entra imagem do José e do Entregador juntos
    with dissolve      #com transição de dissolver

    "José confirmou qual dos moradores era o destinatário e recebeu os pacotes."
    "Foi descarregada uma grande remessa de várias caixas pequenas com fita vermelha e identificação: FRÁGIL."
    "Em seguida, ele assinou um documento de recebimento e se despediu do entregador."

label minijogo2:

    hide fundo3         #sai a frente da guarita com caixas na direita
    hide personagem2    #sai imagem do José e do Entregador juntos
    
    show fundo4         #entra a frente da guarita com mais caixas na esquerda 

    show personagem3    #entra José com dúvida1 grande
    with dissolve       #com transição de dissolver

    "Será que as caixas estão bem guardadas? Após receber os pacotes, o que José deve fazer?"

    hide personagem3    #sai José com dúvida1 grande

    show personagem7    #entra José com dúvida1 pequeno
    with pixellate      #com transição dos pixels como se remetesse ao pensamento

    menu:
        "Não avisar na hora e esperar o dono passar pela portaria":
            hide personagem7    #sai José com dúvida1 pequeno
            show personagem10   #entra José resposta errada1
            with hpunch         #com transição de tremer a tela horizontalmente

            "Opa! As caixas são frágeis!"
            "Se ficarem muito tempo na portaria podem ser danificadas por algum acidente."
            "Não espere! Tente contato o mais rápido possível,"
            "Interfone no apartamento e caso não tenha ninguém em casa avise assim que vê-lo."
            "Jogue Novamente!"

            hide personagem10   #sai José resposta errada1

            jump minijogo2
            return
        "Avisar ao morador":

            hide personagem7     #sai José com dúvida1 pequeno

            show personagem13    #entra José resposta certa1
            with moveinbottom    #com transição que surge de baixo para cima 

            "Opção correta! O porteiro deve sempre guardar os pacotes na portaria,"
            "Registrar as encomendas no livro de registro,"
            "Interfonar no apartamento do morador e avisar que suas encomendas chegaram."

            hide personagem13         #sai Joosé resposta certa1  
            hide fundo4               #sai a frente da guarita com mais caixas na esquerda 
            call screen jogodacaixa   #direciona para o jogo de clicar na caixa
            return

        "Pedir ajuda para as crianças":

            hide personagem7     #sai José com dúvida1 pequeno
            show personagem11    #entra José resposta errada2
            with hpunch          #com transição de tremer a tela horizontalmente

            "Se você colocar as caixas em qualquer lugar e pedir para as crianças mandarem o recado,"
            "Talvez ele não chegue até o Sr. Ednaldo."

            hide personagem11    #sai José resposta errada2
            show personagem12    #entra José fazendo "não" com o dedo
            with fade

            "E não se esqueça, guarde as caixas em um lugar apropriado!"

            hide personagem12    #sai José fazendo "não" com o dedo

            jump minijogo2
            return

label minijogo4:
    
    show fundo6           #entra o fundo da guarita por dentro
    with dissolve         #com transição de dissolver

    show personagem4:     #entra José pedindo pra clicar no botão
       zoom 1.1
       xalign -0.75 yalign 1.1                
    with dissolve         #com transição de dissolver

    "Clique no botão para interfonar para o Sr. Ednaldo"
    
    menu:
        "Ligar para o apartamento 305":
            jump cena5
            return
    
label cena5:
    
    hide personagem4      #sai José pedindo pra clicar no botão
    show personagem5:     #entra José ligando
        zoom 1.9
        xalign -0.55 yalign 1.1                       
    ednaldo "Alô?"
    jose "Boa tarde, Sr. Ednaldo! Aqui é José o porteiro, acabaram de chegar encomendas suas."
    jose "Acredito que sejam itens importantes, pois todas estão com identificação: frágil."
    ednaldo "Boa tarde, José! Vou agora mesmo."
    jose "Certo! Já registrei suas encomendas no livro de registro."

    hide personagem5      #sai José ligando
    show personagem6:     #entra José duvida2
        zoom 1.9
        xalign -0.45 yalign 1.1                          

    jose "Elas já estão organizadas para retirada, só preciso que assine o livro e..."

label minijogo5:
    
    hide fundo6          #sai fundo da guarita por dentro
    hide personagem6     #sai José duvida2
    with pixellate       #com transição de pixels

    show fundo8          #entra o fundo de jogos

    show personagem3:    #entra josé duvida1
        zoom 1.0 
        xalign 0.0 yalign 1.0
    with dissolve        #com transição de dissolver
    
    "Seguindo a norma do Condomínio Laranjeiras, não podemos entregar as encomendas sem apresentação de um documento oficial com foto."
    "Qual documento José precisa pedir para Ednaldo trazer?"
    call screen jogododocumento
    
label cartao:

    hide personagem3       #sai José duvida1
    show personagem11:     #entra Jose resposta errada2
        zoom 1.2
        xalign 0.5 yalign 1.1
    with hpunch            #com transição de tremer a tela horizontalmente

    "Resposta errada! Peça sempre documentos oficiais com foto. Tente novamente!"

    hide personagem11      #sai Jose resposta errada2
    with dissolve          #com transição de dissolver

    jump minijogo5
    return

label identidade:

    hide personagem3      #sai José duvida1
    show personagem14:    #entra José resposta certa2
        zoom 1.15
        xalign 0.65 yalign 1.1
    with moveinbottom     #com transição que surge de baixo para cima 

    "Resposta correta! Estes documentos possuem foto e são válidos em todo território nacional!"

    hide personagem14     #sai José resposta certa2
    hide fundo8           #sai fundo azul de jogos
    with dissolve         #com transição de dissolver

    jump cena6
    return

label carteira:

    hide personagem3        #sai José duvida1
    show personagem10:      #entra Jose resposta errada1
        zoom 1.1
        xalign 0.5 yalign 1.1
    with hpunch            #com transição de tremer a tela horizontalmente

    "Resposta errada! Peça sempre documentos válidos em todo território nacional. Tente novamente!"

    hide personagem10

    jump minijogo5
    return

label cena6:

    show fundo6               #entra o fundo da guarita por dentro
    show personagem5:         #entra José ligando
        zoom 1.9
        xalign -0.45 yalign 1.1 
    with dissolve             #com transição de dissolver

    jose "Só preciso que assine o livro e traga um documento de identificação com foto, pode ser a identidade ou a CNH."
    ednaldo "Com certeza! Irei procurar minha identidade agora mesmo. Até já já!"

    hide  personagem5         #sai José ligando
    show  personagem15:       #entra José dando tchau "até!"
        zoom 2.35 
        xalign -0.25 yalign 1.1

    jose "Até!"

    hide fundo6         #sai fundo da guarita por dentro
    hide personagem15   #sai José dando tchau
    with dissolve       #com transição de dissolver

    show fundo1         #entra fundo da frente do condomínio completo 
    with dissolve       #com transição de dissolver

    "José foi um exemplo de como um Porteiro Classe A deve agir no exercício da sua função,"
    "Pois, assim evita-se que qualquer tipo de incidente venha a surgir ou acontecer durante o seu turno."

    hide fundo1         #sai fundo da frente do condomínio completo 
    with zoominout

    # This ends the game.

    return

screen jogodacaixa:
    add "fundo5"     #entra o fundo do jogo de clicar na caixa
    modal True       #sumir caixa de texto

    hbox:
        spacing 6
        xalign 0.1 yalign 0.1

        text ("Clique sobre a caixa")

    imagebutton auto "caixafragil_%s":
        focus_mask True #aparecer caixa
        xpos 0.5
        ypos 0.75
        
        hovered SetVariable("screen_tooltip", "Clique aqui!")
        unhovered SetVariable("screen_tooltip", "")
        action Jump ("minijogo4")

screen jogododocumento:
    hbox xsize 1920 ysize 1000:
        imagebutton auto "credito_%s.PNG" action Jump("cartao") xalign 2.8 yalign 0.3
        imagebutton auto "documentos_%s.PNG" action Jump("identidade") xalign 0.3 yalign 0.7
        imagebutton auto "membro_%s.PNG" action Jump("carteira") xalign 0.4 yalign 0.7
 