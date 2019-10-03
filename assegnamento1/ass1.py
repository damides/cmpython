import argparse
import logging
import os
import matplotlib.pyplot as plt
from collections import defaultdict
import string
from datetime import datetime


# Some intial setup
# logging.basicConfig(level=logging.DEBUG)


def skiprows(file_pointer, line_number):
    '''
    Skip the specified lines by reading them
    and doing basically nothing
    '''
    for i in range(line_number):
        file_pointer.readline()


def char_count(args):
    # Sanity checks
    assert os.path.exists(args.file_path), "Invalid Path"
    assert args.file_path.endswith('.txt'), "Input file is not a .txt"

    # Initialize dictionary with default value 0
    freq_table = defaultdict(lambda: 0)

    with open(args.file_path, 'r') as f:
        if(args.preamble > 0):
            skiprows(f, args.preamble)
            logging.debug('Skipping the\
                           first {} lines'.format(args.preamble))

        total_lines = 0
        total_words = 0
        # Poulate dictionary
        for line in f:
            line = line.lower()
            for ch in string.ascii_lowercase:
                freq_table[ch] += line.count(ch)
            total_lines += 1
            total_words += len(line.split())

    logging.debug('Populated dictionary {}'.format(freq_table))

    # Normalize entry
    total_letters = sum(freq_table.values())
    for key in freq_table:
        freq_table[key] = freq_table[key] / total_letters

    # Setting up the bar plot
    if args.bar:
        fig, ax = plt.subplots()
        ax.bar(freq_table.keys(), freq_table.values())
        ax.set_title('Frequency occurencies of letters in file')
        ax.set_ylabel('Frequency %')
        plt.tight_layout()
        plt.show()

    # Print the output
    print('++++ Frequency Table ++++')
    for ch, value in freq_table.items():
        print('{}: {:.3f}%'.format(ch, value * 100.))
    print('Elapsed time {}'.format(datetime.now()-startTime))
    if(args.verbose):
        print('Total number of characters = {}'.format(total_letters))
        print('Total number of words = {}'.format(total_words))
        print('Total number of lines = {}'.format(total_lines))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Script that goes through all
                                     the letters of a given file and prints out
                                     the relative frequencies of their
                                     occurencies.""")
    parser.add_argument('file_path',
                        help='path of the file including the .txt extension')
    parser.add_argument('-b', '--bar', action='store_true',
                        help='show bar plot of the relative frequencies')
    parser.add_argument('-p', '--preamble', type=int, metavar='N',
                        default=0, help='number of initial line to skip')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='display extra stats about the book')
    args = parser.parse_args()

    logging.debug('Argument stored {}'.format(args))

    # Start main routine
    startTime = datetime.now()
    char_count(args)
