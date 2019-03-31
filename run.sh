if [ "$1" = "" ]
then
    echo "Please put python files that you want to analyze in the /please_put_test_python_file_here folder"
    echo "Please give a python file name that you want to analyze as argument 1"
    echo "try to run:"
    echo "./run.sh analyze_this_python_file.py"
else
    pip3 install .
    cd bin
    python3 pylint ../please_put_test_python_file_here/$1
fi

