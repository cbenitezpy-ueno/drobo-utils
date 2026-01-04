# Drobo Utils Copyright (C) 2008,2009  Peter Silva (Peter.A.Silva@gmail.com)
# Drobo Utils comes with ABSOLUTELY NO WARRANTY; For details type see the file
# named COPYING in the root of the source directory tree.

import warnings
warnings.warn(
    "setup.py is deprecated. Please use 'pip install .' with pyproject.toml instead.",
    DeprecationWarning,
    stacklevel=2
)

from distutils.core import setup

setup(name='Drobo-utils',
      version='9999',
      description='Drobo Management Protocol io package',
      py_modules=['Drobo', 'DroboGUI', 'DroboIOctl', 'drobom'],
      entry_points={
          'console_scripts': [
              'drobom=drobom:main',
              'droboview=drobom:view_main',
          ],
      })
