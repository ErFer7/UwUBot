# -*- codsing: utf-8 -*-

'''
Limpa os arquivos de cache do projeto.
'''

import os
import shutil

os.chdir('../')

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if name == '__pycache__':
            shutil.rmtree(os.path.join(root, name))

for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        if name == '.pytest_cache':
            shutil.rmtree(os.path.join(root, name))

os.chdir('./scripts')
