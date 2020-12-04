from setuptools import setup, find_packages
from numpy.distutils.core import setup
from os import path
import io

## instructions for upload to pypi

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

if __name__ == "__main__":
    setup(name = 'h5anchor',
          author            = "Rohan Byrne",
          author_email      = "rohan.byrne@gmail.com",
          url               = "https://github.com/rsbyrne/h5anchor",
          version           = "0.9",
          description       = "A set of Python tools for managing h5 files.",
          long_description  = long_description,
          long_description_content_type='text/markdown',
          packages          = ['h5anchor'],
          install_requires  = ['h5py','numpy'],
          setup_requires    = [''],

          
          
          classifiers       = ['Programming Language :: Python :: 3',
                               'Programming Language :: Python :: 3.3',
                               'Programming Language :: Python :: 3.4',
                               'Programming Language :: Python :: 3.5',
                               'Programming Language :: Python :: 3.6',
                               'Programming Language :: Python :: 3.7',
                               'Programming Language :: Python :: 3.8',]
          )
