"""Combine multiple word count CSV-files into a single cumulative count."""

import sys
import csv
import argparse
from collections import Counter


def collection_to_csv(collection, num=None):
    """Write collection of items and counts in csv format."""
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])


def update_counts(reader, word_counts):
    """Update word counts with data from another reader/file."""
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)


def main(args):
    """Run the command line program."""
    word_counts = Counter()
    for fname in args.infiles:
        with open(fname, 'r') as reader:
            update_counts(reader, word_counts)
    collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infiles', type=str, nargs='*',
                        help='Input file names')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output n most frequent words')
    args = parser.parse_args()
    main(args)
    