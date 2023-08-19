from setuptools import find_packages, setup

install_requires = [
    'requests==2.31.0',
]

dev_install_requires = [
    'flake8==6.1.0',
    'mypy==1.5.1',
]

if __name__ == 'main':
    setup(
        name='news_2030_macro',

        url='https://github.com/jaihuni/news_2030_macro',

        packages=find_packages(),
        python_requires='>=3.11, <3.12',

        install_requires=install_requires,
        extra_require={'dev': dev_install_requires},

        package_data={}
    )
