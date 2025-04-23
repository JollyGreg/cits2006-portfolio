# UWA Programming Competition Society - Cybersecurity Workshop

## The Cuckoos Egg - Mark

The Cuckoos Egg - Book rec and breakdown

tearle.com/cuckoo

## OSINT Training for CTFs - Lindsay Coudert

Open Source Intelligence = OSINT

Common methods for CTF:

- Social Media
- Reverse Image Lookups: basic but useful
- Map co-ordinates

exiftool - metadata reading

[flightera.net](http://flightera.net) - flight tracking

Workshop:

Moss Vale: -34.547868919614956, 150.37147096990032

Extra:

inteltechniques.com

osintframework.com

geohunt.vercel.app

Missing Persons Hackathon:

https://www.tracelabs.org/get-involved

## Reverse Binary Engineering - Jeremy

EIF File TOols

readelf - display information

nm - list symbols

ldd

patchelf - modify

### Techniques

static analysis 

- no execution
- Speculation
- Usually transform a program into a text file

### Static analysis Tools

Text: Vim, VSC

Decompiler: Ghidra

Disassembler: Objdump

Constraint solver: Z3, Angr

### Dynamic

If flag is in memory you can just read it with a debugger

Debugging: GDB, LLDB, Angr, Strace

Flags:

1. flag{wow_reading_the_source_code_is_easy_3736424}
2. flag{xor_is_the_inverse_of_xor_323723}
3. flag{dynamic_xor_keys_are_real}
4. 
5. flag{no_source_code_for_you_26433}

## Cryptography -

Challenge Features

- Reversing
- Story Driven
- Identifying
- Layering
- Brute Force
- Injection or Payload

Frequency Analysis

MirrorBox

to reverse MirrorBox Encryption (we know the encryption process), simply reverse the encryption process.
