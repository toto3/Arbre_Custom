This Python script use Tkinter.
The GUI is in french.

It allow the user to select a Newick phylogenetic tree 
and select a liste (Excel format) of information to add to tip of the tree.
And generate a new Newick tree file with the infomation.

By exemple: 
if you have a tip node like this:
    <pre>                    +--Horse
        +-------------------|
        |                   +--Cow
        |
        |          +--Dog
        |     +----|
        |     |    +--Cat
        +-----|
              |    +--Pig
              +----|
</pre>

  and you provide in the Excel file some thing like:
<pre>
  Cow  MoreInfoAboutCow
  Cat  EvelInternetKing
</pre>
  You will get this on the new Newick file :
    <pre>                    +--Horse
        +-------------------|
        |                   +--Cow_MoreInfoAboutCow
        |
        |          +--Dog
        |     +----|
        |     |    +--Cat_EvelInternetKing
        +-----|
              |    +--Pig
              +----|
</pre>



