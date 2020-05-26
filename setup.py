from setuptools import setup

setup(
        name='spotifycli',
        version='0.1.0',
        author='Josh Thomas',
        author_email='joshrthomas@protonmail.com',
        description='spotify command line client',
        url='https://github.com/jerte/spotifycli/',
        packages=['spotifycli', ],
        install_requires=['spotipy'],
        entry_points = {
            'console_scripts': [
                'spotifycli = spotifycli.__main__:main'
                ]
        })
