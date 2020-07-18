import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--input',
    dest='input',
    required=True,
    help='THis is input argument'
)

parser.add_argument(
    '--output',
    dest='output',
    required=True,
    help = 'This is output argument'
)