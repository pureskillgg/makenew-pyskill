PureSkill.gg PySkill Skeleton
=============================

|PyPI| |GitHub Actions|

.. |PyPI| image:: https://img.shields.io/pypi/v/pureskillgg-makenew-pyskill.svg
   :target: https://pypi.python.org/pypi/pureskillgg-makenew-pyskill
   :alt: PyPI
.. |GitHub Actions| image:: https://github.com/pureskillgg/makenew-pyskill/workflows/main/badge.svg
   :target: https://github.com/pureskillgg/makenew-pyskill/actions
   :alt: GitHub Actions

Package skeleton for a PureSkill.gg PySkill.

Description
-----------

Bootstrap a new Python PureSkill.gg PySkill in less than a minute.

🎓 Start with the Tutorial!
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This repository is both a template for creating new a PySkill,
and fully functioning tutorial project.

⚡️💡⚡️ **If you are just getting started with PureSkill.gg data science, start here!**.

Follow these steps to start the tutorial.
On completing the tutorial, you will understand how to do data science
with PureSkill.gg data and be setup to download data from the public data set.
Once you complete the tutorial, you may use this repository to bootstrap you own project.

Requirements
^^^^^^^^^^^^

*Tested on Linux, macOS, and Windows.*

- `Python v3.9`_.
- `Poetry v1`_.
- Git_, `GitHub Desktop`_, or similar Git interface.

*An effort has been made to use dependencies that provide Python Wheels for most platforms.
This means you should not need to install extra compilers or packages.
However, if you get errors when running poetry install, you may need to
search for those errors and determine if additional packages must be installed
on your platform.*

.. _Git: https://git-scm.com/
.. _GitHub Desktop: https://desktop.github.com/
.. _Poetry v1: https://python-poetry.org/docs/
.. _Python v3.9: https://www.python.org/downloads/release/python-3913/

Setup
^^^^^

1. Clone this project locally using Git and enter the project working directory with

::

    $ git clone https://github.com/pureskillgg/makenew-pyskill.git
    $ cd pyskill

2. Confirm the correct Python (3.9.x) and Poetry (1.x.y) versions are installed with

::

    $ python --version
    Python 3.9.13
    $ poetry --version
    Poetry version 1.1.13

3. Install the dependencies with Poetry

::

    $ poetry install

4. Start the Jupyter notebook server

::

    $ poetry run jupyter notebook notebooks

5. Open the URL shown in the terminal,
   and navigate to http://localhost:8888/notebooks/tutorial/1%20-%20Setup.ipynb.

Features
~~~~~~~~

- Publishing to PyPI_.
- Secure dependency management with Poetry_.
- Linting with Pylint_.
- Uncompromising code formatting with Black_.
- pytest_ helps you write better programs.
- Code coverage reporting with Codecov_.
- Continuous testing and deployment with `GitHub Actions`_.
- `Keep a CHANGELOG`_.
- Consistent coding with EditorConfig_.
- Badges from Shields.io_.

.. _Black: https://black.readthedocs.io/en/stable/
.. _Codecov: https://codecov.io/
.. _EditorConfig: https://editorconfig.org/
.. _GitHub Actions: https://github.com/features/actions
.. _Keep a CHANGELOG: https://keepachangelog.com/
.. _PyPI: https://pypi.python.org/pypi
.. _Pylint: https://www.pylint.org/
.. _Shields.io: https://shields.io/
.. _pytest: https://docs.pytest.org/

Bootstrapping a New Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create an empty (**non-initialized**) repository on GitHub.
2. Clone the master branch of this repository with

   ::

       $ git clone --single-branch https://github.com/pureskillgg/makenew-pyskill.git new-pyskill
       $ cd new-pyskill

   Optionally, reset to the latest
   `release <https://github.com/pureskillgg/makenew-pyskill/releases>`__ with

   ::

       $ git reset --hard v1.2.0

3. Run

   ::

       $ ./makenew.sh

   This will replace the boilerplate, delete itself,
   remove the git remote, remove upstream tags,
   and stage changes for commit.

4. Create the required GitHub repository secrets
5. Review, commit, and push the changes to GitHub with

   ::

     $ git diff --cached
     $ git commit -m "Replace makenew boilerplate"
     $ git remote add origin git@github.com:<user>/<new-pyskill>.git
     $ git push -u origin master

