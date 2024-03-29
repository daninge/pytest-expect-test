==================
pytest-expect-test
==================

.. image:: https://img.shields.io/pypi/v/pytest-expect-test.svg
    :target: https://pypi.org/project/pytest-expect-test
    :alt: PyPI version


.. image:: https://img.shields.io/pypi/pyversions/pytest-expect-test.svg
    :target: https://pypi.org/project/pytest-expect-test
    :alt: Python versions


.. image:: https://ci.appveyor.com/api/projects/status/89vkts8il49rdh90/branch/main?svg=true
    :target: https://ci.appveyor.com/project/daninge98/pytest-expect-test-qfsuo/branch/main
    :alt: See Build Status on AppVeyor

A fixture to support expect tests (golden tests) in pytest

This code was mostly copied from `ezyang/expecttest <https://github.com/ezyang/expecttest>`_ who wrote an implementation for unittest.

Installation
------------

You can install "pytest-expect-test" via `pip`_ from `PyPI`_::

    $ pip install pytest-expect-test


Usage
-----

Start by writing your test, printing out any interesting output, and then calling expect with an empty string

.. code-block:: python
            
    # Function we are testing
    def cumulative_sum(nums):
        cum_sum = 0
        result = []
        for num in nums:
            result.append(num+cum_sum)
            cum_sum += num
        return result


    def test_cumulative_sum(expect):
        print(cumulative_sum([2, 3, 5]))
        expect("""""")
        print(cumulative_sum([1, 5, 9]))
        expect("""""")
        
Then run::

    $ pytest

Note that the test fails because we expected nothing to be printed (e.g. we passed an empty string to the expect function), but there was some text that was printed.

We can automatically fix these tests by running::

    $ EXPECTTEST_ACCEPT=1 pytest

Our test will then be updated automatically so that it passes:

.. code-block:: python

    def test_cumulative_sum(expect):
        print(cumulative_sum([2, 3, 5]))
        expect("""\
    [2, 5, 10]
    """)
        print(cumulative_sum([1, 5, 9]))
        expect("""\
    [1, 6, 15]
    """)

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-expect-test" is free and open source software


This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/daninge98/pytest-expect-test/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
