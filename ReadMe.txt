Labview Wrapper Vis for libplctag. (https://github.com/kyle-github/libplctag)

Included are vis for all of the SDK functions and a very simple example (SimpleReadWrite.vi) that reads a single float type tag from a logix PLC, writes a new value, then reads it again.
These vi's should work on Labview 2019 for Linux 64 bit, Windows 64 bit, and Windows 32 bit.  If you need an earlier version let me know.

This should allow you to use labview to read and write tag values directly to plcs, avoiding the use of OPC which in labview limits you to windows 32 bit only, and requires the use of rslinx.

Make sure the .dll or .so files are in the same directory as your wrapper vi's.  If you need to change the location, edit the Choose_Lib.vi.



