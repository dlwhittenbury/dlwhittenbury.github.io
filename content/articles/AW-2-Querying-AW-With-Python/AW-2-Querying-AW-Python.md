Title: AW-2: Querying Adventure Works Database with Python
Date: 2020-04-27
Modified: 2020-04-27
Category: Tutorial
Tags: AdventureWorks, Tutorial, Databases, Python
Author: Daniel
Summary: In this tutorial we will query the SQL Server database AdventureWorksDW2017 with python. We will do this by using pyodbc which is an open source Python module that makes accessing ODBC databases very simple.

<!-- # Working with the Adventure Works Databases -->

<!-- # AW-2: Querying Adventure Works Database with Python -->

In this tutorial we will query the SQL Server database AdventureWorksDW2017 with
python. We will do this by using [pyodbc](https://pypi.org/project/pyodbc/)
which is an open source Python module that makes accessing ODBC databases very
simple.

## 1. Create an Anaconda Environment and Install the Necessary Packages

This step isn't strictly necessary. You can skip creating a dedicated anaconda
environment if you prefer, but you will need to make sure that you have the
necessary packages installed to follow the remaining parts of this tutorial.

From the anaconda prompt create an anaconda environment called whatever you like. I
have chosen to name it **da-py37**, **da** for **d**ata **a**nalysis and **py37** for the **py**thon
version to be installed.

```code
conda create --name da-py37 python=3.7
```
Activate your environment
```code
conda activate da-py37
```

Install the necessary packages
```code
conda install numpy pandas pillow jupyter pyodbc
```

You might be wondering what is Pillow and why we will be needing it. Below when
we query the Adventure Works database we will query the **dbo.DimEmployee** table
which happens to contain photos of the employees. The pillow package will allow
us to handle the images.


The next step is to output a file containing the names and version numbers of
the packages installed. You do not necessarily need to do this, but I think it
is good practice to create a requirements file that contains a list of all
packages used in this project for later use. It is very handy for
reproducibility, especially if you intend to try to do something similar later
on.
```code
conda list -e > aw-2-requirements.txt
```





## 2. Get Server Name and Database Name

If you are not sure what the name of your server is, then open SQL Server
Management Studio and browse **server name**. My server name is identified by
the red rectangle.

&nbsp;

<center>
<img src="articles/AW-2-Querying-AW-With-Python/images/screenshots/server-name-connect.png" width="700">
</center>

&nbsp;

<!-- ![My server name is highlighted, yours maybe different.](./screenshots/server-name-connect.png) -->



Connect to the server which has AdventureWorksDW2017 loaded in it. Now look
in the Object explorer window. Expand databases and you should see all the
databases you have loaded listed. We want the **AdventureWorksDW2017** database.
If you expand the Tables folder you can see a list of tables in the database.
We will be making use of the **dbo.DimEmployee** table in this tutorial.

<center>
<img src="articles/AW-2-Querying-AW-With-Python/images/screenshots/database-table-names.png" width="700">
</center>


## 3. Connecting to the Adventure Works Database

### Import packages  

```python
import pandas as pd
import pyodbc
from PIL import Image
import io
```

### Connect to the Database

Define variables to store the server and database names obtained in step 2.
```python
server_name = "DESKTOP-T6KCVJT"
db_name = "AdventureWorksDW2017"
```

Define the following string **connnection_str** using the variables above
```python
connection_str =  'Driver={SQL Server};' + 'Server=' + server_name + ";Database=" + db_name + ";Trusted_Connection=yes;"
```

Now use this string as an argument to the **pyodbc.connect** function which will
make a connection to the database.
```python
conn = pyodbc.connect(connection_str)
```


## 4. Querying the AdventrureWorksDW2017 Database

Now we will query the Adventure Works database returning the whole
**DimEmployee table** which will be put it into a pandas dataframe.
First we define a string containing our SQL query.
```python
query_1 = "SELECT * FROM dbo.DimEmployee"
```
Please note that if you want to perform a more complicated query that spans
several lines you should enclose the string with triple quotation marks, i.e.,
"""Your More Complicated Query Here""". Finally to query the database we make use of the pandas library function
**read_sql** which returns the data as a pandas dataframe.
```python
df = pd.read_sql(query_1, conn)
```

We can get some summary information about the dataframe, e.g., column names,
data types etcetera, by using pandas **pd.DataFrame.info** function

<!-- ```python
df.info()
``` -->


<center>
<img src="articles/AW-2-Querying-AW-With-Python/images/screenshots/pandas-df-info.png" width="900">
</center>

&nbsp;

## 5. Taking a Peek at the Employee Mug Shots

In the image above we notice that the table stores the photos of each of the 296
employees. To print the very first entry in the EmployeePhoto field we do the
following:
```python
pic = df.EmployeePhoto[0]
print(pic)
```

If you do this you will notice that it is a very long string of the form
"b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H .......'". This is a
binary string and the JFIF marker indicates it is a JPEG image. If you would
like to write this binary string to a **\*.jpg** file this is easily done by
defining the following function:
```python
def save_img(bin_str_img,name_img):
   with open (name_img,"wb") as f:
       f.write(bin_str_img)

save_img(pic,"employee.jpg")
```
Above we note that **'wb'** means **w**rite **b**inary. To show the image we make
use of the **io** and **PIL** packages

```python
image_stream = io.BytesIO(pic)
image_file = Image.open(image_stream)
image_file
```
<center>
<img src="articles/AW-2-Querying-AW-With-Python/images/employee.jpg" width="450">
</center>

&nbsp;

We can also save it using
```python
image_file.save("employee-again.jpg")
```

<!-- ```python
df.iloc[0]
``` -->

This employee's information can be easily accessed using the **iloc** function.
Afterwhich, we find out this guys name is Guy R. Gilbert and he is a production
technician.

<center>
<img src="articles/AW-2-Querying-AW-With-Python/images/screenshots/guy-r-gilbert.png" width="900">
</center>

## Conclusion

In this tutorial we looked at connecting to and querying an SQL Server database
using python. Now that you know how to connect to database in SQL Server you
can also interact with the database using python in other ways, e.g., updating
and deleting records if you so desire. In later tutorials we will look at
performing more complex queries, creating visualisations with Power BI and we
will also work in some machine learning along the way as well.

## Further Reading

  1. D. L. Whittenbury, Blog post: "AW-1: Obtaining, Loading and Querying the Adventure Works Database", April 2020.

  2. Documentation on pyodbc <https://github.com/mkleehammer/pyodbc/wiki>.

  3. Specific information about connecting to SQL Server from Windows in  the
  pyodbc documentation <https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows>.
