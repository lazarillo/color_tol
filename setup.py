from setuptools import setup

try:
    import pypandoc
    long_descr = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_descr = open('README.md').read()

setup(name='color_tol',
      version='0.1.1',
      description='Optimized color schemes for data display',
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
      test_suite='color_tol.tests',
      include_package_data=True,
      zip_safe=False)
