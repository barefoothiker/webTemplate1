#!/bin/bash
yum update -y 
yum install -y \
  atlas \
  atlas-devel \
  blas \
  blas-devel \
  gcc \
  gcc-c++ \
  lapack \
  lapack-devel \
  nginx \
  python34 \
  python34-devel \
  python34-pip

pip-3.4 install --upgrade pip || touch $HOME/pip3upgradefailed

ln -sF /usr/local/bin/pip3 /usr/bin/pip3 || touch $HOME/linkfailed

pip3 install \
  coverage \
  Django \
  django-excel \
  django-nose \
  nose \
  numpy \
  openpyxl \
  pyexcel \
  pyexcel-io \
  pyexcel-webio \
  pyexcel-xls \
  pyexcel-xlsx \
  pytest \
  PyYAML \
  scikit-learn \
  scipy \
  uWSGI \
  xlrd \
  xlwt-future

useradd -M --shell /sbin/nologin www 