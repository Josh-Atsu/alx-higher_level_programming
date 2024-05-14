# PYTHON INPUT/OUTPUT

## Reading and Writing Files
open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)

>>> f = open('workfile', 'w', encoding="utf-8")
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see open()). Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you know that you need to use a different encoding. Appending a 'b' to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.

## The Encoding parameter
Did you notice the encoding parameter that got passed in to the open() function while you were opening a
file for writing? It’s important; don’t ever leave it out! As you saw in the beginning of this chapter, files don’t
contain strings, they contain bytes. Reading a “string” from a text file only works because you told Python
what encoding to use to read a stream of bytes and convert it to a string. Writing text to a file presents the
same problem in reverse. You can’t write characters to a file; characters are an abstraction. In order to
write to the file, Python needs to know how to convert your string into a sequence of bytes. The only way
to be sure it’s performing the correct conversion is to specify the encoding parameter when you open the
file for writing.
