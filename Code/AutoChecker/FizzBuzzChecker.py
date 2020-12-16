#  Copyright (c) 2020. Peter Bethell (moodelymoo)
from Code.Examples import FizzBuzz as Example
from Code.YourImpSpace import FizzBuzz as YourCode


def testFizzBuzzOutput():
    import sys
    from io import StringIO

    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        Example.fizzBuzzVerbose()
        output = out.getvalue().strip()

        out2 = StringIO()
        sys.stdout = out2
        # insert method call to check prints of here
        YourCode.main()
        # ####
        output2 = out2.getvalue().strip()

        assert output == output2, "did not match expected FizzBuzz pattern," \
                                  "\nExpected:\n" + output.__str__() + "\nReceived:\n" + output2.__str__()
    finally:
        sys.stdout = saved_stdout


if __name__ == "__main__":
    testFizzBuzzOutput()
    print("Everything passed, well done")
