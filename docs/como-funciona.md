# Como a Skill Funciona por Dentro

[English](how-it-works.md) · **Português** · [繁體中文](how-it-works.zh-Hant.md)

A história de como o projeto começou abre o [README](../README.pt-BR.md). Esta página trata só de como as peças da skill funcionam juntas.

## Visão Geral

Quem participa quando alguém pede uma pecha: a pessoa, o aparelho que ela usa, o Claude com a skill e as fontes do texto.

```mermaid
flowchart TB
    subgraph internet [" "]
        subgraph fontes [" "]
            lotsawa(Lotsawa House)
            outras(Outras fontes)
        end
        subgraph nuvem [Claude]
            skill[[pecha.skill]]
            claude(Sonnet, Opus)
        end
    end

    subgraph canais [" "]
        celular(Celular)
        notebook(Notebook)
    end

    subgraph pessoa [" "]
        usuario(Usuário)
    end

    pessoa -->|pede a pecha| canais
    canais -->|envia o pedido| claude
    claude -->|lê e executa| skill
    skill -->|consulta o texto| fontes
    fontes -.->|devolve o texto| skill
    skill -.->|gera o PDF| claude
    claude -.->|entrega o PDF| canais
    canais -.->|PDF para imprimir| pessoa

    classDef grupo fill:transparent,stroke:#888780,stroke-dasharray: 5 5
    classDef servico fill:#F1EFE8,stroke:#888780,color:#2C2C2A
    classDef secundaria fill:#F1EFE8,stroke:#888780,color:#2C2C2A,stroke-dasharray: 3 3
    classDef tecnico fill:#ffffff,stroke:#888780,color:#2C2C2A
    class internet,fontes,canais,pessoa grupo
    class nuvem,lotsawa,usuario,celular,notebook servico
    class outras secundaria
    class skill,claude tecnico
```

## As Peças

- **A skill** (`SKILL.md`): as instruções que o Claude segue. Ela diz o que perguntar, quais opções usar e como conferir o resultado.
- **O motor** (`assets/pecha-engine.html`): um único arquivo HTML que faz a diagramação. Ele lê a página, monta as pechas, mede cada uma e decide onde quebrar o texto. Ele roda dentro de um navegador sem tela e não acessa a internet.
- **O script** (`scripts/make_pecha.py`): um programa em Python que abre o motor no Chromium sem tela, por meio do Playwright, passa a página e as opções, e grava o PDF e um relatório com as medidas de cada pecha.
- **As fontes** (`assets/fonts/`): Noto Serif Tibetan para o tibetano, e Noto Serif e Noto Serif Italic para o texto latino, sob a SIL Open Font License.

## A Fonte Tibetana

