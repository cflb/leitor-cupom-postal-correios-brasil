# Gerente de Rastreio Correios

## Objetivo

Armazenar e arquivar códigos de rastreio de pedidos/encomendas postada nos Correios do Brasil

## Como funciona?

- Retire uma foto de todos os seus cupons de postagem, salve-os dentro de um diretorio e compacte utilizando o farmato ZIP.
- Faça o upload do seu arquivo ZIP na tela inicial.
- Espere, Espere um pouco a depender da quantidade de cupons o processo é um pouco demorado.

### Observação: Inicialmente projetado apenas para descompactar ZIP.

## implementação do Cata-Rastreio

Utilitário implementado com python + pytersseract

OBS.: Necessário a instalação do tesseract no seu sistema operacional.

## Etapas:

1. Descompacte o arquivo
2. Execute o utilitario cata-rastreio.py
3. Armazene em uma base de dados cada codigo:
    - CEP
    - RASTREIO
    - ID Cliente
4. Para apresentar o código renderize uma tela com campo de busca: CEP/ID Clietne