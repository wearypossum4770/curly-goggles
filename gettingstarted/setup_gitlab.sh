##################################################################################################################################################################
# Install Prep 
##################################################################################################################################################################
DISTRO="$(lsb_release -s -c)"
#~ Replace with the branch of Node.js or io.js you want to install: node_6.x, node_8.x, etc...
NODE_VERSION=node_8.x
ERLANG_VERSION=23.x

sudo apt install -y build-essential protobuf-compiler python libprotobuf-dev libcurl4-openssl-dev libboost-all-dev libncurses5-dev libjemalloc-dev wget m4 binutils-doc debian-keyring g++-multilib g++-8-multilib gcc-8-doclibstdc++6-8-dbg gcc-multilib autoconf automake libtool flex bison gdb gcc-doc gcc-8-multilib gcc-8-locales libgcc1-dbg libgomp1-dbg libitm1-dbg libatomic1-dbg libasan5-dbg liblsan0-dbg libtsan0-dbg libubsan1-dbg libmpx2-dbg libquadmath0-dbg libvte9 doc-base glibc-doc bzr libstdc++-8-doc make-doc python-crypto-doc python-cryptography-doc python3-cryptography-vectors python-dbus-doc python3-dbus-dbg gnome-keyring libkf5wallet-bin gir1.2-gnomekeyring-1.0 python-secretstorage-doc python-setuptools-doc build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev build-essential pkg-config erlang libicu-dev libmozjs185-dev libcurl4-openssl-dev curl gnupg apt-transport-https libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libgdm-dev libdb4o-cil-dev libpcap-dev
##################################################################################################################################################################
## Manual Building of 
##################################################################################################################################################################

#--------------------------------------------------------------------------------------------------------
# PYTHON   
#--------------------------------------------------------------------------------------------------------
./configure CPPFLAGS="-I/usr/local/ssl/include" LDFLAGS="-L/usr/local/ssl/lib" --enable-optimizations && make -j4 && sudo make altinstall

#--------------------------------------------------------------------------------------------------------
# RETHINK DB Real-Time Database 
#--------------------------------------------------------------------------------------------------------
wget https://download.rethinkdb.com/repository/raw/dist/rethinkdb-2.4.0.tgz
tar xf rethinkdb-2.4.0.tgz
cd rethinkdb-2.4.0
./configure --allow-fetch
make -j4
sudo make install
##################################################################################################################################################################
# Add Package Repositories
##################################################################################################################################################################
#--------------------------------------------------------------------------------------------------------
# NODE JS
#--------------------------------------------------------------------------------------------------------
sudo add-apt-repository -y -r ppa:chris-lea/node.js && sudo rm -f /etc/apt/sources.list.d/chris-lea-node_js-*.list && sudo rm -f /etc/apt/sources.list.d/chris-lea-node_js-*.list.save
# wget can also be used:
# wget --quiet -O - https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -
					#--------------------------------------------------------------------------------------------------------
					# NODEJS AUTO BUILD 
					#--------------------------------------------------------------------------------------------------------
					#~ sudo curl -sL https://deb.nodesource.com/setup_14.x | bash - 
					#~ sudo apt-get install -y nodejs

echo "deb https://deb.nodesource.com/$NODE_VERSION $DISTRO main" | sudo tee /etc/apt/sources.list.d/nodesource.list && echo "deb-src https://deb.nodesource.com/$NODE_VERSION $DISTRO main" | sudo tee -a /etc/apt/sources.list.d/nodesource.list

#--------------------------------------------------------------------------------------------------------
# COUCHDB  
#--------------------------------------------------------------------------------------------------------
echo "deb https://apache.bintray.com/couchdb-deb stretch main" | sudo tee /etc/apt/sources.list.d/couchdb.list
#--------------------------------------------------------------------------------------------------------
# ARANGODB
#--------------------------------------------------------------------------------------------------------

echo 'deb https://download.arangodb.com/arangodb36/DEBIAN/ /' | sudo tee /etc/apt/sources.list.d/arangodb.list

#--------------------------------------------------------------------------------------------------------
# CASSANDRA DB 
#--------------------------------------------------------------------------------------------------------
echo "deb https://downloads.apache.org/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
#--------------------------------------------------------------------------------------------------------
# RETHINK DB Real-Time Database 
#--------------------------------------------------------------------------------------------------------

export CODENAME=`lsb_release -cs`
echo "deb https://download.rethinkdb.com/debian-$CODENAME $CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
#--------------------------------------------------------------------------------------------------------
# RABBITMQ Repository 
#--------------------------------------------------------------------------------------------------------
echo "deb https://dl.bintray.com/rabbitmq-erlang/debian $DISTRO erlang-$ERLANG_VERSION" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list

#--------------------------------------------------------------------------------------------------------
# POSTGRESQL 
#--------------------------------------------------------------------------------------------------------
#sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
##################################################################################################################################################################
## Add Package Repositories KEYS
##################################################################################################################################################################
#--------------------------------------------------------------------------------------------------------
# NODEJS  
#--------------------------------------------------------------------------------------------------------
sudo curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -

#--------------------------------------------------------------------------------------------------------
# RABBITMQ 
#--------------------------------------------------------------------------------------------------------
sudo curl -fsSL https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc | sudo apt-key add -

#--------------------------------------------------------------------------------------------------------
# ARANGODB
#--------------------------------------------------------------------------------------------------------

curl -OL https://download.arangodb.com/arangodb36/DEBIAN/Release.key
sudo apt-key add - < Release.key

#--------------------------------------------------------------------------------------------------------
# COUCHDB 
#--------------------------------------------------------------------------------------------------------
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8756C4F765C9AC3CB6B85D62379CE192D401AB61
#--------------------------------------------------------------------------------------------------------
# POSTGRESQL 
#--------------------------------------------------------------------------------------------------------
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

#--------------------------------------------------------------------------------------------------------
# RETHINK DB Real-Time Database 
#--------------------------------------------------------------------------------------------------------
wget -qO- https://download.rethinkdb.com/repository/raw/pubkey.gpg | sudo apt-key add -
 wget -qO- https://download.rethinkdb.com/repository/raw/pubkey.gpg | sudo apt-key add -v -
##################################################################################################################################################################
## Install All Repository Packagees
##################################################################################################################################################################
sudo apt-get update -y
sudo apt-get install -y --fix-missing postgresql erlang-base  erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key erlang-runtime-tools erlang-snmp erlang-ssl erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl rabbitmq-server rethinkdb arangodb3 
##################################################################################################################################################################
## Confirm Installations
##################################################################################################################################################################
node -e "console.log('Hello from Node.js ' + process.version)"

##################################################################################################################################################################
## GIT GPG & SSH Keys
##################################################################################################################################################################

gpg --full-gen-key

gpg --list-secret-keys --keyid-format LONG $GPG_EMAIL
gpg --armor --export  $GPG_FINGERPRINT
git config --global user.name ""
git config --global user.email ""
git config --global user.signingkey $GPG_FINGERPRINT
git config --global commit.gpgsign true

