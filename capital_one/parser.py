
def inside_quote(line, target_char, quote_lst):
    """
    A helper function to check whether the target_char is surrounded
    by quotation mark in a given line.

    Precondition: char in line == True
    :param line: str
    :param target_char: str
    :return: bool
    """
    target_index = line.rfind(target_char)
    quote_ch = None  # None if it's currently parsed to non-string

    for index, ch in enumerate(line):
        if quote_ch and index == target_index:
            return True
        if ch in quote_lst:
            if not quote_ch:
                quote_ch = ch
            else:
                if ch == quote_ch:
                    quote_ch = None
    return False


class Parser:
    """A Parser that parse text files and count for different types of comments.

    This is an abstract class; subclasses are responsible for implementing
    parse().

    === Attributes ===
    content: list of string to be parsed
    single_count: count of single line comments
    todo_count: count of todos in comments
    block_count: count of block comments. See the definition of block count in
        docstring of subclasses
    block_line_count: count of block line comments
    total_cmt_count: total lines of comments, both single-line and block
    line_count: total number of lines in the file
    block_mode: True iff the line parsed is inside of a block comment
    have_parsed: True iff all contents have been parsed

    """
    def __init__(self, content):
        """
        Initialize an Parser with content to be parsed.

        :param content: list of string
        """
        self.content = content
        self.single_count = 0
        self.todo_count = 0
        self.block_count = 0
        self.block_line_count = 0
        self.total_cmt_count = 0
        self.line_count = len(content)
        self.block_mode = False
        self.have_parsed = False

    def parse(self):
        """
        Parse the content and update the counting attributes.

        :return: None
        """
        raise NotImplementedError

    def fetch_result(self):
        """
        Update the Parse object by calling parse() if it has not been parsed yet
        Otherwise, do nothing
        """
        if not self.have_parsed:
            self.parse()
            self.have_parsed = True

    def print_parsing_result(self):
        """
        Make sure the object is updated and then print the counting attributes

        :return: None
        """

        self.fetch_result()
        print("Total # of lines: ", self.line_count)
        print("Total # of comment lines: ", self.total_cmt_count)
        print("Total # of single line comments: ", self.single_count)
        print("Total # of comment lines within block comments: ", self.block_line_count)
        print("Total # of block line comments: ", self.block_count)
        print("Total # of TODO’s: ", self.todo_count)


class NonMultiLineParser(Parser):
    """
    A Parser for programming language that has no block comment syntax.

    A comment will be only considered as a block comment if it contains
    at least two consecutive lines that start with a comment symbol.
    """
    def __init__(self, content, single_cmt):
        Parser.__init__(self, content)
        self.single_cmt = single_cmt

    def parse(self):
        """
        Parse the content and update the counting attributes. Please refer to
        above docstring for the definition of block comments

        :return: None
        """

        self.total_cmt_count = 0
        curr_block_line_count = 0

        for line in self.content:

            if self.single_cmt in line and \
                    not inside_quote(line, self.single_cmt, ['"', "'"]):
                self.total_cmt_count += 1

                if 'TODO' in line:
                    self.todo_count += 1
                if line.startswith(self.single_cmt):  # equivalent to multi line start
                    self.block_mode = True
                    curr_block_line_count += 1
                    continue

            # end block_mode, clean up
            else:
                if self.block_mode:
                    if curr_block_line_count > 1:
                        self.block_count += 1
                        self.block_line_count += curr_block_line_count
                    self.block_mode = False
                    curr_block_line_count = 0

        self.single_count = self.total_cmt_count - self.block_line_count


class MultiLineParser(Parser):
    """
    A Parser for programming language that has block comment syntax.

    A comment will be considered as a block comment as long as it is surrounded
    by a pair of block comment symbol.
    """
    def __init__(self, content, single_cmt, multi_cmt_start, multi_cmt_end):
        Parser.__init__(self, content)
        self.single_cmt = single_cmt
        self.multi_cmt_start = multi_cmt_start
        self.multi_cmt_end = multi_cmt_end

    def parse(self):
        """
        Parse the content and update the counting attributes. Please refer to
        above docstring for the definition of block comments

        :return: None
        """
        for line in self.content:

            line_is_comment = False
            if self.multi_cmt_start in line and \
                    not inside_quote(line, self.multi_cmt_start, ['"', "'"]):
                self.block_mode = True
            if self.block_mode:
                self.block_line_count += 1
                line_is_comment = True
                if line.endswith(self.multi_cmt_end):
                    self.block_mode = False
                    self.block_count += 1

            elif self.single_cmt in line and \
                    not inside_quote(line, self.single_cmt, ['"', "'"]):
                self.single_count += 1
                line_is_comment = True
            if line_is_comment and 'TODO' in line:
                self.todo_count += 1

        self.total_cmt_count = self.single_count + self.block_line_count
