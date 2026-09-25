# Qlik Github - Pipeline

Framework para versionar, documentar e gerenciar scripts de carga do Qlik Sense com Git — substituindo o modelo de edição direta no editor por um fluxo baseado em branches, Pull Requests e revisão antes de produção.

Desenvolvido e validado em ambiente corporativo com **38 aplicativos**, **602 abas** e **~42.600 linhas de script**.

---

## O problema que este projeto resolve

Em ambientes Qlik Sense sem versionamento, os scripts existem apenas dentro do editor. Isso gera:

- **Sem histórico real.** Quando uma carga quebra, não há como responder "o que mudou?" ou "quem alterou?".
- **Risco de perda irreversível.** Um erro de edição ou sobrescrita não tem reversão.
- **Colaboração por duplicação.** Dois analistas no mesmo app precisam de cópias paralelas e comparações manuais.
- **Custo alto de contexto para IA.** Copiar seção por seção do editor para uma sessão de manutenção consumia ~15 minutos por app.
- **Backup inexistente na prática.** Snapshot de um ecossistema de 600+ abas significaria horas de cópia manual.

---

## Como funciona

### Estrutura de cada app

```
apps/APP-ExemploPainel/
├── script.qvs        ← montado automaticamente, não editar
└── sections/         ← edite aqui, uma aba por arquivo
    ├── 00_Conexoes.qvs
    ├── 01_Calendario.qvs
    ├── 02_Extracao.qvs
    └── 99_Section_Access.qvs
```

O `script.qvs` é carregado pelo Qlik via:

```
$(Must_Include=lib://CNXDIR-GitHub/apps/APP-ExemploPainel/script.qvs)
```

### Fluxo de trabalho

```
1. git checkout -b feat/nome-da-alteracao
2. Editar o arquivo em sections/ correspondente
3. python tools/export_qlik_scripts.py --assemble APP-ExemploPainel
4. git add . && git commit -m "feat: descrição objetiva"
5. Abrir Pull Request → revisão → merge
6. Qlik recarrega via Include automaticamente
```

---

## Estrutura do repositório

```
qlik-git-pipeline/
├── apps/
│   ├── EXT-ExemploExtrator/
│   ├── TRF-ExemploTransformador/
│   └── APP-ExemploPainel/
├── includes/
│   ├── Conexoes.qvs
│   ├── Calendario.qvs
│   └── RegrasDeNegocio.qvs
├── tools/
│   └── export_qlik_scripts.py
├── docs/
│   ├── GOVERNANCA.md
│   └── CARGA_VIA_INCLUDE.md
├── .github/workflows/check-assemble.yml
├── .gitattributes
├── CONTRIBUTING.md
└── README.md
```

---

## Convenção de nomenclatura

| Prefixo  | Tipo                               | Exemplo                 |
| -------- | ---------------------------------- | ----------------------- |
| `EXT-` | Extrator (fonte → QVD)            | `EXT-Pedidos`         |
| `TRF-` | Transformador (QVD → QVD tratado) | `TRF-Pedidos`         |
| `APP-` | Aplicativo final (dashboard)       | `APP-GestaoDePedidos` |

---

## Convenção de commits

```
feat:     nova funcionalidade ou script
fix:      correção de bug ou carga quebrada
docs:     documentação
style:    formatação sem mudança de lógica
chore:    manutenção e configuração
refactor: refatoração sem mudança de comportamento
```

Vincule ao chamado quando aplicável:

```
fix: corrige filtro de região no APP-GestaoDePedidos

Chamado #12345 — vendedor sem região aparecia no total geral.
```

---

## Resultados em produção

| Métrica                      | Antes                                 | Depois                                                 |
| ----------------------------- | ------------------------------------- | ------------------------------------------------------ |
| Histórico de alterações    | Comentário manual inconsistente      | Commit com autor, data e diff                          |
| Reversão de erro             | Impossível                           | `git revert` em segundos                             |
| Colaboração entre analistas | Apps duplicados + comparação manual | Branches + PR + diff automático                       |
| Contexto por sessão de IA    | ~15 min de cópia manual              | Referência direta ao`.qvs`                          |
| Backup do ecossistema         | ~10h de cópia aba a aba              | `git clone`                                          |
| Apps versionados              | 0                                     | 38 (7 extratores · 14 transformadores · 17 painéis) |

---

## Autor

**André Felipe dos Santos Ricardo**
Data & IA Engineer — Joinville, SC

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/itsandrezl/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/itsandrezl)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://itsandrezl.github.io)
