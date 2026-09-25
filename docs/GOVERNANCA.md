# Governança do Repositório

## Princípios

1. **Nenhuma alteração vai direto para main.** Todo trabalho começa em uma branch e passa por Pull Request.
2. **O script.qvs nunca é editado manualmente.** Edite em `sections/` e remonte com a ferramenta.
3. **Todo commit referencia o chamado** quando aplicável.
4. **Includes são a fonte da verdade** para lógica compartilhada (conexões, calendário, regras).

## Branches

| Branch | Propósito |
|--------|-----------|
| `main` | Produção. Protegida — só aceita merge via PR aprovado. |
| `feat/<descricao>` | Nova funcionalidade ou novo script |
| `fix/<descricao>` | Correção de bug ou carga quebrada |
| `docs/<descricao>` | Documentação |

## Pull Requests

- Título: igual ao commit principal (`feat: ...`, `fix: ...`)
- Descrição: o que mudou e por quê
- Vincule ao chamado no corpo do PR
- Ao menos um aprovador antes do merge

## Controle de Alterações (antes e depois)

| Antes (sem Git) | Depois (com Git) |
|-----------------|-----------------|
| Comentário manual no topo do script | Commit com autor, data e diff linha a linha |
| Sem como reverter | `git revert <hash>` em segundos |
| Dois analistas no mesmo app = conflito manual | Branches paralelas + merge automático |
| Histórico dependia de alguém lembrar de escrever | Histórico automático e auditável |
