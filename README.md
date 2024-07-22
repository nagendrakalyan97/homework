# Paragraph to lines based on width

This file takes two parameters as input one is paragraph as a string, an integer value as width and gives an array of lines that fit within specified width.

# Assumption
Assuming minimum of one character space between words and length of line is less than or equal to the width.

# Usage
python3 ./paragraph.py <"Paragraph String"> <"integer_value">

# Example
## Input 1:
width = 20

python ./paragraph.py "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." 20

## Output 1:
<pre>
Array[1] = "This   is  a  sample"
Array[2] = "text      but      a"
Array[3] = "complicated  problem"
Array[4] = "to  be solved, so we"
Array[5] = "are adding more text"
Array[6] = "to   see   that   it"
Array[7] = "actually      works."
</pre>

## Input 2: 
width = 15

python ./paragraph.py "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." 100
## Output 2:
<pre>
Array[1] = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that"
Array[2] = "it                                          actually                                          works."
</pre>

## Input 3:
width = 30

python ./paragraph.py "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." 30
## Output 3:

<pre>
Array[1] = "This  is  a  sample text but a"
Array[2] = "complicated   problem   to  be"
Array[3] = "solved,  so we are adding more"
Array[4] = "text  to  see that it actually"
Array[5] = "works.                        "
</pre>

## Input 4:
width = 5

python ./paragraph.py "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." 5
## Output 4:
<pre>
Array[1] = "This "
Array[2] = "is  a"
Array[3] = "sample"
Array[4] = "text "
Array[5] = "but a"
Array[6] = "complicated"
Array[7] = "problem"
Array[8] = "to be"
Array[9] = "solved,"
Array[10] = "so we"
Array[11] = "are  "
Array[12] = "adding"
Array[13] = "more "
Array[14] = "text "
Array[15] = "to   "
Array[16] = "see  "
Array[17] = "that "
Array[18] = "it   "
Array[19] = "actually"
Array[20] = "works."
</pre>
