#!/bin/bash


PS1=$
PROMPT_COMMAND=
echo -en "\033]0;Web Server Module\a"

echo "setting env vars"
source /home/nicky/.cache/pypoetry/virtualenvs/secuserve-webinterface-module-CXYlx8Dq-py3.8/bin/activate 
poetry run python3 Secuserve-WebInterface-module/__main__.py