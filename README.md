# Envio de E-mail com Imagens em Python <img src='https://github.com/andref-tech/andref-tech/blob/main/Python-programming-logo-on-transparent-background-PNG.png' width='70'>

## Descrição do Projeto 

Este projeto é uma aplicação em Python que utiliza a biblioteca **smtplib** para enviar e-mails com conteúdo HTML e imagens anexadas. O código permite que o usuário configure o remetente, destinatário, assunto e corpo do e-mail, incluindo a possibilidade de anexar imagens.

## Estrutura do Projeto

O projeto é composto por um único arquivo:

1. **send_email.py**: O arquivo principal que contém a lógica para enviar e-mails com imagens.

## Funcionalidades

- **Envio de E-mail**: Permite enviar e-mails para destinatários especificados.
- **Suporte a HTML**: O corpo do e-mail pode ser formatado em HTML.
- **Anexos de Imagens**: Possibilidade de anexar imagens ao e-mail.

## Requisitos

- Python 3.x

###### Bibliotecas Python:
- smtplib
- email

## Instalação

Não há necessidade de instalação de bibliotecas adicionais, pois as bibliotecas utilizadas são parte da biblioteca padrão do Python.

## Como Usar

1. Configure as variáveis de e-mail no código:
   - `sender_email`: E-mail do remetente.
   - `sender_password`: Senha do Google para aplicações.
   - `recipient_email`: E-mail do destinatário.
   - `subject`: Título do e-mail.
   - `html`: Corpo do e-mail em HTML.

2. Execute o arquivo `send_email.py`:

   ```bash
   python send_email.py

## Estrutura do Código

O código contém as seguintes partes principais:

- **Função guess_mime_type:** Determina o tipo MIME da imagem.
- **Configurações do e-mail:** Define remetente, destinatário e assunto.
- **Corpo do e-mail:** Define o conteúdo em HTML.
- **Anexar imagens:** Lê e anexa as imagens ao e-mail.
- **Enviar e-mail:** Conecta ao servidor SMTP e envia o e-mail.
