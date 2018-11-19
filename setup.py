from __future__ import print_function
from setuptools import setup
import os
import shutil

here = os.path.abspath(os.path.dirname(__file__))

# make the faiss python package dir
shutil.rmtree("faiss", ignore_errors=True)
os.mkdir("faiss")
shutil.copyfile("faiss.py", "faiss/__init__.py")
shutil.copyfile("swigfaiss.py", "faiss/swigfaiss.py")
shutil.copyfile("_swigfaiss.so", "faiss/_swigfaiss.so")

long_description="""
*Unofficial prebuilt binary*

The repo that builds this project can be found here: https://github.com/onfido/faiss_prebuilt

Original readme:

Faiss is a library for efficient similarity search and clustering of dense 
vectors. It contains algorithms that search in sets of vectors of any size,
 up to ones that possibly do not fit in RAM. It also contains supporting 
code for evaluation and parameter tuning. Faiss is written in C++ with 
complete wrappers for Python/numpy. Some of the most useful algorithms 
are implemented on the GPU. It is developed by Facebook AI Research.
"""
setup(
    name='faiss_prebuilt',
    version='0.1.3.1',
    description='A library for efficient similarity search and clustering of dense vectors',
    long_description=long_description,
    url='https://github.com/facebookresearch/faiss',
    author='Matthijs Douze, Jeff Johnson, Herve Jegou',
    author_email='matthijs@fb.com',
    license='BSD',
    keywords='search nearest neighbors',
    install_requires=['numpy'],
    packages=['faiss'],
    package_data={
        'faiss': ['*.so'],
    },
    classifiers=[
     'Programming Language :: Python :: 2.7',
     'Programming Language :: Python :: 3.6',
     'Programming Language :: Python :: 3.7'
    ]
)