6. Ensure the GitHub action passes,
   then publish the initial version of the package with

   ::

     $ poetry install
     $ poetry run bump2version patch
     $ git push
     $ git push --tags

Updating
~~~~~~~~

If you want to pull in future updates from this skeleton,
you can fetch and merge in changes from this repository.

Add this as a new remote with

::

    $ git remote rename origin upstream

and then configure your ``origin`` branch as normal.

Otherwise, add this as a new remote with

::

    $ git remote add upstream git@github.com:pureskillgg/makenew-pyskill.git

You can then fetch and merge changes with

::

    $ git fetch --no-tags upstream
    $ git merge upstream/master

Changelog
^^^^^^^^^

Note that ``CHANGELOG.md`` is just a template for this skeleton. The
actual changes for this project are documented in the commit history and
summarized under
`Releases <https://github.com/pureskillgg/makenew-pyskill/releases>`__.

Installation
------------

This package is registered on the `Python Package Index (PyPI)`_
as pureskillgg_makenew_pyskill_.

Install it with

::

    $ poetry add pureskillgg_makenew_pyskill

.. _pureskillgg_makenew_pyskill: https://pypi.python.org/pypi/pureskillgg-makenew-pyskill
.. _Python Package Index (PyPI): https://pypi.python.org/

Development and Testing
-----------------------

Quickstart
~~~~~~~~~~

::

    $ git clone https://github.com/pureskillgg/makenew-pyskill.git
    $ cd pyskill
    $ poetry install

Run each command below in a separate terminal window:

::

    $ make watch

Primary development tasks are defined in the `Makefile`.

Source Code
~~~~~~~~~~~

The `source code`_ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/pureskillgg/makenew-pyskill.git

.. _source code: https://github.com/pureskillgg/makenew-pyskill

Requirements
~~~~~~~~~~~~

You will need `Python 3`_ and Poetry_.

Install the development dependencies with

::

    $ poetry install

.. _Poetry: https://poetry.eustace.io/
.. _Python 3: https://www.python.org/

Tests
~~~~~

Lint code with

::

    $ make lint


Run tests with

::

    $ make test

Run tests on changes with

::

    $ make watch

Publishing
~~~~~~~~~~

Use the bump2version_ command to release a new version.
Push the created git tag which will trigger a GitHub action.

.. _bump2version: https://github.com/c4urself/bump2version

Publishing may be triggered using on the web
using a `workflow_dispatch on GitHub Actions`_.

.. _workflow_dispatch on GitHub Actions: https://github.com/pureskillgg/makenew-pyskill/actions?query=workflow%3Aversion

GitHub Actions
--------------

*GitHub Actions should already be configured: this section is for reference only.*

The following repository secrets must be set on GitHub Actions.

- ``PYPI_API_TOKEN``: API token for publishing on PyPI.

These must be set manually.

Secrets for Optional GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The version and format GitHub actions
require a user with write access to the repository
including access to read and write packages.
Set these additional secrets to enable the action:

- ``GH_USER``: The GitHub user's username.
- ``GH_TOKEN``: A personal access token for the user.
- ``GIT_USER_NAME``: The name to set for Git commits.
- ``GIT_USER_EMAIL``: The email to set for Git commits.
- ``GPG_PRIVATE_KEY``: The `GPG private key`_.
- ``GPG_PASSPHRASE``: The GPG key passphrase.

.. _GPG private key: https://github.com/marketplace/actions/import-gpg#prerequisites

Contributing
------------

Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://github.com/pureskillgg/makenew-pyskill/fork).
2. Create your feature branch (`git checkout -b my-new-feature`).
3. Make changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin my-new-feature`).
6. Create a new Pull Request.

License
-------

This Python package is licensed under the MIT license.

Warranty
--------

This software is provided by the copyright holders and contributors "as is" and
any express or implied warranties, including, but not limited to, the implied
warranties of merchantability and fitness for a particular purpose are
disclaimed. In no event shall the copyright holder or contributors be liable for
any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services;
loss of use, data, or profits; or business interruption) however caused and on
any theory of liability, whether in contract, strict liability, or tort
(including negligence or otherwise) arising in any way out of the use of this
software, even if advised of the possibility of such damage.
