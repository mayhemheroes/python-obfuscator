#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=["python_obfuscator"]):
    import python_obfuscator

obfuscator = python_obfuscator.obfuscator()
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    obfuscator.obfuscate(fdp.ConsumeRemainingString())

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
