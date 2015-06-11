from setuptools import setup


setup(
    name='wa',
    version='0.1',
    scripts=['bin/wa'],
    url='https://github.com/saironiq/wa',
    license='GPLv2',
    author='Sairon Istyar',
    author_email='saironiq@gmail.com',
    description='WolframAlpha API console client',
    requires=['requests', 'beautifulsoup4', 'colorama'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
    ],
)
