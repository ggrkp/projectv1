# projectv1
AutoML GUI using PyQT &amp; auto-sklearn

conda create -n automl_env

conda activate automl_env

conda install python=3.8

conda install gxx_linux-64 gcc_linux-64 swig

curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip3 install 

pyp3 install pyfr

pip3 install auto-sklearn

conda install -c conda-forge featuretools

conda install -c anaconda pyqt

conda install -c conda-forge sqlite