from setuptools import setup, find_packages

setup(
    name='temp-converter',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    description='Basic package for converting temperature units from fahrenheit to kelvin.',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/kjgpta/temp-converter',
    author='kjgpta',
    author_email='myemail@example.com'
)