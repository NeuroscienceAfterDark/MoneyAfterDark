from distutils.core import setup
setup(
name = 'MoneyAfterDark',
packages = 'MoneyAfterDark',
version = '1.0.6',
license = 'MIT',
author = 'NeuroscienceAfterDark',
author_email = 'neuroscience@sigmund.science',
description = 'Business, Finance and Universal Tax Tools. UK Specific Tax Tools also Included',
url = 'https://github.com/NeuroscienceAfterDark/MoneyAfterDark',
download_url = 'https://github.com/NeuroscienceAfterDark/MoneyAfterDark/archive/refs/tags/1.0.6.tar.gz',
install_requires=['os'
                  'pandas',
                  'numpy',],
classifiers = ['Programming Language :: Python :: 3',
               'License :: OSI Approved :: MIT License',
               'Operating System :: OS Independent',
               ],
)
