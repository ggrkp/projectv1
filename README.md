# projectv1

pyuic5 -x guiv1.ui -o guiv1.py 

WSL GIA WINDOWS OPERATING SYSTEM
WSL FILE EXPLORER PATH :            \\wsl$\Ubuntu-20.04\home\georgak

MINICONDA INSTALLATION
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh


AutoML GUI using PyQT &amp; auto-sklearn

conda create -n automl_env

conda activate automl_env

conda install python=3.8

conda install gxx_linux-64 gcc_linux-64 swig

curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip3 install 

pip3 install pyfr

pip3 install auto-sklearn

conda install -c conda-forge featuretools

conda install -c anaconda pyqt

conda install -c conda-forge sqlite
h 
sudo apt-get install sqlite3
sqlite3 --version (test)
sudo apt-get install sqlitebrowser (gia gui)

** pyinstaller gia na ftiaskw to app

GIA TO GITHUB:
gitlens-plugin (PUSH)
git installation sta windows

SQLITE
CREATE TABLE IF NOT EXISTS models(
    name TEXT,
    data BLOB,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    learning_type TEXT
);

GIA TSFRESH:
conda install -c conda-forge tsfresh




** Trouble shooting 
Could not connect to any X display.
INSTALL Xming h kapoion allon Xserver px vcXsrv




ERROR- >    configure email and username: (entoles sto terminal)
SOLUTION:   git config --global user.name ggrkp
            git config --global user.email g.georgak.77@gmail.com

            meta sto terminal tou wsl:
            export DISPLAY=:0
            Gia na exei graphics

            kai run to program


ERROR:      sqlitebrowser: error while loading shared libraries: libQt5Core.so.5: cannot open shared object file: No such file or directory
SOLUTION:   sudo apt-get install -y binutils
            sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5 
