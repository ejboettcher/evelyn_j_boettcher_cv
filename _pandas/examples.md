## Big Data: Numbers Only

* Script: int_floats_cats.py

<br/>


```bash
Building three DF with:
     Range of numbers 1- 4
     Length of DF  10_000
Top 10 rows of data
   INT  INT8     FLOAT
1    2     4  3.329446
2    2     4  1.478631
3    2     3  1.338759
4    3     1  1.846993
5    1     2  2.787727
6    4     3  1.116634
7    1     2  1.064875
8    3     3  3.146007
9    3     2  2.201730

Size of the DF we just made
INT    0.0764MB
INT8   0.0096MB
FLOAT  0.0764MB
____________________
As categories (plain df, category, SAVINGS):
INT  df ---> 0.0764MB , 0.0098MB , 87 %
INT8 df ---> 0.0096MB , 0.0098MB , -2 %
___NOTE______NOTE______NOTE______NOTE___
Categories reduced the size INT df!!
   BUT because of the overhead
   it did not reduce the int8 size

Now, lets try this with random Floats
Float         --->  0.0764MB
Float category--->  0.4079MB
Categories only made the DF memory use worse



All Done

```

---

## Reduced Frequency of Numbers in DF

Let's try it again, but reduce the frequency (e.g. Numbers repeat less) 
by increasing the range of number from r = 4 to r = 240.


* Script: int_floats_cats.py -r 240


```Bash
Building three DF with:
     range of numbers 1 - 240
     length of DF  10_000
Top 10 rows of data
   INT  INT8       FLOAT
1   12   100  235.429842
2   19    63  225.656414
3   13    20  173.416396
4   49   -60   36.324557
5  147  -100   42.525923
6   82    63   15.278578
7   15   121  202.143259
8   44   -43  225.630105
9  211   103  179.905616

Size of the DF we just made
INT    0.0764MB
INT8   0.0096MB
FLOAT  0.0764MB
____________________
As categories (plain df, category, SAVINGS)
INT  df ---> 0.0764MB , 0.0307MB , 59 %
INT8 df ---> 0.0096MB , 0.0307MB , -219 %
___NOTE______NOTE______NOTE______NOTE___
Categories reduced the size INT df!!
   BUT because of the overhead
   it did not reduce the int8 size

Now, lets try this with random Floats
Float         --->  0.0764MB
Float category--->  0.4079MB
Categories only made the DF memory use worse


All Done
```

---

## Large Data: Numbers cont..

### Increase SIZE

```bash
python int_floats_cats.py -r 4 -n 1_000_000
```

```Bash
Building three DF with:
     range of numbers 1 - 4
     length of DF  1_000_000
Top 10 rows of data
   INT  INT8     FLOAT
1    2     2  2.684429
2    2     4  1.696423
3    1     2  2.607256
4    3     1  1.247054
5    4     3  2.413925
6    2     3  3.141839
7    1     1  3.438698
8    2     2  3.584329
9    1     3  1.019402
Getting size of the DF we just made
INT    7.6295MB
INT8   0.9538MB
FLOAT  7.6295MB
____________________
As categories (plain df, category, SAVINGS)
INT  df ---> 7.6295MB , 0.9539MB , 87 %
INT8 df ---> 0.9538MB , 0.9539MB , 0 %
___NOTE______NOTE______NOTE______NOTE___
Categories reduced the size INT df!!
   BUT because of the overhead
   it did not reduce the int8 size

Now, lets try this with random Floats
Float         --->  7.6295MB
Float category--->  51.4442MB
Categories only made the DF memory use worse


All Done
```

---

## Large Data: Strings

So lets see how we can reduce size of STRINGS arrays.
If you have a column of strings that repeats, 
says days of week, states etc, then you might save memory 
if you switch to columns


```bash
python strings_cat.py
```

```Bash
Building three DF with:
     length of random string in a row 1 - 4
     length of DF  10_000
Top 10 rows of data
        Days  HELLO      Locations     Days_c HELLO_c    Locations_c Random_String
1    Tuesday  World    Beavercreek    Tuesday   World    Beavercreek          xhka
2  Wednesday  Hello        Oakwood  Wednesday   Hello        Oakwood          wiwh
3   Thursday  World      Fairfield   Thursday   World      Fairfield          gahf
4     Friday  Hello  Huber Heights     Friday   Hello  Huber Heights          ldou
5   Saturday  World      Riverdale   Saturday   World      Riverdale          rynl
6     Sunday  Hello         Dayton     Sunday   Hello         Dayton          oasv
7     Monday  World    Beavercreek     Monday   World    Beavercreek          nuym
8    Tuesday  Hello        Oakwood    Tuesday   Hello        Oakwood          gjvs
9  Wednesday  World      Fairfield  Wednesday   World      Fairfield          nmwn
Getting size of the DF we just made
String NO Categories      2.64MB
String WITH Categories    0.0306MB
Random String (1 column)  0.5MB
____________________
As categories
String Columns: HELLO, Locations, Days
(plain df, category, SAVINGS)
NO CAT to category ---> 2.67MB , 0.03MB , 98 %
Cat df to category ---> 0.0306MB , 0.0306MB , 0 %
___NOTE______NOTE______NOTE______NOTE___

Now, lets try this with random STRINGS
String: Random         --->  0.5818MB
String: Random category--->  0.9068MB
Categories only made the DF memory use worse




.
```

