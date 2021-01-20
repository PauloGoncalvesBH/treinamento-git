
<div align="center">
<h1>Aprenda conceitos de git, não comandos</h1>
<h4>Um tutorial interativo de git, destinado a ensinar como o git funciona e não apenas quais comandos executar.</h3>
<i>Esse treinamento é quase de graça, basta deixar uma star ⭐ no <a href="https://github.com/PauloGoncalvesBH/treinamento-git">repositório</a>.</i>
</div>
<br>

Então quer usar o **git**, certo?

Mas não quer apenas aprender comandos, quer entender o que usam?

Então isso é para você!

Vamos começar!

> Esse treinamento é uma tradução e adaptação do excelente conteúdo [Learn git concepts, not commands](https://dev.to/unseenwizzard/learn-git-concepts-not-commands-4gjc), de [Nicola Riedmann](https://www.linkedin.com/in/nicola-michel-henry-riedmann/). Thanks Nico 😊

---

> Com base no conceito geral da postagem do blog de Rachel M. Carmena em [How to teach Git](https://rachelcarmena.github.io/2018/12/12/how-to-teach-git.html).
>
> Embora eu ache diversos tutoriais de git na internet focados no que fazer, ao invés de como as coisas funcionam, o recurso mais inestimável para ambos (e a fonte para este tutorial!) é o [Pro Git Book (traduzido para PT-BR)](http://git-scm.com/book/pt-br) e a [página de referência](https://git-scm.com/docs).
>
> Então, se ainda estiver interessado quando terminar aqui, vá conferir! Espero que o conceito um pouco diferente deste tutorial o ajude a entender todos os outros recursos git detalhados lá.

---
- [Visão geral](#visão-geral)
- [Obtendo um _Remote Repository_](#obtendo-um-remote-repository)
- [Adicionando coisas novas](#adicionando-coisas-novas)
- [Fazendo mudanças](#fazendo-mudanças)
- [Ramificação (Branch)](#ramificação-branch)
- [Mesclagem (Merging)](#mesclagem-merging)
    - [Merge Fast-Forward](#merge-fast-forward)
    - [Mesclando branches divergentes](#mesclando-branches-divergentes)
    - [Resolvendo conflitos](#resolvendo-conflitos)
- [Rebasing](#rebasing)
    - [Resolvendo conflitos](#resolvendo-conflitos-1)
- [Atualizando o _Dev Environment_ com as alterações remotas](#atualizando-o-dev-environment-com-as-alterações-remotas)
    - [Buscando as alterações (Fetch)](#buscando-as-alterações-fetch)
    - [Puxando as alterações (Pull)](#puxando-as-alterações-pull)
    - [Escondendo as alterações (Stash)](#escondendo-as-alterações-stash)
    - [Puxando (Pull) com conflitos](#puxando-pull-com-conflitos)
- [Cherry-picking](#cherry-picking)
- [Reescrevendo a história](#reescrevendo-a-história)
    - [Alterando o último commit (Amend)](#alterando-o-último-commit-amend)
    - [Rebase interativo](#rebase-interativo)
    - [História pública, por que você não deve reescrevê-la e como fazer isso com segurança](#história-pública-por-que-você-não-deve-reescrevê-la-e-como-fazer-isso-com-segurança)
- [Lendo a história](#lendo-a-história)
- [Treinando comandos git](#treinando-comandos-git)
---

## Visão geral

Na imagem abaixo existem 4 caixas. Uma delas fica sozinha, enquanto as outras três estão agrupadas no que chamarei de _Development Environment_.

<!-- components.png -->
![componentes do git](https://user-images.githubusercontent.com/29241659/87479229-79442f00-c601-11ea-8ca6-f9a8070a17e5.png)

Vamos começar com o que está sozinho. O _Remote Repository_ é para onde envia as alterações quando deseja compartilhá-las com outras pessoas e de onde obtém as alterações. Se já usou outros sistemas de controle de versão, não há nada de interessante nisso.

O _Development Environment_ é o que possui na sua máquina local.
As três partes são seu _Working Directory_, a _Staging Area_ e o _Local Repository_. Aprenderemos mais sobre quando começarmos a usar o **git**.

Escolha um local em que prefere colocar o seu _Development Environment_.
Basta ir para a sua pasta pessoal ou para onde preferir e assim colocar os seus projetos. Não será necessário criar uma nova pasta para o seu _Dev Environment_.

## Obtendo um _Remote Repository_

Agora queremos pegar um _Remote Repository_ e colocar o que está nele, na sua máquina.

Sugiro que usemos o repositório [github.com/PauloGoncalvesBH/treinamento-git](https://github.com/PauloGoncalvesBH/treinamento-git) no nosso treinamento.

> Para fazer isso use o comando `git clone https://github.com/PauloGoncalvesBH/treinamento-git.git`
> 
> Mas, ao seguir este tutorial, você precisará enviar as alterações feitas no seu _Dev Environment_ de volta ao _Remote Repository_, e o github não permite que alguém faça isso no repositório de outra pessoa, por isso o melhor a fazer é criar um [_fork_](https://guides.github.com/activities/forking). Há um botão para fazer isso no canto superior direito desta página.

Agora que já possui uma cópia do meu _Remote Repository_ na sua conta do github por ter feito o _fork_, é hora de colocar isso na sua máquina.

Para isso usamos `git clone https://github.com/{SEU USUÁRIO}/treinamento-git.git`

Como podem ver no diagrama abaixo, isso copia o _Remote Repository_ em dois lugares, no seu _Working Directory_ e o _Local Repository_.
Agora é possível ver como o git é um "controle de versão _distribuído_". O _Local Repository_ é uma cópia do _Remote_ e age exatamente como ele. A única diferença é que você não o compartilha com ninguém.

O que o `git clone` também faz é, criar uma nova pasta no local onde executamos o comando. Deve haver uma pasta `treinamento-git` agora. Abra-a.

<!-- clone.png -->
![Clonando o repositório remoto](https://user-images.githubusercontent.com/29241659/87479277-92e57680-c601-11ea-9f8f-a9082fb24e90.png)

## Adicionando coisas novas

Alguém já colocou um arquivo chamado `Alice.txt` no _Remote Repository_. É meio solitário lá, então criaremos um novo arquivo e chamaremos de `Bob.txt`.

O que acabamos de fazer foi adicionar um arquivo no seu _Working Directory_.
Existem dois tipos de arquivos no seu _Working Directory_: Arquivos _tracked_, que o git conhece, e _untracked_, arquivos que o git (ainda) não conhece.

<!-- tracking_files.png -->
![Rastreando arquivos](https://user-images.githubusercontent.com/29241659/87481065-f91fc880-c604-11ea-8c30-97a963fb0533.png)

Para ver o que está acontecendo no seu _Working Directory_ execute `git status`, que informará em que branch você está, se o seu _Local Repository_ é diferente do _Remote_ e os arquivos _tracked_ e _untracked_.

Você verá que `Bob.txt` não é rastreado (_untracked_) e o `git status` até lhe diz como mudar isso.
Na figura abaixo, podemos notar o que acontece quando seguimos a dica e executamos `git add Bob.txt`: Você adicionou o arquivo à _Staging Area_, onde coletaremos todas as alterações que desejamos incluir no _Repository_.

<!-- add.png -->
![Incluindo mudanças na staging area](https://user-images.githubusercontent.com/29241659/87479352-b9a3ad00-c601-11ea-975f-2c5eb0cefffe.png)

Quando adicionar todas as suas alterações (que agora é apenas adicionar `Bob.txt`), estaremos prontos para fazermos o _commit_ do que acabamos de criar no _Local Repository_.

As alterações que fizemos são uma parte significativa do trabalho, portanto, quando executar o `git commit`, um editor de texto será aberto e permitirá que escreva uma mensagem dizendo tudo o que acabou de fazer. Quando salvar e fechar o arquivo de mensagens, o seu _commit_ será adicionado ao _Local Repository_.

<!-- commit.png -->
![Commitando no repositório local](https://user-images.githubusercontent.com/29241659/87479385-c922f600-c601-11ea-8287-22eb200a6a32.png)

Podemos também, adicionar a sua _mensagem de commit_ na linha de comando se chamarmos o `git commit` assim: `git commit -m "Adicionar Bob"`. Mas como desejamos escrever [boas mensagens de commit](https://chris.beams.io/posts/git-commit/), devemos usar um tempo estudando e testarmos o editor.

Agora as alterações estão no seu repositório local, o que é um bom "local" para elas, desde que ninguém mais precise delas ou que ainda não estejam prontas para compartilhá-las.

Para compartilhar os seus commits com o _Remote Repository_ precisamos "empurrá-los" via (`push`).

<!-- push.png -->
![Enviando para o repositório remoto](https://user-images.githubusercontent.com/29241659/87479430-da6c0280-c601-11ea-837a-105a696abb52.png)

Depois de executar o comando `git push` as alterações serão enviadas para o _Remote Repository_. No diagrama abaixo, veremos o estado após o seu `push`.

<!-- after_push.png -->
![Estado de todos os componentes após enviar as alterações](https://user-images.githubusercontent.com/29241659/87479605-2c148d00-c602-11ea-8103-0e72183059ab.png)

## Fazendo mudanças
Até agora apenas adicionamos um novo arquivo. Obviamente a parte mais interessante do controle de versão é a alteração de arquivos.

Dê uma olhada no arquivo `Alice.txt`.

Na realidade, ele contém algum texto, mas `Bob.txt` não, então vamos mudar isso e colocar `Oi!! Eu sou o Bob. Eu sou novo aqui.`.

Se você executar o `git status` agora, verá que o `Bob.txt` está modificado (`modified`).
Nesse estado as alterações estão apenas no seu _Working Directory_.

Se desejarmos ver o que mudou em seu _Working Directory_, podemos executar o comando `git diff` para vermos a seguinte saída:

```Diff
diff --git a/Bob.txt b/Bob.txt
index e69de29..3ed0e1b 100644
--- a/Bob.txt
+++ b/Bob.txt
@@ -0,0 +1 @@
+Oi!! Eu sou o Bob. Eu sou novo aqui.
```

Vá em frente e execute `git add Bob.txt` como fizemos anteriormente. Como sabemos, isso move as suas alterações para a _Staging Area_.

Queremos ver as mudanças que acabamos de realizar, então vamos executar `git diff` novamente! É notável que desta vez a saída está em branco.

Isso acontece porque o `git diff` opera apenas nas alterações no seu _Working Directory_.

Para mostrar quais mudanças já estão na _Staging Area_, podemos executar `git diff --staged` e veremos a mesma saída diff de antes.

Acabei de notar que colocamos dois pontos de exclamação após o 'Oi'. Eu não gosto disso, então vamos mudar o `Bob.txt` novamente, para que seja apenas 'Oi!'

Se agora rodarmos `git status`, veremos que existem duas mudanças: A que já enviamos para a _Staging Area_, onde adicionamos texto, e a que acabamos de fazer, que ainda está apenas no diretório de trabalho.

Podemos dar uma olhada no `git diff` entre o _Working Directory_ e o que já enviamos para a _Staging Area_, para mostrar o que mudou desde que nos sentimos prontos para realizar um commit das mudanças.

```Diff
diff --git a/Bob.txt b/Bob.txt
index 8eb57c4..3ed0e1b 100644
--- a/Bob.txt
+++ b/Bob.txt
@@ -1 +1 @@
-Oi!! Eu sou o Bob. Eu sou novo aqui.
+Oi! Eu sou o Bob. Eu sou novo aqui.
```

Como a mudança é o que queríamos, vamos executar `git add Bob.txt` para enviar o estado atual do arquivo para _stage_.

Agora estamos prontos para realizar o `commit` com o que acabamos de fazer. Criamos o commit com `git commit -m "Alterar texto de Bob"` porque senti que, para uma mudança tão pequena, escrever uma linha seria suficiente.

Como sabemos, as alterações estão agora no _Local Repository_.
Ainda podemos querer saber que mudança acabamos de commitar e o que havia antes.

Podemos fazer isso comparando commits.
Todo commit no git tem um hash exclusivo pelo qual é referenciado.

Se dermos uma olhada no `git log`, não apenas veremos uma lista de todos os commits com _hash_, como _Autor_ e _Data_, também notamos o estado do nosso _Local Repository_ e as informações locais mais recentes sobre _branches remotas_.

No momento, o `git log` se parece com isso:

```ShellSession
commit 87a4ad48d55e5280aa608cd79e8bce5e13f318dc (HEAD -> master)
Author: {VOCÊ} <{SEU EMAIL}>
Date:   Sun Jan 27 14:02:48 2019 -0300

    Alterar texto de Bob

commit 8af2ff2a8f7c51e2e52402ecb7332aec39ed540e (origin/master, origin/HEAD)
Author: {VOCÊ} <{SEU EMAIL}>
Date:   Sun Jan 27 13:35:41 2019 -0300

    Adicionar Bob

commit 71a6a9b299b21e68f9b0c61247379432a0b6007c \1
Author: Paulo Gonçalves <paulorochag@hotmail.com>
Date:   Fri Jan 25 20:06:57 2019 -0300

    Adicionar Alice

commit ddb869a0c154f6798f0caae567074aecdfa58c46
Author: Paulo Gonçalves <paulorochag@hotmail.com>
Date:   Fri Jan 25 19:25:23 2019 -0300

    Adicionar texto do tutorial

    Todas as alterações no tutorial são compactadas neste commit para manter o log livre de desorganização que o distrai.
```

Aqui vemos algumas coisas interessantes:
* Os dois primeiros commits são feitos por mim.
* O seu commit inicial para adicionar Bob é o _HEAD_ atual da branch _master_ no _Remote Repository_. Veremos isso novamente quando falarmos sobre ramificações (branches) e obter alterações remotas.
* O último commit no _Local Repository_ é o que acabamos de fazer e agora sabemos o seu hash.

> Observe que os hashes dos commits serão diferentes para você. Se quiser saber exatamente como o git chega a esses IDs de revisão, dê uma olhada [neste artigo sobre a anatomia de um commit](https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html).

Para comparar esse commit e o anterior, podemos utilizar `git diff <commit>^!` (Onde `^!` diz ao git para comparar o commit com o que veio antes dele). Portanto, neste caso, executo: `git diff 87a4ad48d55e5280aa608cd79e8bce5e13f318dc^!`.

Também podemos fazer o `git diff 8af2ff2a8f7c51e2e52402ecb7332aec39ed540e 87a4ad48d55e5280aa608cd79e8bce5e13f318dc` para o mesmo resultado e, em geral, comparar quaisquer dois commits. Note que o formato aqui é `git diff <de commit> <para commit>`, logo o nosso novo commit fica em segundo.

No diagrama abaixo veremos novamente os diferentes estágios de uma alteração e os comandos diff correspondentes.

<!-- diffs.png -->
![Estados de uma mudança e comandos diff relacionados](https://user-images.githubusercontent.com/29241659/87479633-36cf2200-c602-11ea-84f4-46cf255e8f7b.png)

Agora que temos certeza de que fizemos a alteração que queríamos, vá em frente e execute `git push`.

## Ramificação (Branch)

Outra coisa que torna o git excelente é o fator de que trabalhar com ramificações é realmente uma parte fácil e essencial de como trabalhar com o git.

De fato, trabalhamos em uma branch desde que começamos.

Quando clonamos o _Remote Repository_, o seu _Dev Environment_ inicia automaticamente na ramificação principal do repositório, ou seja, _master_.

> Há um movimento atual para a branch principal deixar de ser chamada como _master_ e passar a ser _trunk_ ou _main_. Linux, Github e outras companhias adotaram a nova nomenclatura. É uma ótima proposta e totalmente alinhada ao movimento `#BlackLivesMatter`. Podemos entender mais lendo o artigo [The bigger picture behind the GitHub master branch name change](https://dev.to/sylviapap/the-bigger-picture-behind-the-github-master-branch-name-change-35h8).

A maioria dos fluxos de trabalho com o **git** incluem fazermos as suas alterações em uma _branch_ antes de mesclá-las (`merge`) novamente na _master_.
Normalmente trabalhará por conta própria até que esteja pronto e confiante das suas alterações, que poderão ser mescladas (mergeadas) na _master_.

> Muitos gerenciadores de repositório git, como o _GitLab_ e o _GitHub_, permitem que as branches sejam _protegidas_, o que significa que nem todos podem simplesmente empurrar (`push`) as mudanças para lá. O _master_ geralmente é protegido por padrão.

Não se preocupe, retornaremos a todas essas coisas com mais detalhes quando precisarmos delas.

No momento queremos criar uma branch para fazermos algumas alterações. Talvez queira apenas tentar algo por conta própria e não mexer com o estado de trabalho na sua branch _master_, ou não pode empurrar (`push`) para a _master_.

As branches ficam no _Local_ e no _Remote Repository_. Quando criamos uma nova branch, o conteúdo dessa branch será uma cópia de qualquer ramificação em que trabalhe no momento.

Vamos fazer algumas alterações no `Alice.txt`! Que tal colocarmos algum texto na segunda linha?

Queremos compartilhar essa mudança, mas não colocá-la na _master_ imediatamente, então vamos criar uma ramificação para ela usando `git branch <branch name>`.

Para criarmos uma nova branch chamada `change_alice`, podemos executar o comando: `git branch change_alice`.

Isso adiciona a nova branch ao _Local Repository_.

Enquanto o seu _Working Directory_ e _Staging Area_ realmente não se importam com branches, sempre criamos o `commit` com a branch em que está atualmente.

Pensamos em _branches_ no git como ponteiros, apontando para uma série de confirmações. Quando fazemos um `commit`, adicionamos o que está a apontar no momento.

Apenas adicionar uma branch, isso não a leva diretamente para lá, apenas cria um ponteiro.
De fato, o estado em que o seu _Local Repository_ está atualmente, pode ser visto como outro ponteiro, chamado _HEAD_, que aponta para qual branch e commit estamos atualmente.

Se isso parecer complicado, os diagramas abaixo ajudarão a esclarecer um pouco as coisas:

<!-- add_branch.png -->
![Estado após adicionar branch](https://user-images.githubusercontent.com/29241659/87479558-1bfcad80-c602-11ea-9ea6-a7611215540e.png)

Para mudar para a nossa nova branch, teremos que usar o comando `git checkout change_alice`. O que isso faz é simplesmente mover o _HEAD_ para a branch que você especificar.

> Como normalmente desejamos mudar para uma branch logo após criá-la, existe a conveniente opção `-b` disponível para o comando `checkout`, que permite realizar `checkout` diretamente em uma branch nova, para que não seja necessária criá-la de antemão.
>
> Então, para criar e mudar para a nossa branch `change_alice`, também poderíamos ter executado `git checkout -b change_alice`. Mais fácil, não é?

<!-- checkout_branch.png -->
![Estado após trocar de branch](https://user-images.githubusercontent.com/29241659/87479588-24ed7f00-c602-11ea-8a4b-c733d1da4826.png)

Notaremos que o seu _Working Directory_ não mudou e o fato de termos modificado `Alice.txt` ainda não está relacionado à branch em que estamos inseridos. Agora podemos adicionar (`add`) e fazer `commit` da alteração em `Alice.txt`, como fizemos no _master_ antes, que irá mover o arquivo para a _Staging Area_ (nesse ponto ainda não está relacionado à branch) e, finalmente, _'committar'_ a sua alteração na branch `change_alice`.

Há apenas uma coisa em que não podemos fazer ainda. Tente enviar (`git push`) as suas alterações para o _Remote Repository_.

Veremos que o seguinte erro e - como o git está sempre pronto para ajudar - uma sugestão de como resolver o problema:

```ShellSession
fatal: The current branch change_alice has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin change_alice 
```

Mas não queremos fazer isso às cegas. Estamos aqui para entender o que realmente acontece. Então, o que são _upstream branches_ e _remotes_?

Lembra quando clonamos o _Remote Repository_ há um tempo? Nesse ponto, ele não continha apenas este tutorial e `Alice.txt`, mas na verdade, duas ramificações.

Quando copiamos as coisas no _Remote Repository_ para o seu _Dev Environment_, algumas etapas (extras) ocorreram "embaixo do capô".

O Git configurou o _remote_ do seu _Local Repository_ para ser o _Remote Repository_ que clonamos e deu a ele o nome padrão `origin`.

> O seu _Local Repository_ pode rastrear vários _remotes_ e eles podem ter nomes diferentes, mas seguiremos apenas com a `origin` nesse tutorial.

Em seguida, ele copiou as duas branches remotas no seu _Local Repository_ e, finalmente, alterou para a _master_ para você (`git checkout`).

Ao fazer isso, outra etapa implícita acontece. Quando fazemos o `checkout` de um nome de uma branch que tenha uma correspondência exata nas branches remotas, obteremos uma nova branch _local_ que está vinculada à branch _remote_. A branch _remote_ é a branch _upstream_ do seu _local_.

Nos diagramas anteriores, podemos notar que apenas as branches locais que possuem. Podemos ver essa lista de branches locais executando o comando `git branch`.

Se quisermos ver também as branches remotas em que o seu _Local Repository_ conhece, podemos executar o comando `git branch -a` para listar todas elas.

<!-- branches.png -->
![Branches remotas e local`](https://user-images.githubusercontent.com/29241659/87479573-2159f800-c602-11ea-8b88-d77409c18278.png)

Agora podemos executar o comando sugerido `git push --set-upstream origin change_alice`, e "empurrar" (`push`) as alterações nas nossas branch para um novo _remote_. Isso criará a branch `change_alice` no _Remote Repository_ e definirá o nosso _local_ `change_alice` para rastrear essa nova branch.

> Existe outra opção se realmente quisermos que o nosso ramo rastreie algo que já exista no _Remote Repository_. Talvez um colega já tenha promovido algumas mudanças, enquanto trabalhamos em alguma questão relacionada a nossa branch local, e gostaríamos de integrar as duas. Então poderíamos simplesmente definir o _upstream_ para a nossa branch `change_alice` como um novo _remote_ usando `git branch --set-upstream-to=origin/change_alice` e daí para rastrear a branch _remote_.

Depois disso, dê uma olhada no seu _Remote Repository_ no github, a sua branch estará lá, pronto para outras pessoas verem e trabalharem.

Vamos ver como podemos obter as alterações de outras pessoas no seu _Dev Environment_ em breve, mas primeiro trabalharemos um pouco mais com as branches, para introduzir todos os conceitos que também entram em jogo quando obtemos novidades do _Remote Repository_.

## Mesclagem (Merging)

Como você e todos, em geral, trabalharão em branches, precisamos conversar sobre como obter alterações de uma branch para outra, _mergeando_ elas.

<!-- NO CONFLICT -->
Acabamos de alterar o arquivo `Alice.txt` na branch `change_alice`, e eu diria que estamos felizes com as alterações que fizemos.

Se executarmos `git checkout master`, o `commit` que fizemos na outra branch não estará lá. Para colocar as alterações na master, precisamos mesclar (`merge`) a branch `change_alice` na master.

Note que sempre mesclaremos uma branch específica com a que estaremos atualmente.

### Merge Fast-Forward

Como já fizemos o checkout na _master_, agora podemos executar `git merge change_alice`.

Como não existem outras alterações conflitando em `Alice.txt` e não mudamos nada na _master_, isso ocorrerá sem problemas na chamada 'fusão' _fast forward_ (rápida).

Nos diagramas abaixo, podemos notar que isso significa apenas que o ponteiro _master_ podemos simplesmente ser avançado para onde o _change_alice_ está.

O primeiro diagrama mostra o estado antes de nossas mesclagens (`merge`). A _master_ ainda está no commit que era originalmente e, na outra branch, fizemos mais um commit.

<!-- before_ff_merge.png -->
![Antes do merge fast forward](https://user-images.githubusercontent.com/29241659/87479561-1dc67100-c602-11ea-9faf-c4b7f17525c2.png)

O segundo diagrama mostra o que mudou com o nosso `merge`.

<!-- ff_merge.png -->
![Após o merge fast forward](https://user-images.githubusercontent.com/29241659/87479646-3a62a900-c602-11ea-88dc-10451f30af2c.png)

### Mesclando branches divergentes

Vamos tentar algo mais complexo.

Adicione algum texto numa nova linha em `Bob.txt` na _master_ e faça um commit.

Então execute `git checkout change_alice`, altere `Alice.txt` e commite.

No diagrama abaixo, veremos como os nossos históricos de commits agora se parecem. _Master_ e `change_alice` se originaram do mesmo commit, mas desde então eles _divergiram_, cada um com o seu próprio commit adicional.

<!-- branches_diverge.png -->
![Commits divergentes](https://user-images.githubusercontent.com/29241659/87479584-23bc5200-c602-11ea-8723-18bb43f084a4.png)

Se você voltar para a master (`git checkout master`) e executar `git merge change_alice`, uma mesclagem de avanço rápido (_fast forward_) não será possível. Em vez disso, seu editor de texto favorito será aberto e permitirá que você altere a mensagem do commit de merge que o git está prestes a criar para reunir as duas branches. Você pode apenas seguir com a mensagem padrão. O diagrama abaixo mostra o estado de nossa história do git após a mesclagem (`merge`).

<!-- merge.png -->
![Mesclando branches](https://user-images.githubusercontent.com/29241659/87479666-40f12080-c602-11ea-9615-a18cacf96524.png)

O novo commit envia as alterações que fizemos na branch `change_alice` para a _master_.

Como você deve se lembrar, as revisões no git não são apenas uma captura instantânea de seus arquivos, mas também contêm informações de onde elas vieram. Cada `commit` tem um ou mais commits pais. Nosso novo commit de `merge` possui como seus pais o último commit da _master_ e o commit que fizemos na branch `change_alice`.

### Resolvendo conflitos

Até agora nossas mudanças não interferiram entre si.

Vamos criar um conflito e depois solucioná-lo.

Crie e faça o checkout de uma nova branch. Você sabe como, mas talvez tente usar o `git checkout -b` para facilitar sua vida.
Eu chamei a minha de `branch_do_bobby`.

Nessa branch faremos uma alteração no `Bob.txt`.
A primeira linha ainda deve ser `Oi! Eu sou o Bob. Eu sou novo aqui.` Mude isso para `Oi! Eu sou o Bobby. Eu sou novo aqui.`

Faça o `commit` da sua alteração e volte (`checkout`) para a branch _master_. Aqui vamos mudar a mesma linha para `Oi!! Eu sou o Bob. Estou aqui há um tempo.` e realizar um `commit` da alteração.

Agora é hora de fazer o `merge` da branch `branch_do_bobby` com a _master_.
Ao tentar isso, você verá a seguinte mensagem:

```ShellSession
Auto-merging Bob.txt
CONFLICT (content): Merge conflict in Bob.txt
Automatic merge failed; fix conflicts and then commit the result.
```
A mesma linha mudou nas duas branches, e o git não pode lidar com isso sozinho.

Se você executar `git status`, receberá todas as instruções úteis de como continuar.

Primeiro, temos que resolver o conflito manualmente.

> Para um conflito fácil como este seu editor de texto favorito se sairá bem. Para mesclar arquivos grandes com muitas alterações, uma ferramenta mais poderosa tornará sua vida muito mais fácil, e eu suponho que sua IDE favorita venha com ferramentas de controle de versão e uma bela visualização para mesclagem.

Se você abrir `Bob.txt`, verá algo semelhante a isso (eu trunquei o que quer que tenhamos colocado na segunda linha antes):

```Diff
<<<<<<< HEAD
Oi!! Eu sou o Bob. Estou aqui há um tempo.
=======
Oi! Eu sou o Bobby. Eu sou novo aqui.
>>>>>>> branch_do_bobby
[... tanto faz o que você colocou na linha 2]
```

No topo, você vê o que mudou em `Bob.txt` no HEAD atual. Abaixo, o que mudou na branch que estamos mesclando.

Para resolver o conflito manualmente, você só precisa ter um conteúdo razoável e sem as linhas especiais que o git introduziu no arquivo.

Então vá em frente e mude o arquivo para algo assim:

```
Oi! Eu sou o Bobby. Estou aqui há um tempo.
[...]
```

A partir daqui, o que estamos fazendo é exatamente o que faríamos para qualquer alteração.
Nós enviamos para _stage_ quando executamos `add Bob.txt`, e então fazemos o `commit`.

Já conhecemos o commit das alterações que fizemos para resolver o conflito. É o _merge commit_ que está sempre presente ao mesclar.

Se alguma vez você perceber no meio da resolução de conflitos que realmente não deseja seguir com o `merge`, você pode simplesmente cancelar (`abort`) executando o comando `git merge --abort`.

## Rebasing

Git tem outra maneira limpa de integrar mudanças entre duas branches, que é chamada de `rebase`.

Ainda lembramos que uma branch é sempre baseada em outra. Quando você a cria, você ramifica de algum lugar.

No nosso exemplo de mesclagem simples, ramificamos a _master_ em um commit específico e, em seguida, fizemos commit de algumas mudanças no _master_ e na branch `change_alice`.

Quando uma ramificação está divergindo daquela em que se baseia e você deseja integrar as alterações mais recentes em sua ramificação atual, o `rebase` oferece uma maneira mais limpa de fazer isso do que uma `mesclagem` faria.

Como vimos, um `merge` introduz um _merge commit_ no qual os dois históricos são integrados novamente.

Visto de forma simples, o rebasing muda apenas o ponto da história (o commit) no qual sua ramificação se baseia.

Para tentar isso, vamos primeiro fazer o checkout da branch _master_ novamente e depois criar uma nova branch baseada nela.
Chamei a minha branch de `add_patrick`, adicionei um novo arquivo chamado `Patrick.txt` e fiz um commit com a mensagem 'Adicionar Patrick'.

Após o commit, volte para a _master_, faça uma alteração e faça o commit. Eu adicionei mais algum texto em `Alice.txt`.

Como em nosso exemplo de mesclagem, a história dessas duas branches divergem em um ancestral comum, como você pode ver no diagrama abaixo.

<!-- before_rebase.png -->
![Histórico antes do rebase](https://user-images.githubusercontent.com/29241659/87479563-1ef79e00-c602-11ea-9e08-fc1d323d51dc.png)

Agora vamos executar `checkout add_patrick` novamente, pegar a mudança que foi feita na _master_ e enviar para a branch em que estamos trabalhando!

Quando executamos `git rebase master`, baseamos nossa ramificação `add_patrick` no estado atual da branch _master_.

A saída desse comando nos dá uma boa dica do que está acontecendo:

```ShellSession
First, rewinding head to replay your work on top of it...
Applying: Adicionar Patrick
```

Como lembramos, _HEAD_ é o ponteiro para o commit atual em que estamos em nosso _Dev Environment_.

Está apontando para o mesmo lugar que `add_patrick` antes do rebase começar. Para o rebase, ele volta primeiro ao ancestral comum, antes de passar para o head atual da branch que queremos basear.

Portanto, o _HEAD_ passa do commit _0cfc1d2_ para o commit  _7639f4b_ que está no head da _master_.
Então rebase aplica cada commit que fizemos na nossa branch `add_patrick`.

Para ser mais exato o que o _git_ faz depois de retornar o _HEAD_ de volta ao ancestral comum dos branches, é armazenar partes de cada commit que você fez na branch (o `diff` das mudanças, o texto do commit, autor, etc. .).

Depois disso, ele faz um `checkout` do último commit da branch na qual você está reestruturando e, em seguida, aplica cada uma das alterações armazenadas como __um novo commit__ no topo dela.

Portanto, em nossa visão simplificada original, assumiríamos que após o `rebase` o commit _0cfc1d2_ não aponta mais para o ancestral comum em sua história, mas aponta para o head da _master_.
De fato, o commit _0cfc1d2_ não existe mais, e a branch `add_patrick` começa com um novo commit _0ccaba8_, que tem o commit mais recente de _master_ como seu ancestral.
Nós fizemos parecer que a branch `add_patrick` foi baseada na _master_ atual, e não em uma versão mais antiga, mas ao fazê-lo reescrevemos o histórico da branch.
No final deste tutorial, aprenderemos um pouco mais sobre como reescrever o histórico e quando é apropriado e inapropriado fazê-lo.

<!-- rebase.png -->
![Histórico após rebase](https://user-images.githubusercontent.com/29241659/87479673-451d3e00-c602-11ea-9fc8-7a31b4395703.png)

`Rebase` é uma ferramenta incrivelmente poderosa quando você está trabalhando em sua própria branch de desenvolvimento, que é baseada em uma branch compartilhada, por exemplo, a _master_.

Usando o rebase, você pode garantir que integra frequentemente as alterações que outras pessoas fazem e enviam para _master_, mantendo um histórico linear limpo que permite fazer uma mesclagem de avanço rápido (`fast-forward merge`) quando chegar a hora de colocar seu trabalho na branch compartilhada.

Manter um histórico linear também torna a leitura ou a visualização (tente `git log --graph` ou dê uma olhada na visualização de branch do _GitHub_ ou _GitLab_) do log de commits muito mais agradável do que ter um histórico repleto de _merge commits_, geralmente usando o texto padrão.

### Resolvendo conflitos

Assim como em um `merge`, você pode ter conflitos se você tiver dois commits alterando as mesmas partes de um arquivo.

No entanto, quando você encontra um conflito durante um `rebase` você não o corrige em um _merge commit_ extra, mas pode simplesmente resolvê-lo no commit que está sendo aplicado no momento.
Novamente, baseando suas alterações diretamente no estado atual da branch original.

Resolver conflitos de `rebase` é muito parecido com o que você faria para um `merge`, portanto, consulte a seção se você não tiver mais certeza de como fazê-lo.

A única distinção é que, como você não está introduzindo um _merge commit_, não há necessidade de fazer um `commit` da sua resolução. Simplesmente execute `add` das alterações, enviando para _Staging Environment_, e depois execute `git rebase --continue`. O conflito será resolvido no commit que estava sendo aplicado.

Assim como no merge, você sempre pode parar e cancelar tudo o que fez até o momento executando `git rebase --abort`.

## Atualizando o _Dev Environment_ com as alterações remotas

Até agora, aprendemos apenas como fazer e compartilhar alterações.

Isso se encaixa no que você fará se estiver trabalhando por conta própria, mas geralmente haverá muitas pessoas que fazem o mesmo e queremos que as alterações sejam alteradas do _Remote Repository_ para o nosso _Dev Environment_ de alguma forma.

Como já faz algum tempo, vamos dar uma outra olhada nos componentes do git:

<!-- components.png -->
![componentes do git](https://user-images.githubusercontent.com/29241659/87479630-359df500-c602-11ea-92f0-301124069b82.png)

Assim como o seu _Dev Environment_, todos os outros que trabalham no mesmo código-fonte possui o seu próprio.

<!-- many_dev_environments.png -->
![muitos dev environments](https://user-images.githubusercontent.com/29241659/87479662-40588a00-c602-11ea-8531-c2e03659d372.png)

Todos esses _Dev Environments_ possuem suas próprias alterações em _Working directory_ e _Staging Area_, que em algum momento geram um novo `commit` no _Local Repository_ e são finalmente empurradas (`push`) para o _Remote Repository_.

No nosso exemplo, usaremos as ferramentas on-line oferecidas pelo _GitHub_ para simular alguém fazendo alterações no _remote_ enquanto trabalhamos.

Vá para o seu `fork`deste repositório no [github.com](https://www.github.com) e abra o arquivo `Alice.txt`.

Encontre o botão de editar o arquivo, faça uma alteração e crie o commit através do site.

<!-- github.png -->
![editar o github](https://user-images.githubusercontent.com/29241659/87483591-739f1700-c60a-11ea-8d27-10c372f2cbb2.png)

Neste repositório adicionei uma alteração remota ao `Alice.txt` em uma branch chamada `fetching_changes_sample`, mas na sua versão do repositório você pode, é claro, alterar o arquivo na `master`.

### Buscando as alterações (Fetch)

Ainda lembramos que quando você executa `git push`, sincroniza as alterações feitas no _Local Repository_ no _Remote Repository_.

Para obter as alterações feitas no _Remote_ no seu _Local Repository_, você usa o `git fetch`.

Isso obtém qualquer alteração do remoto - commits e branches - no seu _Local Repository_.

Observe que, neste ponto, as alterações ainda não estão integradas nas branches locais e, portanto, no _Working Directory_ e na _Staging Area_.

<!-- fetch.png -->
![Fazendo fetch das alterações](https://user-images.githubusercontent.com/29241659/87479640-38004f00-c602-11ea-8d76-8c7371fd6c7e.png)

Se você executar `git status` agora, verá outro ótimo exemplo de comandos git dizendo exatamente o que está acontecendo:

```ShellSession
> git status
On branch fetching_changes_sample
Your branch is behind 'origin/fetching_changes_sample' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
```

### Puxando as alterações (Pull)

Como não temos nenhuma alteração em _working_ ou _staged_, podemos executar o `git pull` agora para obter as alterações do _Remote Repository_ até a nossa área de trabalho.

> Puxar implicitamente também faz `fetch` do _Remote Repository_, mas as vezes é uma boa idéia fazer um `fetch` por si só.
> Por exemplo, quando você deseja sincronizar qualquer nova branch _remote_, ou quando deseja garantir que seu _Local Repository_ esteja atualizado antes de fazer uma `git rebase` em algo como `origin/master`.

<!-- pull.png -->
![Puxando mudanças](https://user-images.githubusercontent.com/29241659/87479670-42224d80-c602-11ea-98a7-68659f60f976.png)

Antes de puxarmos (`pull`), vamos alterar um arquivo localmente para ver o que acontece.

Vamos alterar o arquivo `Alice.txt` no nosso _Working Directory_!

Agora, se você tentar fazer um `git pull`, verá o seguinte erro:

```ShellSession
> git pull
Updating df3ad1d..418e6f0
error: Your local changes to the following files would be overwritten by merge:
        Alice.txt
Please commit your changes or stash them before you merge.
Aborting
```

Você não pode executar `pull` enquanto existirem modificações nos arquivos no _Working Directory_ que também são alteradas pelos commits que você está puxando (`pull`).

Embora uma maneira de contornar isso seja adicioná-las (`add`) ao _Staging Environment_ e criar o `commit`, este é um bom momento para aprender sobre outra excelente ferramenta, o `git stash`.

### Escondendo as alterações (Stash)

Se a qualquer momento você tiver alterações locais que ainda não deseja colocar em um commit, ou deseja armazenar em algum lugar enquanto tenta alguma forma diferente de resolver um problema, você pode esconder essas alterações.

Um `git stash` é basicamente uma pilha de alterações nas quais você armazena as alterações no _Working Directory_.

Os comandos que você mais irá utilizar são o `git stash`, que coloca qualquer modificação feita no _Working Directory_ em stash (ocultada), e o `git stash pop`, que recebe a última alteração que foi salva em stash e a aplica ao _Working Directory_ novamente.

Assim como os comandos de pilha com o nome, o `git stash pop` remove a última alteração escondida antes de aplicá-la novamente.
Se você não deseja remover as alterações do stash no momento de aplicá-las, pode usar o `git stash apply`.

Para inspecionar o seu `stash` atual, você pode usar `git stash list` para listar as entradas individuais, e `git stash show` para mostrar as alterações da última entrada no `stash`.

> Outro comando interessante é o `git stash branch {BRANCH NAME}`, que cria um branch a partir do HEAD no momento em que você armazenou as alterações e aplica as alterações armazenadas nessa branch.

Agora que sabemos sobre `git stash`, vamos executá-lo para remover nossas alterações locais em `Alice.txt` do _Working Directory_ para que possamos prosseguir e puxar (`git pull`) as alterações que fizemos no Github.

Depois disso, vamos executar `git stash pop` para recuperar as alterações.
Como tanto o commit que puxamos quanto a alteração que ocultamos (`stash`) modificam `Alice.txt`, você terá que resolver o conflito da mesma forma que faria em um `merge` ou `rebase`. Quando terminar, adicione (`add`) e _commite_ a alteração.

### Puxando (Pull) com conflitos

Agora que entendemos como buscar (`fetch`) e puxar (`pull`) as mudanças remotas em nosso _Dev Environment_, é hora de criar alguns conflitos!

Não mande `push` do commit que mudou `Alice.txt` e volte ao seu _Remote Repository_ em [github.com](https://www.github.com).

Lá vamos mudar `Alice.txt` novamente e _commitar_ a alteração.

Agora existem dois conflitos entre nossos _Local_ e _Remote Repositories_.

Não se esqueça de executar o `git fetch` para ver a mudança remota sem puxá-la (`pull`) imediatamente.

Se você executar o `git status`, verá que as duas branches têm um commit nelas diferente da outra.

```ShellSession
> git status
On branch fetching_changes_sample
Your branch and 'origin/fetching_changes_sample' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)
```

Além disso, alteramos o mesmo arquivo em ambos os commits para introduzir um conflito de `merge` que precisaremos resolver.

Quando você executa `git pull` enquanto existe uma diferença entre o _Local_ e o _Remote Repository_, exatamente a mesma coisa acontece quando você executa `merge` de 2 branches.

Além disso, você pode pensar no relacionamento entre ramificações no _Remote_ e aquele no _Local Repository_ como um caso especial de criação de uma ramificação com base em outra.
Uma ramificação local é baseada no estado de uma ramificação no _Remote_ desde a última vez que você a buscou (`fetch`).

Pensando assim, as duas opções que você possui para obter mudanças remotas fazem muito sentido:

Quando você executa `git pull`, as versões _Local_ e _Remote_ de um ramo serão mescladas (`merge`). Assim como mesclagem de branches isso apresentará um commit de _merge_.

Como qualquer ramificação _local_ é baseada em sua respectiva versão _remote_, também podemos executar `rebase`, para que qualquer alteração que possamos ter feito localmente apareçam como se fossem baseadas na versão mais recente disponível no _Remote Repository_.
Para fazer isso, podemos usar `git pull --rebase` (ou a abreviação `git pull -r`).

Conforme detalhado na seção [Rebasing](#rebasing), há um benefício em manter um histórico linear limpo, e é por isso que eu recomendo fortemente que sempre que você for executar `git pull`, execute como `git pull -r`.

> Você também pode dizer ao git para usar `rebase` em vez de `merge` como estratégia padrão quando executar `git pull`, configurando a configuração `pull.rebase` com um comando como este: `git config --global pull.rebase true`.

Se você ainda não executou o `git pull` quando o mencionei há alguns parágrafos atrás, agora vamos executar o `git pull -r` para obter as mudanças remotas, fazendo parecer que nosso novo commit aconteceu depois delas.

Obviamente, como em uma `rebase` normal (ou `merge`) você terá que resolver o conflito que introduzimos para que o `git pull` finalize.

## Cherry-picking

> Parabéns! Você chegou aos recursos mais avançados!

> Agora você entende como usar todos os comandos git típicos e, mais importante, como eles funcionam.
>
> Esperamos que isso torne os conceitos a seguir muito mais simples de entender do que se eu tivesse acabado de dizer quais comandos digitar.
>
> Então, vamos direto ao assunto e aprender fazer `cherry-pick` de commits!

> _Curiosidade:_ A tradução de `cherry-pick` é colher cereja.

Você ainda se lembra mais ou menos do que um `commit` é feito, certo?

E como seus commits são aplicados como novos commits, com o mesmo _change set_ e _message_ quando você faz o [`rebase`](#rebasing) de uma branch?

Sempre que você quiser apenas fazer algumas alterações de uma branch e aplicá-las a outra branch, você precisa fazer `cherry-pick` desses commits e colocá-los em sua branch.

É exatamente isso que o `git cherry-pick` permite que você faça com commits isolados ou com um agrupado de commits.

Assim como durante um `rebase`, isso realmente colocará as alterações desses commits em um novo commit em sua branch atual.

Vamos dar uma olhada nos exemplos de cada `cherry-pick` com um ou mais commits.

A figura abaixo mostra três branches antes de fazermos qualquer coisa. Vamos supor que realmente queremos obter algumas mudanças da branch `add_patrick` na branch `change_alice`. Infelizmente, eles ainda não entraram no master, portanto, não podemos apenas executar `rebase` na master para obter essas alterações (juntamente com outras alterações na outra branch, que talvez nem desejemos).

<!-- cherry_branches.png -->
![Branches antes do cherry-pick](https://user-images.githubusercontent.com/29241659/87479595-28810600-c602-11ea-9a0e-dd9eb7a81d29.png)

Então vamos fazer `git cherry-pick` do commit _63fc421_.
A figura abaixo mostra o que acontece quando executamos `git cherry-pick 63fc421`

<!-- cherry_pick.png -->
![Cherry-pick de um único commit](https://user-images.githubusercontent.com/29241659/87479601-2a4ac980-c602-11ea-8591-6763c088c75a.png)

Como você pode ver, um novo commit com as alterações que queríamos aparece na branch.

> Neste ponto observe que, como qualquer outro tipo de alteração de uma branch que já vimos antes, qualquer conflito que ocorra durante um `cherry-pick` precisará ser resolvido por nós, antes que o comando possa ser executado.
>
> Como todos os outros comandos, você pode continuar (`--continue`) um `cherry-pick` quando resolver os conflitos, ou abortar (`--abort`) o comando por completo.

A figura abaixo mostra um `cherry-pick` de um conjunto de commits em vez de um único. Você pode simplesmente fazer isso chamando o comando no formato `git cherry-pick <from>..<to>` ou, no nosso exemplo abaixo, como `git cherry-pick 0cfc1d2..41fbfa7`.

<!-- cherry_pick_range.png -->
![Cherry-pick de um conjunto de commits](https://user-images.githubusercontent.com/29241659/87479604-2c148d00-c602-11ea-9bff-20407bd7d876.png)

## Reescrevendo a história

> Estou me repetindo agora, mas você ainda se lembra de [`rebase`](# rebasing) bem o suficiente, certo? Caso contrário, volte rapidamente para essa seção antes de continuar aqui, pois usaremos o que já sabemos enquanto aprendemos a mudar o histórico!

Como você sabe, um `commit` contém basicamente suas alterações, uma mensagem e algumas outras coisas.

A história de uma branch é composta por todos os seus commits.

Mas digamos que você acabou de fazer um `commit` e, em seguida, observou que esqueceu de adicionar um arquivo ou que você cometeu um erro de digitação e a alteração deixou você com um código com bug.

Examinaremos brevemente duas coisas que poderíamos fazer para corrigir isso e fazer parecer que nunca aconteceu.

Vamos mudar para uma nova branch com `git checkout -b rewrite_history`.

Agora faça algumas alterações em `Alice.txt` e `Bob.txt` e, em seguida, execute `git add Alice.txt`.

Então faça o `commit` usando uma mensagem como "Essa é uma história" e pronto.

Espere, eu disse que terminamos? Não, você verá claramente que cometemos alguns erros aqui:

* Nós esquecemos de adicionar as mudanças de `Bob.txt`
* Nós não escrevemos uma [boa mensagem de commit](https://chris.beams.io/posts/git-commit/)

<!-- amending -->
### Alterando o último commit (Amend)
Uma maneira de corrigir ambos os itens de uma só vez seria alterar (`amend`) o commit que acabamos de fazer.

Alterar o último commit basicamente funciona como criar um novo.

Antes de fazer qualquer coisa, dê uma olhada no seu último commit, com `git show {COMMIT}`. Coloque o hash de confirmação (que você provavelmente ainda verá em sua linha de comando ao ter executado `git commit` ou no `git log`), ou apenas _HEAD_.

Assim como no `git log`, você verá a mensagem, o autor, a data e, claro, as alterações.

Agora vamos alterar (`amend`) o que fizemos nesse commit.

Execute `git add Bob.txt` para enviar as alterações para a _Staging Area_ e, em seguida, `git commit --amend`.

O que acontece a seguir é o desenrolamr do commit, as novas alterações da _Staging Area_ adicionadas no commit existente e a abertura do editor da mensagem de commit.

No editor, você verá a mensagem de commit anterior.
Sinta-se livre para alterá-lo para algo melhor.

Depois que você terminar, dê uma olhada no último commit com `git show HEAD`.

Como você certamente já esperava, o hash de confirmação é diferente. O commit original se foi e, em seu lugar, existe um novo, com as alterações combinadas e a nova mensagem de commit.

> Observe como os outros dados de commit, como autor e data, não são alterados em relação ao commit original. Você pode mexer com eles também, se você realmente quiser, usando os sinalizadores extras `--author={AUTHOR}` e `--date={DATE}` ao alterar.

Parabéns! Você acabou de reescrever a história pela primeira vez!

### Rebase interativo
<!-- squashing -->
Geralmente, quando executamos `git rebase`, nós fazemos `rebase` em uma branch. Quando fazemos algo como `git rebase origin/master`, o que realmente acontece é um rebase no _HEAD_ dessa branch.

De fato, se quiséssemos, poderíamos fazer `rebase` em qualquer commit.

> Lembre-se de que um commit contém informações sobre o histórico que veio antes dele

Como muitos outros comandos, o `git rebase` possui um modo _interactive_.

Diferente da maioria dos outros, o `rebase` _interativo_ é algo que você provavelmente estará usando muito, pois permite alterar o histórico o quanto quiser.

Especialmente se você seguir um fluxo de trabalho fazendo muitos pequenos commits de suas alterações, o que lhe permitirá voltar facilmente se cometer um erro,`rebase` interativo será o seu aliado mais próximo.

_Chega de conversa! Vamos fazer algo!_

Volte para a sua branch _master_ e faça `git checkout` de uma nova branch para trabalharmos nela.

Como antes, faremos algumas alterações em `Alice.txt` e `Bob.txt` e, em seguida, executaremos `git add Alice.txt`.

Em seguida, faça `git commit` usando uma mensagem como "Adicionar texto em Alice ".

Agora, em vez de alterar esse commit, execute `git add Bob.txt` e `git commit`. Como mensagem, usei "Adicionar Bob.txt".

E para tornar as coisas mais interessantes, faremos outra alteração em `Alice.txt`, na qual faremos `git add` e `git commit`. Como mensagem, usei "Adicionar mais texto a Alice".

Se agora analisarmos o histórico da branch com `git log` (ou apenas uma rápida olhada, de preferência com `git log --oneline`), veremos nossos três commits em cima do que estiver na sua _master_.

Para mim, aparece assim:
```ShellSession
> git log --oneline
0b22064 (HEAD -> interactiveRebase) Adicionar mais texto a Alice
062ef13 Adicionar Bob.txt
9e06fca Adicionar texto em Alice
df3ad1d (origin/master, origin/HEAD, master) Adicionar Alice
800a947 Adicionar texto do tutorial
```

Há duas coisas que gostaríamos de corrigir sobre isso, que, com o objetivo de aprender coisas diferentes, serão um pouco diferentes do que na seção anterior sobre `amend`:

* Coloque as duas alterações de `Alice.txt` em um único commit
* Nomeie as coisas de forma consistente e remova o _.txt_ da mensagem sobre `Bob.txt`

Para alterar os três novos commits, queremos fazer um rebase no commit antes deles. Esse commit para mim é `df3ad1d`, mas também podemos referenciá-lo como o terceiro commit do atual _HEAD_ como `HEAD~3`

Para iniciar um `rebase` _interativo_, usamos `git rebase -i {COMMIT}`, então vamos executar `git rebase -i HEAD~3`

O que você verá é o editor de sua escolha mostrando algo como isto:

```bash
pick 9e06fca Adicionar texto em Alice
pick 062ef13 Adicionar Bob.txt
pick 0b22064 Adicionar mais texto a Alice

# Rebase df3ad1d..0b22064 onto df3ad1d (3 commands)
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

Observe que o `git` sempre explica tudo o que você pode fazer quando você chama o comando.

Os comandos (_Commands_) que você provavelmente mais usará são `reword`, `squash` e `drop`. (E `pick`, mas esse está lá por padrão)

Reserve um momento para pensar sobre o que você vê e o que vamos usar para alcançar nossos dois objetivos de cima. Eu vou esperar.

Tem um plano? Perfeito!

Antes de começarmos a fazer alterações, observe que os commits são listados do mais antigo para o mais novo e, portanto, na direção oposta à saída do `git log`.

Vou começar com a alteração fácil e fazer com que possamos alterar a mensagem do commit do meio.

```bash
pick 9e06fca Adicionar texto em Alice
reword 062ef13 Adicionar Bob.txt
pick 0b22064 Adicionar mais texto a Alice

# Rebase df3ad1d..0b22064 onto df3ad1d (3 commands)
[...]
```

Agora para obter as duas alterações do `Alice.txt` em um commit.

Obviamente, o que queremos fazer é `squash` (compactar) o último dos dois commits no primeiro, então vamos colocar esse comando no lugar do `pick` no segundo commit, alterando `Alice.txt`. Para mim, no exemplo, isso é _0b22064_.

```bash
pick 9e06fca Adicionar texto em Alice
reword 062ef13 Adicionar Bob.txt
squash 0b22064 Adicionar mais texto a Alice

# Rebase df3ad1d..0b22064 onto df3ad1d (3 commands)
[...]
```

Nós terminamos? Isso fará o que queremos?

Não vai, né? Como os comentários no arquivo nos dizem:

```bash
# s, squash = use commit, but meld into previous commit
```

Portanto, o que fizemos até agora mesclará (merge) as alterações do segundo commit de Alice, com o commit de Bob. Não é isso que queremos.

Outra coisa poderosa que podemos fazer em um `rebase` _interativo_ é mudar a ordem dos commits.

Se você leu com atenção o que os comentários disseram, você já sabe como: Simplesmente mova as linhas!

Felizmente, você está no seu editor de texto favorito, então vá em frente e mova o segundo commit Alice para ficar logo após o primeiro.

```bash
pick 9e06fca Adicionar texto em Alice
squash 0b22064 Adicionar mais texto a Alice
reword 062ef13 Adicionar Bob.txt

# Rebase df3ad1d..0b22064 onto df3ad1d (3 commands)
[...]
```

Isso deve funcionar, então feche o editor e diga ao `git` para começar a executar os comandos.

O que acontece a seguir é como uma `rebase` normal: começando com o commit que você referenciou no início, cada um dos commits que você listou será aplicado um após o outro.

> Neste momento isso não acontecerá, mas quando você reordenar as alterações do código, poderá ocorrer que você entre em conflito durante o `rebase`. Afinal, você possivelmente misturou as mudanças que estavam desenvolvendo.
>
> Apenas [resolva](#resolvendo-conflitos) eles como faria normalmente.

Após aplicar o primeiro commit, o editor abrirá e permitirá que você coloque uma nova mensagem para o commit combinando as alterações em `Alice.txt`. Joguei fora o texto dos dois commits e coloquei "Adicionar vários textos importantes em Alice".

Depois de fechar o editor para concluir o commit, ele será aberto novamente para permitir que você altere a mensagem do commit `Adicionar Bob.txt`. Remova o ".txt" e continue fechando o editor.

É isso aí! Você reescreveu a história novamente. Desta vez, muito mais substancialmente do que quando utilizamos `amend`!

Se você olhar o `git log` novamente verá que há dois novos commits no lugar dos três que tínhamos anteriormente. Mas agora você já está acostumado com o que o `rebase` faz com commits e estava esperando por isso.

```
> git log --oneline
105177b (HEAD -> interactiveRebase) Adicionar Bob
ed78fa1 Adicionar vários textos importantes em Alice
df3ad1d (origin/master, origin/HEAD, master) Adicionar Alice
800a947 Adicionar texto do tutorial
```

<!-- changing meta data?>

<!-- force pushing -->
### História pública, por que você não deve reescrevê-la e como fazer isso com segurança

Como observado anteriormente, a alteração do histórico é uma parte incrivelmente útil de qualquer fluxo de trabalho que envolve fazer muitos pequenos commit enquanto você trabalha.

Embora todas as pequenas alterações atômicas tornem muito fácil para você, por exemplo, verificar se a cada alteração que seu conjunto de testes ainda passa e, se não, remover ou emendar apenas essas alterações específicas, os 100 commits que você fez para escrever `HelloWorld.java` provavelmente não são algo que você deseja compartilhar com as pessoas .

Muito provavelmente o que você deseja compartilhar com eles são algumas alterações bem-formadas, com boas mensagens de commit, informando aos colegas o que você fez por qual motivo.

Enquanto todos esses pequenos commits existirem apenas no seu _Dev Environment_, você estará perfeitamente seguro para fazer um `git rebase -i` e alterar o histórico para o conteúdo do seu coração.

As coisas ficam problemáticas quando se trata de mudar a _história pública_. Isso significa qualquer coisa que já tenha chegado ao _Remote Repository_.

Nesse ponto, tornou-se público e as branches de outras pessoas podem se basear nessa história. Isso realmente faz com que você geralmente não queira mexer.

O conselho usual é "nunca reescrever a história pública!" e enquanto repito isso aqui, devo admitir que há uma quantidade decente de casos em que você ainda pode reescrever a _história pública_.

Em todos esses casos, a história não é "realmente" pública. Você certamente não deseja reescrever o histórico na branch _master_ de um projeto de código aberto, ou algo como a branch _release_ da sua empresa.

Onde você pode querer reescrever a história são branches que você empurrou (`push`) apenas para compartilhar com alguns colegas.

Você pode estar desenvolvendo em trunk-based, mas deseja compartilhar algo que ainda não é compilado, portanto, obviamente, não deseja colocar isso na branch principal conscientemente.
Ou você pode ter um fluxo de trabalho no qual compartilha branch de feature.

Especialmente com as branches de feature, espero que você faça `rebase` com freqüência no _master_ atual. Mas, como sabemos, um `git rebase` adiciona os commits de nossas branches à medida que novos commits se baseiam naquilo em que os baseamos. Isso reescreve a história. E, no caso de uma branch de feature compartilhada, ele reescreve a _história pública_.

Então, o que devemos fazer se seguirmos o mantra "Nunca reescrever a história pública"?

Nunca fazer rebase da nossa branch e esperar que ele ainda mergeie com a _master_ no final?

Não usar branches de features compartilhadas?

É certo que o segundo é realmente uma resposta razoável, mas você ainda não pode fazer isso. Portanto, a única coisa que você pode fazer é aceitar reescrever a _história pública_ e empurrar (`push`) o histórico alterado para o _Remote Repository_.

Se você fizer um `git push`, você será notificado de que não está autorizado a fazer isso, pois sua branch _local_ divergiu da _remote_.

Você precisará forçar (`force`) o envio das alterações e substituir o remoto pela sua versão local.

Como destaquei isso de forma sugestiva, você provavelmente está pronto para tentar o `git push --force` no momento. Você realmente não deveria fazer isso se quiser reescrever a _história pública_ em segurança!

Você está muito melhor usando o irmão mais cuidadoso do `--force`, `--force-with-lease`!

O `--force-with-lease` irá verificar se a sua versão _local_ da branch _remote_ e o atual _remote_ correspondem, antes de fazer o `push`.

Com isso, você pode garantir que não irá apagar acidentalmente nenhuma alteração que alguém possa ter dado `push` enquanto você reescreveu o histórico!

<!-- force_push.png -->
![O que acontece com push --force-with-lease](https://user-images.githubusercontent.com/29241659/87479653-3cc50300-c602-11ea-9b1f-4044c7a655aa.png)

E nessa nota, deixarei você com um mantra ligeiramente alterado:

_Não reescreva o histórico público, a menos que tenha certeza do que está fazendo. E se você o fizer, esteja seguro e force-with-lease._

## Lendo a história

Conhecendo as diferenças entre as áreas em seu _Dev Environment_ - especialmente o _Local Repository_ - e como os commits e o histórico funcionam, fazer um `rebase`não deve ser assustador para você.

Mesmo assim, as vezes as coisas dão errado. Você pode ter feito um `rebase` e acidentalmente aceitado a versão errada do arquivo ao resolver um conflito.

Agora, em vez do recurso que você adicionou, apenas os seus colegas adicionaram a linha de logon em um arquivo.

Felizmente o `git` está ao seu lado por ter um recurso de segurança interno chamado logs de referência (_Reference Logs_), também conhecido como `reflog`.

Sempre que qualquer _referência_ como a ponta de uma branch é atualizada no seu _Local Repository_, uma entrada no _Log de Referência_ é adicionada.

Portanto, há um registro de qualquer momento em que você faz um `commit`, mas também de quando você redefiniu (`reset`) ou moveu o `HEAD` etc.

Depois de ler este tutorial até agora, você vê como isso pode ser útil quando estragamos um `rebase`, certo?

Sabemos que um `rebase` move o `HEAD` da nossa branch até o ponto em que o baseamos e aplica nossas alterações. Um `rebase` interativo funciona da mesma forma, mas pode fazer coisas com esses commits como _squashing_ ou _rewording_ eles.

Se você ainda não está na branch em que praticamos o [rebase interativo](#rebase-interativo), mude para ela novamente, pois estamos prestes a praticar um pouco mais lá.

Vamos dar uma olhada no `reflog` das coisas que fizemos nessa branch - você adivinhou como - executando o `git reflog`.

Você provavelmente verá muita informação na saída, mas as primeiras linhas na parte superior devem ser semelhantes a esta:

```bash
> git reflog
105177b (HEAD -> interactiveRebase) HEAD@{0}: rebase -i (finish): returning to refs/heads/interactiveRebase
105177b (HEAD -> interactiveRebase) HEAD@{1}: rebase -i (reword): Adicionar Bob
ed78fa1 HEAD@{2}: rebase -i (squash): Adicionar vários textos importantes em Alice
9e06fca HEAD@{3}: rebase -i (start): checkout HEAD~3
0b22064 HEAD@{4}: commit: Adicionar mais texto a Alice
062ef13 HEAD@{5}: commit: Adicionar Bob.txt
9e06fca HEAD@{6}: commit: Adicionar texto em Alice
df3ad1d (origin/master, origin/HEAD, master) HEAD@{7}: checkout: moving from master to interactiveRebase
```

Aí está. Tudo o que fizemos, desde a mudança para a branch até o `rebase`.

É muito legal ver as coisas que fizemos, mas inútil por si só se erramos em algum lugar, se não fosse pelas referências no início de cada linha.

Se você comparar a saída de `reflog` com a última vez que examinamos o `log`, verá esses pontos relacionados às referências de commit, e podemos usá-las dessa maneira.

Digamos que realmente não quiséssemos fazer o rebase. Como nos livramos das alterações feitas?

Nós movemos o `HEAD` para o ponto anterior ao `rebase` iniciado com um `git reset 0b22064`.

> `0b22064` é o commit antes de `rebase` no meu caso. De um modo mais geral, você também pode fazer referência a ele como _HEAD de quatro mudanças atrás_ via `HEAD@{4}`. Observe que, se você tiver alternado entre as branches ou tiver feito alguma outra coisa que crie uma entrada de log, poderá ter um número maior lá.

Se você der uma olhada no `log` agora, verá o estado original com três commits individuais restaurados.

Mas digamos que agora percebemos que não era isso que queríamos. O `rebase` está bom, nós simplesmente não gostamos de como mudamos a mensagem do commit de Bob.

Nós poderíamos simplesmente fazer outro `rebase -i` no estado atual, exatamente como fizemos originalmente.

Ou usamos o reflog e voltamos para depois do rebase e alteramos o commit a partir daí com `amend`.

Mas agora você já sabe como fazer isso, então deixarei você tentar por conta própria. Além disso, você também sabe que existe o `reflog` que permite desfazer a maioria das coisas que você pode acabar fazendo por engano.

## Treinando comandos git

O site [try github](http://try.github.io/), precisa de apenas **15 minutos** para aprendermos **Git**.

Ignorando uma possível instalação do git e utilizando de um `prompt de comando` com controle de versão direto do seu navegador.
 
O Try Git, de forma prática e rápida, acaba por facilitar todo o fluxo de aprendizagem do Git.

Mesmo utilizando de linhas de comando, o Try Git vem com diversas instruções de _passo a passo_ além de toda a representação visual de um repositório Git.

Com essas instruções, é possível notarmos algumas _dicas e truques_ para serem aplicados ao Git.

###### Que tal analisarmos?

> dica:

O **Try Git** também se integra perfeitamente ao **GitHub** via OAuth e é possível enviarmos os nossos repositórios de aprendizagem/tutorial para conta GitHub como um repo chamado `try_git`.

---

**Aprendeu algo com o treinamento? É quase de graça, basta deixar uma star ⭐ no [repositório](https://github.com/PauloGoncalvesBH/treinamento-git).**
