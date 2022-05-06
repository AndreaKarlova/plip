from setuptools import setup, find_packages

setup(name='plip',
      version=1.0.0,
      description='fully automated protein-ligand interaction profiler',
      packages=find_packages(),
      install_requires=[
          'openbabel',
          'numpy',
          'lxml']
      )
