[metadata]
name = QuantumDreamsAI
version = 0.1.0
author = Jemone McCubbin
author_email = xingxerx@email.com
description = A short description of QuantumDreamsAI
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/xingxerx/QuantumDreamsAI.git
license = MIT
license_file = LICENSE
classifiers =
    Programming Language :: Python :: 3
    Operating System :: OS Independent
    Topic :: Software Development :: Libraries :: Python Modules
    Typing :: Typed
[options]
package_dir =
    = src
packages = find:
where = src
[options.packages.find]
python_requires = >=3.7
install_requires =
    requests >= 2.20
    # Add more dependencies here
