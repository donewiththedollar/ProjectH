echo -e "Iniciando La Instalacion"

pip install colorama

sudo apt install curl wget -y

sudo apt install curl -y

curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall

chmod 755 msfinstall

echo -e "Instalacion terminada"
