><h1>A FAZER</h1>
- versus mode
- msg e changescn
><h1>A2_LP</h1>

Nesse repositório, feito para a segunda avaliação de Linguagem de Programação, encontram-se os códigos feitos para a criação de um jogo a partir da biblioteca ``pygame``.

><h2>Índice</h2>

   * [Pygame Racer](#jogo)
   * [Requisitos](#requisitos)
   * [Iniciar](#uso)
   * [Como jogar](#intrucoes)
   * [Documentação](#docs)
   * [Easter-Eggs](#extras)
   * [Colaboradores](#equipe)

><h2 id=jogo>Pygame Racer</h2>
Esse jogo é um jogo arcade, ou seja, seu objetivo é obter a maior pontuação possível a cada partida e ir atualizando o placar de pontuação (``SCORES``) conforme você vai aprimorando suas habilidades e obtendo pontuações cada vez maiores. 

Ele funciona da seguinte forma: você controla um carro por ruas conhecidas do Rio de Janeiro, cenários desenhados por nós. O objetivo é ficar o maior tempo possível sem bater nos outros carros que estão na pista, que são gerados aleatoriamente e servem como obstáculos para o jogador. Quanto mais tempo, mais pontos vocêe faz. Há, tembém, diamantes pela pista que, ao pegá-los, você ganha um incremento de pontuação. Você começa com 3 vidas, e a cada batida em algum dos carros, perde uma vida. O jogo acaba quando você não tem mais vidas, e vale a pontuação que você adquiriu ateé o momento da última colisão. Há vidas extras pela pista, então, caso você bata em um carro mas pegue uma vida em sequência, você se menterá com 3 vidas.

><h2 id=requisitos>Requisitos</h2>

Use o pacote [pip](https://pip.pypa.io/en/stable/) para instalar as bibliotecas necessárias:

```bash
pip install pygame
pip install os
pip install random
pip install json
```

><h2 id=uso>Iniciar</h2>

Após instalar todas as bibliotecas, para o uso desse repositório e dar início ao jogo, basta cloná-lo e seguir a seguinte linha de comando:

```bash
python main.py
```

><h2 id=instrucoes>Como jogar</h2>

Após seguir a intrução de como iniciar o jogo, para iniciar uma partida, você terá duas opções de botões:

   * [PLAY](#play) 
   * [PLAY VERSUS](#versus)

>><h3 id=play>PLAY</h3>

Ao escolher essa opção de início, você iniciará uma partida solo, onde o objetivo é obter a maior pontuação possível. Antes de iniciar de fato, haverá uma identificação do nome do jogador e também a seleção dos mapas. Essa identificação serve para poder criar a lista de maiores pontuadores, que poderá ser vista no botão do menu inicial escrito ``SCORES``. Para jogar você usará as seguintes teclas:
   * <kbd>A</kbd>, move o carro para a esquerda.
   * <kbd>D</kbd>, move o carro para a direita.

>><h3 id=versus>PLAY VERSUS</h3>

Ao escolher essa opção, a partida para dois jogadores irá iniciar, onde o objetivo será ter a maior pontuação que seu adversário para poder ganhar. Nesse modo não há identificação dos jogadores, o que os diferenciará serão as teclas que usam para jogar. Esse modo também conta com a escolha dos mapas. Nesse modo, as teclas para controle dos carros são distribuídas da seguinte forma:
   >>><h4>Jogador 1</h4>
   * <kbd>A</kbd>, move o carro para a esquerda.
   * <kbd>D</kbd>, move o carro para a direita. 
   >>><h4>Jogador 2</h4>
   * <kbd>←</kbd>, move o carro para a esquerda.
   * <kbd>→</kbd>, move o carro para a direita. 



><h2 id=docs>Documentação</h2>

A documentação desse projeto foi feita dentro das linhas de código do jogo, onde cada função está devidamente comentada e documentada.


><h2 id=extras>Easter-Eggs</h2>

Para ter um pouco de acréscimo ao jogo, resolvemos incrementar alguns detalhes extras ao jogo, os ``Easter-Eggs``. Eles são "macetes" que podem ser usados pelos jogadores em sua jogatina. A ideia é que, caso alguém jogue o jogo sem ter lido o repositório, consiga achá-los e se divertir! São estes os ``Easter-Eggs``:
   * **INVICIBLE**: Ao inserir o nome do jogador, se o jogador colocar ``INVINCIBLE`` como identificação, ele começará a partida com 100 vidas.
   * **I AM SPEED**: Ao inserir o nome do jogador, se o jogador colocar ``I AM SPEED`` como identificação, ele começará a partida a 150km/h.
   * **ROCKETMAN**: Ao inserir o nome do jogador, se o jogador colocar ``ROCKETMAN`` como identificação, ele começará a partida a 10000km/h.

><h2 id=equipe>Colaboradores</h2>
  
  * [João Oliveira](https://github.com/JoaoPereiraOliveira)
  
  * [Rafael dos Santos](https://github.com/rafael1509)

  * [Mikael Pereira](https://github.com/G-mikael)
