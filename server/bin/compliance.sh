#!/bin/bash

######################################################################
# Author: Ishwarachandra Gowtham                                     #
# E-mail: ic.gowtham@gmail.com                                       #
######################################################################

echo "-----------------------------------------------"
echo "Starting pycodestyle(PEP8) compliance check ..."
echo "-----------------------------------------------"
pycodestyle -v \
     --format=pylint \
     --ignore=F405,E126,E501,E731 \
     --max-line-length=120 "$*"
echo "---------------------------------------------"
echo "Completed pycodestyle(PEP8) compliance check."
echo "---------------------------------------------"

echo "------------------------------------"
echo "Starting FLAKE8 compliance check ..."
echo "------------------------------------"
flake8 --format=pylint \
       --ignore=F405,E126,E501,E731 \
       --max-line-length=120 "$*"
echo "----------------------------------"
echo "Completed FLAKE8 compliance check."
echo "----------------------------------"

echo "------------------------------------"
echo "Starting pylint compliance check ..."
echo "------------------------------------"
pylint --disable=C0325,W1202,unused-argument,no-self-use,too-many-arguments \
       --max-line-length=120 "$*"
echo "----------------------------------"
echo "Completed pylint compliance check."
echo "----------------------------------"

echo "----------------------------------------"
echo "Starting PEP257 doc compliance check ..."
echo "----------------------------------------"
pep257 -esv "$*"
echo "--------------------------------------"
echo "Completed PEP257 doc compliance check."
echo "--------------------------------------"

echo "---------------------------------------------------------"
echo "Starting Radon cyclomatic complexity compliance check ..."
echo "---------------------------------------------------------"
radon cc -a -s "$*"
echo "-------------------------------------------------------"
echo "Completed Radon cyclomatic complexity compliance check."
echo "-------------------------------------------------------"
