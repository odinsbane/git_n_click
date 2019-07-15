from setuptools import setup

setup(name='git_n_click',
      version='0.1.0',
      packages=['example_pkg'],
      install_requires=["click"],
      entry_points={
          'console_scripts': [
              "click_example = click_example:main",
              "pkg_example = example_pkg.pkg_example:main"
          ]
      },
      )
