#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=["python_obfuscator"],
                                exclude=["python_obfuscator.helpers.variable_name_generator",
                                "python_obfuscator.helpers.random_datatype"]):
    import python_obfuscator

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    obfuscator = python_obfuscator.obfuscator()
    obfuscator.obfuscate(fdp.ConsumeRemainingString())

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
