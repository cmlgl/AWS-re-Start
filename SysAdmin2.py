import subprocess


# Exibe os arquivos do diretório em listagem longa. Exibe o diretório "files"

subprocess.run(["ls","-l","files"])

# Usa o comando "uname -a" para exibir informações do sistema

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Usa o comando "ps -x" para exibir informações de disco (executando o comando "df")

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])