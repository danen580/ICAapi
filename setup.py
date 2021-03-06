from distutils.core import setup
setup(
  name = 'icaapi',         # How you named your package folder (MyLib)
  packages = ['icaapi'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python Wrapper for ICA shopping list API',   # Give a short description about your library
  author = 'Daniel Engberg',                   # Type in your name
  author_email = 'engberg.daniel@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/danen580/ICAapi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/danen580/ICAapi/archive/v0.2.tar.gz',    # I explain this later on
  keywords = ['ICA', 'Shoppinglist'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)