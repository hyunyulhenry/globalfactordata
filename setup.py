from setuptools import setup, find_packages

setup(
    name='globalfactordata',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    include_package_data=True,
    package_data={
        'globalfactordata': ['data/*.pkl', 'data/*.xlsx', 'data/*.csv']
    },
    author='Henry Lee',
    description='JKP 글로벌 팩터 데이터를 쉽게 불러올 수 있는 도구',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hyunyulhenry/globalfactordata',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)