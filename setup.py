from setuptools import setup

setup(
    name='logmerge',
    version='1.0',
    author='Julius Chuang',
    py_modules=['logmerge'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        logmerge=logmerge:cli
    ''',
)