We have 2 runtime errors caught by mypy:
    1. The third conductor is missing the U argument
    2. The join function requires strings, but the arguments are given as floats

There are a few lint warnings by ruff:
    1. There are multiple imports in a single line
    2. Some of the imports are not used
    3. The Conductor class is defined in a single line
    4. The individual Conductors are all defined in a single line
    5. The main function execution is in a single line