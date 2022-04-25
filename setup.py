from setuptools import setup, find_packages

install_requirements=[
    'mysqlclient',
    'sqlalchemy',
    'sqlalchemy_utils',
]

setup(
    name='scielo-usage-counter-schema',
    version='0.5.1',
    description='The SciELO Usage Counter Schema',
    author='SciELO',
    author_email='scielo-dev@googlegroups.com',
    license='BSD',
    install_requires=install_requirements,
    url='https://github.com/rafaelpezzuto/scielo_usage_counter_schema',
    keywords='database schema, project counter r5, sushi',
    maintainer_email='rafael.pezzuto@gmail.com',
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        init-db=init_db:main
    """
)
