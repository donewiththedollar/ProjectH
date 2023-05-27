echo -e "Iniciando La Instalacion"

pip3 install slowloris -y

pip3 install colorama

sudo apt install curl wget -y

sudo apt install curl -y

chmod +x MiniLav.py

chmod +x astronet.py

curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall

chmod 755 msfinstall

echo -e "Instalacion terminada"
