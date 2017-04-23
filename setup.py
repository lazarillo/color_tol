from setuptools import setup

try:
    import pypandoc
    long_descr = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_descr = open('README.md').read()

setup(
    name='blah',
    version=find_version('blah.py'),
    description='Short description',
    long_description=long_description,
)


=============================================




setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      long_description=long_descr,
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Visualization',
      ],
      keywords='visualization seaborn matplotib',
      url='https://github.com/lazarillo/color_tol',
      author='Mike Williamson',
      author_email='mwilliamson@pacific.edu',
      license='MIT',
      packages=['color_tol'],
      install_requires=[
          'os',
          'json'
      ],
      test_suite='color_tol.tests',
      include_package_data=True,

      zip_safe=False)



