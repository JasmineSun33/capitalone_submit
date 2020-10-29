import sys
import ntpath
from parser import NonMultiLineParser, MultiLineParser
from support_extension import SUPPORT_EXTENSION


def get_parser_spec(filename):
    """
    Return the parser specification list based on the filename extension.

    Raise ValueError if the file extension is not available
    :param filename: string
    :return: list
    """

    # find the highest index of the '.' in filename
    dot_index = filename.index('.')
    extension = filename[dot_index:]
    if dot_index == -1 or extension not in SUPPORT_EXTENSION:
        raise ValueError
    else:
        return SUPPORT_EXTENSION[extension]


def parser_factory(content, single_cmt, multi_cmt_start, multi_cmt_end):
    """
    Return the corresponding child class of Parser, based on whether or not
    these two parameters, multi_cmt_start and multi_cmt_end, are provided.

    :param content: list of str
    :param single_cmt: str
    :param multi_cmt_start: str
    :param multi_cmt_end: str
    :return: Parser
    """
    if multi_cmt_start is None and multi_cmt_end is None:
        return NonMultiLineParser(content, single_cmt)
    else:
        return MultiLineParser(content, single_cmt, multi_cmt_start, multi_cmt_end)


def parse_handler(filepath,filename):
    """
    Open and clean the text file into a list of string. Then feed the data into
    appropriate Parser and print the parsing result.

    :param filepath: str
    :param filename: str
    :return: None
    """
    f = open(filepath, "r")
    content = f.read().split("\n")
    f.close()

    # remove leading and trailing spaces
    for i in range(len(content)):
        content[i] = content[i].strip()

    single_cmt, multi_cmt_start, multi_cmt_end = get_parser_spec(filename)
    parser = parser_factory(content, single_cmt, multi_cmt_start, multi_cmt_end)
    parser.print_parsing_result()


def run(filepath_list):
    """
    The main function of the program. Take a list of file path from standard
    input and pass them into the parse_handler.
    FileNotFoundError, OSError, and ValueError will be handled with appropriate
    print message.
    File name started with '.' will be ignored.

    :param filepath_list: list of str
    :return: None
    """
    for fp in filepath_list:
        # get filename from file path
        filename = ntpath.basename(fp)
        if filename[0] == ".":
            continue

        print("==============", filename, "==============")
        try:
            parse_handler(fp, filename)
        except FileNotFoundError:
            print("This file does not exist.")
        except OSError:
            print("This file can not be opened.")
        except ValueError:
            print("This file type is not currently supported.")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: "+sys.argv[0]+" file1, file2...", file=sys.stderr)
    else:
        run(sys.argv[1:])


