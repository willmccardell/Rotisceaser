#!/bin/bash
pip install --use-feature-in-tree-build --editable .[test]

echo "Linting..."
flake8 --max-line-length=88 tests rotisceaser

echo "Testing..."
pytest