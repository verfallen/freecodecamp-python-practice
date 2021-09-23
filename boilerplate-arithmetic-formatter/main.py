# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
                           '888 + 40', '653 + 87']))

# Run unit tests automatically
main()
