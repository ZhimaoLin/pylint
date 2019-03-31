GREEN="\033[1;32m"
NOCOLOR="\033[0m"

# Install Pylint
pip3 install .
cd bin

echo -e "${GREEN}===================================================${NOCOLOR}"

if [ "$1" = "" ]
then
    for file in "../please_put_test_python_file_here"/*
    do
        python3 pylint $file
    done
else
    python3 pylint ../please_put_test_python_file_here/$1
fi

