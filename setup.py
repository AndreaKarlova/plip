from setuptools import setup, find_packages

from plip.basic import config

setup(name='plip',
      version=config.__version__,
      description='fully automated protein-ligand interaction profiler',
      packages=find_packages(),
#      scripts=['plip/plipcmd.py'],
      install_requires=[
          'openbabel',
          'numpy',
          'lxml']
      )
