echo -e "Iniciando Instalacion..."

pkg install slowloris -y

pip install colorama -y

pkg install curl wget -y

pkg install curl -y

wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh

chmod +x metasploit.sh

echo -e "Instalacion Terminada..."
