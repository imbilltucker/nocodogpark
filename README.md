# README

This is a hello world example python program to show [uv](https://docs.astral.sh/uv/concepts/tools/) tool for running a
project and making an executable using [pyinstaller](https://pyinstaller.org/en/stable/)


## Run the program to make the html map

`uv run noco-dog-parks`


## Create an executable that can be distributed to make this map
` uv run pyinstaller --onefile --paths=src src/noco_dog_parks/__init__.py --name
noco_dog`
