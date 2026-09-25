# Como Funciona a Carga via Include

## O mecanismo

O Qlik Sense permite carregar scripts externos via a instrução `$(Must_Include=)`.
Este repositório usa essa feature para que cada app sempre execute a versão
mais recente do script versionado no GitHub.

## Configuração no QMC

1. Crie uma conexão de dados do tipo **Folder** apontando para a pasta onde
   o GitHub sincroniza os arquivos (ou para o caminho de rede mapeado).
2. Nomeie a conexão como `CNXDIR-GitHub` (ou ajuste o nome nos scripts).
3. Garanta que o servidor Qlik tenha acesso de leitura ao caminho.

## Instrução nos scripts

Cada `script.qvs` começa com:

```
$(Must_Include=lib://CNXDIR-GitHub/apps/NOME-DO-APP/script.qvs)
```

Na recarga, o Qlik lê o arquivo direto do repositório — qualquer merge em `main`
é refletido automaticamente na próxima execução.

## Includes compartilhados

```
$(Must_Include=lib://CNXDIR-GitHub/includes/Conexoes.qvs)
$(Must_Include=lib://CNXDIR-GitHub/includes/Calendario.qvs)
$(Must_Include=lib://CNXDIR-GitHub/includes/RegrasDeNegocio.qvs)
```

Altere uma vez, propaga para todos os apps que incluem o arquivo.
