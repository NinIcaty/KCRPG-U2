DIR="kcrpg"
URL="https://github.com/NinIcaty/KCRPG-U2"
INP="D"
PKG=("colorama" )
if command -v python3 >/dev/null 2>&1; then
    if [ -d "$DIR" ]; then
        echo "Please delete or rename the Directory $DIR"

        exit 1
        #broken:(
        : 
    else
        echo 'Starting install'
        git clone $URL $DIR
        echo 'Cloned repo'
        cd $DIR
        python -m venv .venv
        echo 'Venv Created'
        source .venv/bin/activate
        echo 'Activated'

    fi
else
    echo "Python 3 is not installed,Please install it."
fi
#In the venv
python --version
echo "Packages that will be installed are:"
for i in ${!myArray[@]}; do
  echo "${myArray[$i]}"
done
echo Installing packages
pip install $PKG
echo "Packages that have been succesfully innstalled are:"
pip list
echo 'To re-activate the venv run the command "source .venv/bin/activate" in the Directory' $DIR
