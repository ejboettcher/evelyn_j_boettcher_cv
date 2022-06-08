## Data Memory footprint

(sans overhead)

#### Numbers

|memory usage |	int|	uint | float | 	bool  |	  complex |
|:---:        |:----|:----   |:----  |:----     |:----       |
|1 bytes |  int8 (-128-127)  | uint8 (0-255)| | bool |        |
|2 bytes |	int16	 (-32768 to 32767) | uint16 (0 to 65535) |float16 (Half precision)| |   |
|4 bytes |	int32 |	uint32 |	float32 (Single precision)    |	|   |
|8 bytes	|f	int64	|   uint64 |float64 |         |  complex64 (rep. by 2 32-bit floats) |

#### Strings
Python uses three kinds of internal representations for Unicode strings:

* 1 byte per char (Latin-1 encoding)
* 2 bytes per char (UCS-2 encoding)
* 4 bytes per char (UCS-4 encoding)

---

## How does Panda's categories work?

Pandas category type uses integer values to map to the raw values in a column.  
<br/>

This mapping is useful whenever a column contains a limited set of values.

So instead of writing
#### df.mydays = ["Sunday", "Sunday", "Sunday"]

<br/>
Pandas categories says

#### Sunday = 1

and the DataFrame **in memory** is effectively now

#### df.mydays = [1, 1, 1]

---

## Convert Data to Categories

To convert a column of data to the category we set the data type (dtype).

```Python
df['column name'].astype('category')
```

![SundaySunday df](assets/img/pandas/SundaySunday.png)



### But wait..

Converting to categories is not always helpful.
<br/>

The following examples will show the power and pitfalls of categories

