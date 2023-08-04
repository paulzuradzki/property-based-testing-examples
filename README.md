# `encoder`

# Description

A small package for [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding) (RLE) to demonstrate property-based testing and compare it with example-based unit tests.

Definition from Wikipedia
> Run-length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.

# Setup

```bash
# Clone the repository
$ git clone git@github.com:paulzuradzki/property-based-testing-examples.git

# (Mac/Linux) Activate virtual environment
$ source venv/bin/activate

# (Windows command prompt) Activate virtual environment
$ venv\Scripts\activate

# Install package and dependencies from source
(venv) $ python -m pip install .

# If you are editing the source code in src/, use -e / --editable flag
# (this creates a symlink between your site packages and local)
(venv) $ python -m pip install --editable .

# Run tests
(venv) pytest --verbose
```

# References

This example is described in the [Hypothesis Quick Start Guide](https://hypothesis.readthedocs.io/en/latest/quickstart.html).
