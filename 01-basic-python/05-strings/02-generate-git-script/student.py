#!/usr/bin/python3

from textwrap import dedent

def generate_git_script(id):
    string = f"if [ ! -d {id} ]; then\n    git clone https://github.com/{id}/project {id}\nelse\n    (cd {id}; git pull)\nfi" 

    return dedent(string).strip()