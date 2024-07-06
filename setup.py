from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# 配置
setup(
    # 名称必须匹配文件名 'verysimplemodule'
    name="pypoitools",
    version=VERSION,
    author="AlpaCa",
    author_email="<hf2604307870@outlook.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy','geopandas','pyrosm','matplotlib'],  # add any additional packages that
    # 需要和你的包一起安装，例如：'caer'

    keywords=['python', 'poi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)