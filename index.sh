#!/bin/bash

# Pedir nome de usuário e senha
echo "Digite seu nome de usuário:"
read usuario
echo "Digite sua senha:"
read -s senha

# Verificar se o nome de usuário e senha estão corretos
if [ "$usuario" = "admin" ] && [ "$senha" = "123" ]
then
    echo "Login realizado com sucesso!"
else
    echo "Nome de usuário ou senha incorretos"
fi
