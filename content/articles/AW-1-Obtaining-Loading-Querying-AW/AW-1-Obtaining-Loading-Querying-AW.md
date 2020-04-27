Title: AW-1: Obtaining, Loading and Querying Adventure Works Database
Date: 2020-04-27
Modified: 2020-04-27
Category: Tutorial
Tags: AdventureWorks, Tutorial, Databases
Author: Daniel
Summary: Hello and welcome to the first in a series of tutorials utilising Microsoft's Adventure Works database samples. The focus of these tutorials will be on database and analytics concepts and software. In particular, we will look at performing queries and other important tasks with SQL Server Management Studio, interacting with databases with python, creating Power BI reports and many other topics.



<!-- # Working with the Adventure Works Databases -->



## Introduction

Hello and welcome to the first in a series of tutorials utilising Microsoft's Adventure Works database samples. The focus of these tutorials will be on database and analytics concepts and software. In particular, we will look at performing queries and other important tasks with SQL Server Management Studio, interacting with databases with python, creating Power BI reports and many other topics.

As you may already know, SQL server is not a database it is database management system.
Microsoft does, however, have several [sample databases](https://docs.microsoft.com/en-us/sql/samples/sql-samples-where-are?view=sql-server-ver15) that can be freely downloaded. These are very useful when coming to grips with database concepts and also Microsoft's database and analytics software, e.g., SQL Server, SQL Server Management Studio, Power BI, SSIS, and so on.

In this series of
tutorials we will be taking a close look at the Adventure Works
databases. Adventure Works is a fictitious bicycle company (Adventure Works
Cycles).
The **AdventureWorks** database is the Online Transaction Processing (OLTP)
sample database and **AdventureWorksDW** data warehouse is the Online
Analytics Processing (OLAP) sample.
The OLTP database sample supports standard online transaction
processing scenarios for the company, e.g., manufacturing, sales, purchasing,  
product management, and human resources, while the OLAP data warehouse is
set up for related analytics scenarios. Over the years new versions of these databases have been released making them compatible with newer features of SQL server. Although, these previous databases a not that dissimilar to the current versions. In these tutorials, we will be
using the AdventureWorks2017 and AdventureWorksDW2017 databases. To take
advantage of SQL server's more recent features and Azure SQL Database, one
should look into the [World Wide Importer database samples](https://github.com/Microsoft/sql-server-samples/tree/master/samples/databases/wide-world-importers).

A typical company will generally have many OLTP systems which support their
day to day business. These OLTP systems are usually highly normalised. Data from
these systems is quite often Extracted, Transformed and then Loaded (ETL) into
OLAP systems. These systems tend to have less normalised tables, usually implementing star and/or snowflake schemas. We
will discuss these details in future tutorials. In our first tutorial our aim is
to simply obtain and load these two databases into SQL Server using SQL Server
Management Studio and then perform a simple query.



## Obtaining

The first thing to do is to obtain the back up files for these Adventure Works
databases. The Adventure Works samples can be obtained from [Microsoft's documentation pages](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15) or their [GitHub repository](https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks). Simply click on and
download **AdventureWorks2017.bak** and **AdventureWorksDW2017.bak**.

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/AW-Download.png" width=900>
</center>

&nbsp;


Place these backup files in

```cmd
 C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\Backup
```

## Loading

Now open SQL Server Management Studio. You should see the screen shown below.

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Arrows Connect Cropped.png" width=900>
</center>

&nbsp;

Set Server type to Database engine, select your server name and chose your
authentication method. If you are not sure about this, a typical default for a
personal setup is Windows Authentication. Then finally click connect.


Now in **Object Explorer** window right click on Databases and click on **Restore Database**.

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Restore DB.png" width=900>
</center>

&nbsp;

Under **Source** select **device**, then click on the ellipsis (the 3 dots).

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Select Backup Device.png" width=900>
</center>

&nbsp;

Click **Add**.

&nbsp;



<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Click Add.png" width=900>
</center>

&nbsp;

Navigate to the backup folder and select AdventureWorks2017 and click ok.

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Select AW.png" width=900>
</center>

&nbsp;

Click ok.

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Click Ok after selecting db.png" width=900>
</center>

&nbsp;

Click ok again.

&nbsp;

<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Click Ok again.png" width=900>
</center>

&nbsp;

Now AdventureWorks2017 database has been added. Click ok and repeat the previous
steps to add AdventureWorksDW2017.

&nbsp;


<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - AW restored.png" width=900>
</center>

&nbsp;

## Querying  with SQL Server

Now that we have some databases added to SQL Server. Expand the **Databases**
tree by clicking on the plus sign to see the available databases, then expand
the AdventureWorks2017 database and then expand the Tables folder. This will
allow you to see the many tables in the database.

&nbsp;


<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - AW DB and Tables.png" width=700>
</center>


&nbsp;


To write a query in SQL Server click on New Query.

&nbsp;


<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - New Query.png" width=700>
</center>


&nbsp;


Before you write your query go to Edit > IntelliSense > Refresh Local Cache.
This will update the autocompletion for the new databases you have
just added.

&nbsp;


<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - IntelliSense.png" width=700>
</center>


&nbsp;


Now you can writer your very first query. In the new query text editor window
type

```sql
USE AdventureWorks2017;
SELECT * FROM HumanResources.Employee;
```

Click execute.

&nbsp;


<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Execute Query.png" width=700>
</center>


&nbsp;

This query simply displays the contents of the Employee table, which appears in
the window at the bottom of the screen.

&nbsp;


<center>
<img src="articles/AW-1-Obtaining-Loading-Querying-AW/screenshots/SS - Query Results.png" width=700>
</center>


&nbsp;

You can similarly query the AdventureWorksDW2017 data warehouse in the same way,
but notice that the list of tables is quite different. The OLAP system uses a
dimensional model with many fact and dimension tables. This will be discussed in
later tutorials. In our next tutorial we will query this database using python.

## Conclusion

In this tutorial we looked at obtaining, loading and querying the Adventure
Works OLTP and OLAP databases. We have barely scratched the surface of what's in
and what can be done these databases. In subsequent tutorials we will make
extensive use of these databases to practice writing SQL queries, creating
reports with Power BI and much more.

## Further Reading

1. Microsoft's [sample databases](https://docs.microsoft.com/en-us/sql/samples/sql-samples-where-are?view=sql-server-ver15) documentation.

2. Dataedo AdventureWorks [data dictionary](file:///C:/Users/dell_lappy.DESKTOP-T6KCVJT/My_Files/Git_repos_mine/private-repos/adventure-works-resources/AdventureWorks.pdf) has very useful information about the Adventure Works database.

3. AdventureWorks2008 database schema can be found [here](https://akela.mendelu.cz/~jprich/vyuka/db2/AdventureWorks2008_db_diagram.pdf). This is the schema for the 2008 version, but this is very close to the 2017 version.

4. AdventureWorksDW2008 database schema can be found [here](http://www.iam.fmph.uniba.sk/institute/odrobina/AdventureWorksDW2008.pdf). This is the schema for the 2008 version, but this is very close to the 2017 version.

5. D. L. Whittenbury, Blog post: "AW-2: Querying Adventure Works Database with Python", April 2020.
