# Guia de Contribuição

## Pré-requisitos

- Python 3.8+
- Git configurado com seu usuário corporativo
- Acesso de leitura/escrita ao repositório

## Configuração inicial

```bash
git clone <url-do-repositorio>
cd qlik-git-pipeline
```

## Fluxo completo

### 1. Criar branch

```bash
git checkout -b feat/nome-da-alteracao
```

### 2. Editar

Edite o arquivo `.qvs` correspondente dentro de `sections/`.
**Nunca edite `script.qvs` diretamente.**

### 3. Remontar

```bash
python tools/export_qlik_scripts.py --assemble NOME-DO-APP
```

### 4. Validar

```bash
python tools/export_qlik_scripts.py --check-assemble
```

### 5. Commit

```bash
git add .
git commit -m "feat: descrição objetiva da alteração"
```

Formato de commit:
```
feat:     nova funcionalidade ou script
fix:      correção de bug ou carga
docs:     documentação
style:    formatação sem mudança de lógica
chore:    manutenção
refactor: refatoração sem mudança de comportamento
```

Vincule ao chamado:
```
fix: corrige cálculo de margem no APP-ExemploPainel

Chamado #12345 — valor negativo aparecia em devoluções.
```

### 6. Pull Request

Abra o PR para `main` com título e descrição claros.
O CI valida automaticamente que `script.qvs` está sincronizado.

## O que não fazer

- Editar `script.qvs` manualmente
- Commitar credenciais, senhas ou strings de conexão reais
- Fazer push direto em `main`
- Deixar o campo de descrição do PR vazio
