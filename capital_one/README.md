
### Introduction
This is a take-home coding assessment for the PEY software engineer position at CapitalOne.

It is a command line program that counts different types of comments in the input textfile.

Currently, it supports the following file extension:
".py", ".sh", ".bash", ".java",".js", ".c", ".cpp",".swift", ".sql",".rb"


### Assumptions
1. The input file must be compiled program. Or, at least, the string " " and multi-line comment symbol(if applicable) must be closed properly.
2. My definition of "block comments":

    2.1 language with no multi-line syntax: A comment will be only considered as a block comment if it contains at least two consecutive lines that start with a comment symbol.
    
    2.2 language with multi-line syntax: A comment will be considered as a block comment as long as it is surrounded
    by a pair of block comment symbol.


### Design choices

Due to time constrains, I haven't get a chance to implement all languages with different comment patterns. However, I put many thoughts on the program design so it can be easily extended.

For example, if you want to add language that has no single line comment syntax (eg. HTML), you only need to add a class that override the `parse()` function and modify the factory function a bit in `main.py`

**Design Pattern** used: Polymorphism, Inheritance, Factory

**Why command-line program**? : I thought about use cases. Normally when people push code, we can use git to find out which files are modified/created. Therefore we can take these file names as standard input and easily piped into this command-line program.


### Files
There are three files for this program Please see detailed explanations in the docstring.

1. `main.py` -> main program
2. `parser.py` -> contains a abstract class `Parser` and two child classes `NonMultiLineParser` and `MultiLineParser`
3. `support_extension.py` -> a single variable for all currently supported file extensions. It features some common programming languages and you can extend it very simply.


### Installation Prerequisite
The only requirement for this program is python3. To install, please visit the official website https://www.python.org/downloads/


### Usage
Download the the entire repository, then use command line to `cd` to the folder. Then you can run it on multiple file by using:
```
python3 main.py <filepath1> <filepath2>  <filepath3>
```
The `filepath` can be either relative or absolute. Don't forget to add a space between two `filepaths`!

### Test Cases
I've tested my program with the following cases.
* 3 example files provided in the pdf (saved in the `test` folder)
* file that doesn't exist/ permission denied/ a folder
* file with an unsupported extension
* edge cases file with comment_symbol inside/ourside of a string. (saved in the `test` folder)