O tibetano sai em [Noto Serif Tibetan](https://fonts.google.com/noto/specimen/Noto+Serif+Tibetan), da família [Noto](https://fonts.google.com/noto) do Google, desenhada pela [equipe de design da Monotype](https://github.com/notofonts/tibetan). O estudo da escrita tibetana para a Noto Tibetan foi feito pelo designer de tipos Toshi Omagari, que trabalhou na Monotype de 2012 a 2020, com o apoio do estudioso budista Shojiro Nomura e a revisão de monges tibetanos. O caderno de esboços dele, com os primeiros desenhos da Noto Tibetan, foi doado ao Design Museum, e ele apresentou a palestra "Making Noto Sans Tibetan" na conferência Granshan de 2015 ([perfil de Toshi Omagari](https://tosche.net/profile) e [estudo de caso da Monotype](https://enterprise.monotype.com/resources/case-studies/creating-noto-google)).

[![Creating Noto for Google, imagem do Google sobre a criação das fontes Noto](https://www.gstatic.com/images/icons/material/apps/fonts/1x/catalog/v5/noto/creating_noto_for_google_720.png)](https://youtu.be/16_NYHUZ1kM)

*Imagem: Google. Clique nela para ver no YouTube o vídeo "Creating Noto for Google", da Monotype, sobre como as fontes Noto foram criadas.*

## Do Endereço ao PDF

1. A pessoa pede uma pecha e dá o endereço de uma página da Lotsawa House, ou anexa a página salva.
2. O Claude, seguindo a skill, pergunta só o que a página deixa em aberto, como os títulos que o tradutor colocou no meio do texto.
3. O script abre o motor, que lê as camadas pela marcação da própria página: tibetano, transliteração e tradução. Nenhuma inteligência artificial lê ou reescreve o texto nesse caminho ([`SKILL.md`](../SKILL.md)).
4. O motor monta as pechas de 297 × 105 mm, duas por folha A4 paisagem, e o script grava o PDF.
5. O Claude confere o relatório, escolhe o nome do texto para a margem e entrega o PDF.

Quando o texto vem de outra fonte, como outro site ou uma tradução própria, o Claude converte o texto para um formato intermediário e a pessoa confere antes do PDF. Em qualquer caminho, a página de créditos diz que a pecha foi preparada com apoio de inteligência artificial e precisa ser revisada antes do estudo e da prática.

Dentro do pacote da skill, três peças fazem o trabalho, uma depois da outra:

```mermaid
flowchart TB
    pdf(PDF)
    modelo(Claude Sonnet, Opus)
    fonte(Lotsawa House, outras fontes)

    subgraph pacote [pecha.skill]
        skillmd[[SKILL.md]]
        script[[make_pecha.py]]
        motor[[pecha-engine.html]]
    end

    modelo -->|segue| skillmd
    skillmd -->|manda rodar| script
    fonte -->|texto| script
    script -->|abre| motor
    motor -->|monta| pdf

    classDef servico fill:#F1EFE8,stroke:#888780,color:#2C2C2A
    classDef tecnico fill:#ffffff,stroke:#888780,color:#2C2C2A
    class pacote,fonte,pdf,modelo servico
    class skillmd,script,motor tecnico
```

## Decisões de Desenho

### Título Curto na Margem e Numeração em Algarismos Tibetanos

Cada pecha leva, na margem esquerda, o nome curto do texto em tibetano e, na margem direita, o número da pecha em algarismos tibetanos, como numa pecha tradicional. O nome da margem é escolhido pela skill a partir do título do texto, porque o corte automático às vezes devolve o nome do ciclo, e não o da prece.

### Título Maior na Capa

A capa traz o título tibetano a partir de 28 pt e o título traduzido em 14 pt. O tamanho foi escolhido comparando quatro combinações na mesma capa, porque o título traduzido em 12 pt ficava pequeno demais perto do tibetano.

### Linhas da Moldura

A moldura dupla sai com duas linhas finas por padrão. Para uma moldura mais marcada, uma linha de cada par pode ser grossa: a grossa por fora, ou a grossa por dentro. A moldura cresce para fora o que a linha grossa acrescenta, e o texto quebra nos mesmos pontos nas três molduras.

### Impressão em Frente e Verso

A pecha pode sair em uma face só, que é o padrão, ou em frente e verso. No frente e verso, a skill prepara o PDF para a folha ser virada pela borda longa.

### Títulos do Tradutor

Alguns tradutores colocam no meio do texto títulos só em inglês, sem tibetano. A skill pergunta a cada texto se eles seguem no fluxo, se cada um abre uma pecha nova ou se ficam de fora, porque o melhor caminho muda de um texto para outro.

### Sinal de Terma

Nos textos de tesouro revelado (terma), os versos tibetanos terminam com o sinal ༔. A skill repete esse sinal ao fim da transliteração e da tradução de cada verso que o traz, colado à última palavra. É uma boa prática de edição e um sinal de respeito pelo tesouro revelado. A skill reconhece o terma sozinha, quando a maioria dos versos tibetanos termina com o sinal ([`SKILL.md`](../SKILL.md)).

### Tamanho do Tibetano

O tibetano sai em 19 pt quando divide a pecha com outras camadas e em 21 pt quando vem sozinho. O espaço em branco é medido da moldura até o corpo das letras, e não até os sinais de vogal, para que a pecha pareça equilibrada a olho nu.
