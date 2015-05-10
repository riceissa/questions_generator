# How to use

Run with Python 3 as follows:

```bash
python3 question.py data.txt
```

As you can see in `data.txt`, variables in questions are defined using
`{}`. If you need more than one variable, just use more than one `{}`;
in the question line in `data.txt`, however, you have to define each
variable using additional columns, like so:

```
What is it like to give {} {}? | dogs, cats | apples, oranges
# Output:
# What is it like to give dogs apples?
# What is it like to give dogs oranges?
# What is it like to give cats apples?
# What is it like to give cats oranges?

```

You can define custom lists in `lists.py`, which will be treated like
comma-separeted strings. (See `data.txt` and `lists.py` for how these
are used together.)

You can also turn on reporting of number of answers with the `-n` flag.
Also if you don't specify an input file, you can read from stdin and
then press `Ctrl`-`d` when you're done with input.  Example:

```bash
$ python3 question.py -n
What is it like to be {}? | PERSON
# Hit Ctrl-d
What is it like to be Mark Zuckerberg?
What is it like to be Travis Kalanick?
What is it like to be Jimmy Wales?
What is it like to be Peter Thiel?
What is it like to be Elon Musk?
What is it like to be Noam Chomsky?
What is it like to be Bryan Caplan?
7 questions were generated
```
