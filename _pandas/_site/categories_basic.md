## Python Pandas

Python's Pandas is a high performance, easy to use library for analyzing structured
 data: csv files, json, SQLite etc.
<br/>

Pandas is fast, powerful and flexible. 
It enables you to quickly parse data. 
**But**, it is mainly designed to handle ~<100mb.  


<br/>


There are other tools like Spark to handle LARGE data sets 
(100 gigabytes to terabytes), but...

#### Pandas does an amazing job at cleaning messy / real data.

---

## How does one handle Large data with Pandas
When you have a gigabyte of real world data
and you want to:

* Explore it
* Use your laptop and
* You don't want to switch to Spark.  

<br/>

### Step One:

Use old programming tricks like set numbers to 
***int8***, ***floats16***, or ***float32*** etc to 
reduce the memory size of your DataFrame.  

---

## Second Step: Use Categories

If you have strings that ***repeat*** SWITCH to

### categories

<br/>

### String Examples
#### Non-repeating strings

```Python
string_list = ['Hello', 'World', 'More Strings', 'Evelyn','Boettcher']
```

#### Repeating String
Many times string data will be repetitive, like days of week.

```Python
val_days = ['Monday', 'Tuesday', 'Monday', 'Wednesday', 'Monday', 
            'Thursday', 'Friday', 'Saturday', 'Monday', 'Monday', 
            'Sunday']
```