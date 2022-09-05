from setuptools import setup, find_packages


setup(
    name='MoneyAfterDark',
    version='1',
    license='NeuroscienceAfterDark',
    author="MoneyAfterDark",
    author_email='neuroscience@sigmund.science',
    packages=find_packages('MoneyAfterDark'),
    package_dir={'': 'MoneyAfterDark'},
    url='https://github.com/NeuroscienceAfterDark/MoneyAfterDark',
    keywords='Business, Finance and Universal Tax Tools. UK Specific Tax Tools also Included',
    install_requires=[
          'os',
          'pandas',
          'numpy',
      ],

)
