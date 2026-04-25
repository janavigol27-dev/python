#### **Sales Analysis Dashboard**



###### **Project Overview**



I have created a professional Sales Dashboard using Power BI and PowerPoint. The goal of this project is to analyze customer behavior, sales trends, and regional performance to help business decisions.



Steps Followed in this Project



**1. Background Design (PowerPoint)**

Designed a custom dashboard background in PowerPoint for a clean and professional look.

Used rounded rectangles and shadow effects to create distinct sections for KPIs and Charts.

Exported the design as an image and set it as the Canvas Background in Power BI with 0% transparency.



**2. Data Cleaning \& Transformation (Power Query)**

Imported the dataset (Customers, Orders, Products, and Shipping tables) into Power BI.

Used Power Query Editor to:

Remove duplicates and null values.

Correct data types (e.g., setting Order \_Date to 'Date' format).

Standardized columns like Gender and City for accurate filtering.



**3. Data Modeling**

Established relationships between tables in the Model View.

Created a "One-to-Many" relationship between Customers and Orders to track sales per customer accurately.



**4. DAX Calculations (Measures)**

Created several DAX measures to get deep insights, including:

Total Sales: Calculated by multiplying Quantity and Unit Price.

Total Quantity: To track the volume of products sold.

Active Customers: Using DISTINCTCOUNT to find unique buyers.



**5. Data Visualization**

Built the following visuals to represent the data:

KPI Cards: Displaying Total Sales, Active Customers, and Total Quantity at the top.

Area Chart: To show the Monthly Sales Performance Trend over time.

Donut Chart: To visualize sales distribution by Product Category.

Clustered Bar Chart: To compare performance across different Cities.

Top N Filters: Applied filters to show only the Top 5 performing cities and categories for a clutter-free view.



**Key Insights**

The Area Chart helps identify which months had the highest growth.

The Top Cities Bar Chart highlights the primary geographic markets.

The Category Donut Chart shows which product types are driving the most revenue.

