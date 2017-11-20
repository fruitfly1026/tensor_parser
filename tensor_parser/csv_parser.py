
from sys import exit, stderr
import csv
import gzip
import bz2


#
# Utilities
#

def open_file(fname, mode):
  '''
    A wrapper around `open()` which also supports gzip and bz2.

    `mode` should either be 'r' or 'w'. A 't' will be appended when reading
    from a compressed file.
  '''
  if fname.endswith('.gz'):
    return gzip.open(fname, mode + 't')
  elif fname.endswith('.bz2'):
    return bz2.open(fname, mode + 't')
  else:
    return open(fname, mode)



def get_file_sample(fname, max_lines=100):
  '''
    Return up to the first `max_lines` of file `fname`. This is useful for CSV
    sniffing.
  '''
  sample = ''
  nlines = 0
  # gather sample for sniffer
  with open_file(fname, 'r') as f:
    for line in f:
      sample += line
      nlines += 1
      if nlines == max_lines:
        break
  return sample


#
# The good stuff.
#

class csv_parser:
  '''
    A class representing a CSV file which is a thin wrapper above the python
    CSV library.
  '''

  def __init__(self, fname, delim=None, has_header=None):
    self._fname = fname

    # Sniff the file to get a dialect, which stores metadata such as delimiter.
    try:
      self._dialect = csv.Sniffer().sniff(get_file_sample(fname))
    except csv.Error as e:
      print('ERROR {}: {}'.format(fname, e))
      exit(1)

    # override delimiter if requested
    if delim is not None:
      if self._dialect.delimiter != delim:
        print('Overriding delimiter "{}" with "{}"'.format(
            self._dialect.delimiter, delim))
      self._dialect.delimiter = delim

    # Parse the header of a CSV file. If no header is present, this will use
    # a 1-indexed list (e.g., [1, 2, 3, ...]).
    #
    # `has_header` is just a hint/override. If not supplied, the CSV lib's best
    # guess will be used.
    if has_header is None:
      has_header = csv.Sniffer().has_header(get_file_sample(fname))

    with open_file(self._fname, 'r') as f:
      line = next(csv.reader(f, self._dialect))
      if has_header:
        self._header = line
      else:
        self._header = [x+1 for x in range(len(line))]
    self._file_has_header = has_header

  def rows(self):
    '''
      Yield rows of the CSV file in dictionary form. Keys are taken from
      `_header` and values are those found in the file.
    '''
    print('Parsing {}...'.format(self._fname), file=stderr)
    print('  delim: {}'.format(self.delim()), file=stderr)
    print('  header: [{}]'.format(', '.join(self.header())), file=stderr)

    with open_file(self._fname, 'r') as f:
      reader = csv.reader(f, self._dialect)
      try:
        # skip header if file includes it
        if self._file_has_header:
          next(reader)

        # grab each line
        for line in reader:
          yield line

      # bad news
      except csv.Error as e:
        exit('ERROR {} line {}: {}'.format(self._fname, reader.line_num, e))

  def delim(self):
    return self._dialect.delimiter

  def header(self):
    return self._header

  def num_columns(self):
    return len(self._header)

