# Data Storage

There are two main drives for data storage:

| Usage Type   | Operational Usage                          | Analytical Usage                          |
|--------------|--------------------------------------------|-------------------------------------------|
| Purpose      | Day-to-day operations                      | Business insights and decision making     |
| Data Type    | Current, real-time data                    | Historical data                           |
| Data Volume  | Typically smaller, manageable volumes      | Large volumes of data                     |
| Access Speed | Fast access for immediate needs            | Optimized for complex queries and analysis|
| Examples     | Transaction processing, customer management| Data mining, reporting, trend analysis    |


For each, there's a different type of processing:

- **OLTP** (Online Transactional Processing)
- **OLAP** (Online Analytical Processing)


| Feature                | OLTP (Online Transactional Processing) | OLAP (Online Analytical Processing)       |
|------------------------|----------------------------------------|-------------------------------------------|
| Purpose                | Manage day-to-day operations           | Support complex analysis and decision making|
| Data Type              | Current, real-time data                | Historical, aggregated data               |
| Query Type             | Simple, standardized queries           | Complex queries involving aggregations    |
| Data Updates           | Frequent, short transactions           | Infrequent, bulk updates                  |
| Schema                 | Normalized for efficiency              | Denormalized for read performance         |
| Examples               | Order entry, retail sales              | Sales forecasting, market research        |
&nbsp;


# Data Warehouse

Where does a data warehouse fit in this?

## Single-Tier Architecture

![alt text](image-1.png)

This is a the simplest architecture for a data warehouse system. Known as <b>Single-Tier Data Warehouse</b> Key challenges with this architecture are:
- Performance Issues (Seven - DB crashes)
- Scalability
- Not Flexible (Pre-defined schemas in the RDB for DW)

this is considered an OLTP + OLAP simple integration. Not a data warehouse in that sense.

** Here, Datawarehouse is considered the OLAP layer, the sources are the OLTP.


## Two-Tier Architecture

![alt text]({053308A2-746F-4CF5-A8AF-72730EB8D384}.png)

Adding an intermediate layer between data sources and data warehouse, storing the raw data, even unstructured or semi-structured. This gives us more flexibility with analyzing the data, as well as keeping track of the historical raw data.

- However, this adds complexity and running costs over the single-tier architecture. It also requires more effort for maintenance due to its more complex nature and increased system components.

## Three-Tier Architecture

![alt text]({AF13A1FD-3A7E-4C8B-9A2C-A3C096434B54}.png)

The most-used data warehouse architecture for larger enterprises with large amounts of data from various sources. 
However, it has the obvious drawbacks of being complex and costly as well as being the most demaing from a technical perspective. 

&nbsp;
&nbsp;


# Data Warehouse Layer

## Data Modeling
In data warehouses, a modeling technique called **Dimensional Modeling** is used to organize the data. 
Dimensional Modeling includes separating the data into:
- **Fact Tables**:
    - Contain quantitative data (measures) like sales amount, quantity sold.
- **Dimension Tables**:
    - Contain describtive attributes (dimensions) like time, geography, product

Both are linked via foreign keys. 
### Example Tables

#### Fact Table: Sales
| SaleID | ProductID | CustomerID | TimeID | Quantity | TotalAmount |
|--------|-----------|------------|--------|----------|-------------|
| 1      | 101       | 1001       | 202201 | 2        | 40.00       |
| 2      | 102       | 1002       | 202202 | 1        | 20.00       |
| 3      | 103       | 1003       | 202203 | 5        | 100.00      |

#### Dimension Table: Time
| TimeID | Date       | Month | Quarter | Year |
|--------|------------|-------|---------|------|
| 202201 | 2022-01-01 | Jan   | Q1      | 2022 |
| 202202 | 2022-02-01 | Feb   | Q1      | 2022 |
| 202203 | 2022-03-01 | Mar   | Q1      | 2022 |

#### Dimension Table: Customers
| CustomerID | Name       | Location   | Age |
|------------|------------|------------|-----|
| 1001       | John Doe   | New York   | 30  |
| 1002       | Jane Smith | Los Angeles| 25  |
| 1003       | Bob Brown  | Chicago    | 40  |


The way these tables are organized in the data warehouse define how our schema will be designed. 

## Schema Design

### Star Schema
![alt text](image-2.png)

Star schema is the simplest form with a central fact table connected to multiple dimension tables.
It's easy to understand and query. 
However, in the star schema, the dimension table is not normalized. Since it's fact-centric, dimensions are designed to include everything for that specific fact record using only the foreign key. 

### Snowflake Schema

![alt text](main.jpg)
An extension of the star schema with normalized dimension tables.
reduces data redundancy but can be more complex, and leads to more complex joins (just like any normalization)


### Example Tables for Snowflake Schema

#### Fact Table: Sales
| SaleID | ProductID | CustomerID | TimeID | Quantity | TotalAmount |
|--------|-----------|------------|--------|----------|-------------|
| 1      | 101       | 1001       | 202201 | 2        | 40.00       |
| 2      | 102       | 1002       | 202202 | 1        | 20.00       |
| 3      | 103       | 1003       | 202203 | 5        | 100.00      |

#### Dimension Table: Time
| TimeID | Date       | MonthID | QuarterID | YearID |
|--------|------------|---------|-----------|--------|
| 202201 | 2022-01-01 | 1       | 1         | 2022   |
| 202202 | 2022-02-01 | 2       | 1         | 2022   |
| 202203 | 2022-03-01 | 3       | 1         | 2022   |

#### Dimension Table: Month
| MonthID | MonthName |
|---------|-----------|
| 1       | Jan       |
| 2       | Feb       |
| 3       | Mar       |

#### Dimension Table: Quarter
| QuarterID | QuarterName |
|-----------|-------------|
| 1         | Q1          |
| 2         | Q2          |
| 3         | Q3          |
| 4         | Q4          |

#### Dimension Table: Year
| YearID | Year |
|--------|------|
| 2022   | 2022 |
| 2023   | 2023 |

#### Dimension Table: Customers
| CustomerID | Name       | LocationID | Age |
|------------|------------|------------|-----|
| 1001       | John Doe   | 1          | 30  |
| 1002       | Jane Smith | 2          | 25  |
| 1003       | Bob Brown  | 3          | 40  |

#### Dimension Table: Location
| LocationID | City        |
|------------|-------------|
| 1          | New York    |
| 2          | Los Angeles |
| 3          | Chicago     |



# Scalability on single level
    -> explain file system
    -> go to distributed file system from here
    -> Hadoop 
    -> MapReduce
    -> YARN


now that we covered all topics, let's see some datawarehouse projects. (Cloud/on-prem)
    -> Hive
    -> Redshift
    -> ClickHouse
    -> Azure synabse