---

## Large Data: STRING
#### Now, lets make this BIGGGG

* 1 million rows
* 4 chars long in each cell

```bash
python strings_cat.py -n 1_000_000 -r 4
```

```Bash
Building three DF with:
     length of random string in a row 1 - 4
     length of DF  1_000_000
Top 10 rows of data
     Days  HELLO      Locations     Days_c HELLO_c    Locations_c Random_String
   Tuesday  World    Beavercreek    Tuesday   World    Beavercreek        qbzd
 Wednesday  Hello        Oakwood  Wednesday   Hello        Oakwood        wixv 
  Thursday  World      Fairfield   Thursday   World      Fairfield        vwjs    
   Friday  Hello  Huber Heights      Friday   Hello  Huber Heights        xiiz
  Saturday  World      Riverdale   Saturday   World      Riverdale        owon
    Sunday  Hello         Dayton     Sunday   Hello         Dayton        jihl
    Monday  World    Beavercreek     Monday   World    Beavercreek        xwon
   Tuesday  Hello        Oakwood    Tuesday   Hello        Oakwood        zchj
 Wednesday  World      Fairfield  Wednesday   World      Fairfield        hnjt

Size of the DF we just made
String NO Categories      267.2MB
String WITH Categories      2.8MB
Random String (1 column)  58.17MB
____________________
As categories
String Columns: HELLO, Locations, Days
               (plain df, category, SAVINGS)
NO CAT to category ---> 267.2MB , 2.8MB , 98 %
Cat df to category ---> 2.8MB , 2.8MB , 0 %
___NOTE______NOTE______NOTE______NOTE___

Now, lets try this with random STRINGS
String: Random         --->  58.1MB
String: Random category--->  47.3MB
____________________________________________________
WHAT.......
   There was an improvement!!!
   HOW  DID  THAT  HAPPEN????
____________________________________________________


.
```

#### There was an improvement!!!
HOW  DID  THAT  HAPPEN????


---

#### Interesting Fact:

When we have a random string of characters of length 4 (26 char in the alphabet)
<br/>
    (e.g. 26 x 26 x 26 x 26 = 456,976) 
<br/>

Therefor over 1/2 of the strings should repeat!


---

## Larger Data: strings cont.


```bash
python strings_cat.py -n 10_000_000 -s 1 -r 6
```

This should produce a csv file called <br/>

* *my_awesome.csv* with a size of 550.6MB and
* *my_awesome_cat.csv* with size of 486.2  (No random str)

<br/>


---


```bash
Starting
Building three DF with:
     length of random string in a row 1 - 6
     length of DF  10_000_000
Top 10 rows of data
        Days  HELLO      ...         Locations_c Random_String
1    Tuesday  World      ...         Beavercreek        ahlcks
2  Wednesday  Hello      ...             Oakwood        rwccxh
3   Thursday  World      ...           Fairfield        ihyieo
4     Friday  Hello      ...       Huber Heights        rtxevt
5   Saturday  World      ...           Riverdale        whpjhe
6     Sunday  Hello      ...              Dayton        vktted
7     Monday  World      ...         Beavercreek        klajfi
8    Tuesday  Hello      ...             Oakwood        eneums
9  Wednesday  World      ...           Fairfield        jvruya

[9 rows x 7 columns]
Size of the DF we just made
String NO Categories      2672.3MB
String WITH Categories      28.6MB
Random String (1 column)   600.8MB
____________________
As categories
String Columns: HELLO, Locations, Days
               (plain df, category, SAVINGS)
NO CAT to category ---> 2672.8MB , 28.6122MB , 98 %
Cat df to category ---> 28.6MB , 28.6123MB , 0 %
___NOTE______NOTE______NOTE______NOTE___

Now, lets try this with random STRINGS
String: Random         --->  600.8MB
String: Random category--->  949.3MB
Categories only made the DF memory use worse


.
```


---

## Read in...

 `my_awesome_cat.csv` (Files size: ~486MB)

</br>

* Same data as my_awesome.csv, but **without** the column of random strings

#### WOW

The data in memory is **LESS** than the file size, by almost 90%!

```Bash
USING CATEGORIES for columns that make sense.
__________________________________________________

It took this many seconds to read in the csv file 7.85
__________________________________________________
Now lets look at size
Memory of Df is:  57.2MB
Top 4 rows of data
   HELLO      Locations       Days HELLO_c    Locations_c     Days_c
1  World    Beavercreek    Tuesday   World    Beavercreek    Tuesday
2  Hello        Oakwood  Wednesday   Hello        Oakwood  Wednesday
3  World      Fairfield   Thursday   World      Fairfield   Thursday
4  Hello  Huber Heights     Friday   Hello  Huber Heights     Friday
13    Sunday
20    Sunday
27    Sunday

Name: Days, dtype: category
Categories (7, object): [Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday]
__________________________________________________


```
