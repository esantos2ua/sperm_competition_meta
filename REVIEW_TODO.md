# Revisão pendente: recuperação da análise de 2018

Criado em 2026-09-24, branch `recover-2018-analysis` (commit `15638d2`).
PR: https://github.com/esantos2ua/sperm_competition_meta/pull/new/recover-2018-analysis

Os modelos da dissertação foram refeitos a partir da planilha original (variâncias exatas) em
`analysis/01_baseline_models.R`. Isso mudou afirmações do manuscrito. Marque cada item ao revisar.

## Mudanças de interpretação (discutir com a Lygia)

- [ ] **Viés de publicação invertido.** O Egger original (`lm(resíduos ~ v)`) lia só o intercepto.
      O Egger multinível (√v como moderador) mostra efeito de estudos pequenos em todos os modelos:
      nulo +1.633 (p < 0.001), Modelo 1 +1.426 (p < 0.001), Modelo 2 +0.862 (p = 0.031).
      Texto novo em `manuscript.typ`, seção "Publication bias diagnostics". Considerar análises
      de sensibilidade (média ajustada, remoção de extremos) já nesta versão.
- [ ] **SCR significativo no Modelo 2.** Deixar o efeito variar por SCR dentro de cada categoria melhora
      o ajuste (LRT χ² = 67.69, gl = 11, p < 0.001). Antes o texto dizia "sem moderação significativa". O novo texto
      diz que o teste omnibus não mostra por si só o pico em risco intermediário. Decidir a interpretação.
- [ ] **I² corrigido.** O script original usava pesos 1/√v na variância amostral típica (Eq. 22 de
      Nakagawa & Santos 2012 usa 1/v). O I² total do modelo nulo foi de 83.24% para 93.39%. O manuscrito cita os dois.
- [ ] Rever o **Resumo e a Discussão**: ainda não foram reescritos à luz dos itens acima.

## Decisões pendentes

- [ ] **Número de espécies:** *Parablennius parvicornis* e *P. sanguinolentus parvicornis* aparecem
      como espécies distintas, mas caem na mesma ponta da árvore. Se forem sinônimos, são 28 espécies, não 29.
- [ ] **Tabela 3 / crosscheck com Dougherty et al. (2022):** os números 31 compartilhados / 19 não incluídos /
      27 só Dougherty foram calculados sobre 50 estudos. Só 48 estudos têm efeitos entre os 183 analisados. Conferir.
- [ ] **Efeitos extremos:** 7 dos 183 têm |g| > 8 (8 entre as 207 linhas). Priorizar a reextração.
- [ ] **Visibilidade do repo:** `esantos2ua/sperm_competition_meta` está **público** e contém o PDF da
      dissertação e dados não publicados. Decidir se vira privado (`gh repo edit --visibility private`).
- [ ] Fazer merge do branch `recover-2018-analysis` em `main` depois da revisão.

## Conferências rápidas

- [ ] Fig. 4 (funnel) agora usa dados reais. Os efeitos extremos aparecem na borda do gráfico. Ver se o
      eixo do erro padrão (até ~7.7, por causa de um único ponto) precisa de ajuste visual.
- [ ] Fig. 1 (PRISMA): o texto da caixa final mudou para "50 (48 contributing…)".
- [ ] Protocolo `02_update_protocol.{md,typ}`: passos 3–5 da seção Q0 foram reescritos (dados recuperados).
      Se o protocolo já foi registrado (OSF), isso deve ir como emenda, não como edição silenciosa.

## Fora do escopo desta recuperação

A planilha de 2018 **não** tem médias e DPs por morfo das variáveis de esperma, só g e variância.
A reextração por morfo do Q1 continua necessária.
