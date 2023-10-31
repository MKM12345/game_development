from setuptools import setup, find_packages

setup_args = dict(
    name='game_development',
    version='1.0.6',
    description='Simplify 2D and 3D game development and combine the power of Panda3D and Pygame to create awesome games.',
    long_description_content_type='text/markdown',
    long_description="""
    <div align="center">
      <img src="https://github.com/MKM12345/game_development/raw/main/logo.png">
    </div>
    <a style="display:inline;" href="#"><img src="https://img.shields.io/badge/Python- >= 2.7 -blue?style=plastic.svg" alt="python versions" /></a>
    <a style="display:inline;" href="#"><img src="https://img.shields.io/badge/pypi package- 1.0.6 -4DC71F?style=plastic.svg" alt="pypi version" /></a>
    <a style="display:inline;" href="#"><img src="https://img.shields.io/badge/first timer-friendly-4DC71F?style=plastic.svg" alt="first timer friendly" /></a>
    <a style="display:inline;" href="https://github.com/MKM12345/game_development/labels/game_development-idea"><img src="https://img.shields.io/github/issues-raw/MKM12345/game_development/game_development-idea?color=4DC71F&label=game_development%20ideas" alt "game_development ideas" /></a>
    <a style="display:inline;" href="#"><img src="https://img.shields.io/badge/tests- all passing -4DC71F?style=plastic.svg" alt="game_development ideas" /></a>
    
    <h1>game_development v1.0.6</h1>
    A game development library for Python with <em>a lot</em> of assorted functions to simplify both 2D and 3D game development tasks in Pygame and Panda3D while combining their power to create awesome games.
    
    ### GitHub Page: https://github.com/MKM12345/game_development
    
    ## How to install
    Install with pip in your terminal, making sure Python is added to PATH:
    $ pip install game_development
    
    Alternatively, you can use the git URL to do the same.
    $ pip install "git+https://github.com/MKM12345/game_development.git@pip-install#egg=game_development"
    
    ### What can it do?
    As an open-source library, it offers a wide range of simple functions to make writing game code in both Pygame and Panda3D easier and quicker. A complete list of all game_development functions that are available can be found here.
    
    ### Support game_development
    game_development is full of contributions from the community! We're beginner-friendly here, so read the contributing guidelines and give us your best game_development functions 😃!
    
    ### View the site
    Recently, game_development's website launched at https://MKM12345.github.io/game_development-the-site/, feel free to report bugs or give feature requests, using the web-issue label. Or, take a look at the discussion.
    
    ### License
    game_development is licensed under the MIT LICENSE.
    """,
    license='MIT',
    packages=find_packages(),
    author='MKM12345',
    author_email='arekhon.shadow@gmail.com',
    keywords=['game development', 'pygame', 'panda3d'],
    url='https://github.com/MKM12345/game_development',
    download_url='https://pypi.org/project/game_development/',
)

install_requires = [
    'pygame',
    'panda3d'
    # Add other dependencies here
]

setup(**setup_args, install_requires=install_requires)
