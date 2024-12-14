# PyTranslator
Tradutor de Linguagens Feito em Python

# Como Funciona?
Cada Arquivo Tem Sua Própria Linguagem, Basta Baixar o Código, Importar o Arquivo da Linguagem que Preferir e Usar as Funções(Ou Classe) da Linguagem.

# Morse
A Função: translateToMorse(), é a Função para Traduzir um Texto Para Morse. Já A Função translateMorseToText() é a Função de Tradução de Morse Para Texto Plano. Deve Ser Usado o Morse no Padrão: "--- / ... / ---"

# Binário
A Função: translateToBinary(), é a Função para Traduzir Texto Para Binário. Já a Função translateBinaryToText() é a Função Para Traduzir Binário Para Texto. Deve Ser Usado o Padrão: "01000001 01000010 01000011"

# Hexadecimal
A Função: translateToHex(), é a Função para Traduzir Texto Para Hexadecimal. Já a Função translateHexToText() é a Função para Traduzir Hexa Para Texto. Os Únicos Caractéres Possíveis São os Números de 0 a 9 e as Letras de A a F. O Padrão de Tradução Deve Ser: "0x0 0xa 0xf"

# Hexadecimal (Alpha)
Usando Como Base o Hexadecimal Convencional de 0 a 9 e de A a F. Ele Expande de 0 a 9 e de A a Z. A Função translateToHexAlpha() Converte Texto Para Hexa, e a Função translateHexAlphaToText() é a Função que Traduz de Volta a Texto Plano. O Padrão de Tradução Deve Ser: "0x00 0x1c 0x09"

# Hash
A Classe HashFy Contem deve ser Chamada da Seguinte Forma: "Hash = hash.HashFy("Hello Friend")" E ao Usar as Funções Respectivas da Hash Requisitada como Por Exemplo: "Hash.Sha256()" Ira Retornar o Texto "Hello Friend" em Hash SHA256
