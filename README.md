## Set up
Create a free Datastax account at https://www.datastax.com/

  Click Create Database

  ![Graphical user interface, application, email  Description automatically generated](https://github.com/cosc-516-2022/lab10/blob/main/Cassandra/README.assets/clip_image002.jpg?raw=true)

   

  Name your database and keyspace – remember your keyspace’s name! Select under provider and region “Google Cloud” -“North America” -“Moncks Corner, South California”. Make sure the current plan is free, and click “Create Database”.

  ![Graphical user interface, application  Description automatically generated](https://github.com/cosc-516-2022/lab10/blob/main/Cassandra/README.assets/clip_image004.jpg?raw=true)

   

   

   

  Make sure to save your token details, as you would not be able to access it later.

  Once it’s saved, click “Go to Database”.

  ![Graphical user interface, application  Description automatically generated](https://github.com/cosc-516-2022/lab10/blob/main/Cassandra/README.assets/clip_image006.jpg?raw=true)

  Under dashboard, click the database you just created and go to “CQL Console”.

  ![Graphical user interface, application, email  Description automatically generated](https://github.com/cosc-516-2022/lab10/blob/main/Cassandra/README.assets/clip_image008.jpg)
  
##Run CQL queries in the Datastax console

  In the console, you could test your CQL queries.

  ![Graphical user interface, text, application, Teams  Description automatically generated](https://github.com/cosc-516-2022/lab10/blob/main/Cassandra/README.assets/clip_image010.jpg?raw=true)

  Datastax has its own documentary “DataStax Python Driver” for how to execute CQL queries using Python.

  Cassandra’s official documentary also includes information on how Cassandra works.

   

   

  Write Python code using VS Code. The file to edit is “cassandra.py”. The test file is “test_cassandra.py”. Fill in the methods requested (search for **TODO**). Marks for each method are below. You will receive the marks if you pass the pytest tests **AND** have followed the requirements asked for in the question (including documentation and proper formatting).
##Tasks
  - +? mark -  Write the method connect() to create a connection to Datastax.
  - +? mark -  Write the method create() to create a table with proper schema, PLEASE NAME IT "Customer".
  - +? marks - Write the methods load () customer.csv into the Datastax. Use appropriate   data structures.
  - +? marks - Write the method query1() that returns the age of the customer whose id is 979863.
  - +? marks - Write the method query2() that returns information of customers who  are “MALE” and age is 25 or 35.
## Bonus Marks: (up to 3)

- Up to +3 bonus marks for demonstrating some other unique feature of Cassandra.

## Submission

The lab is marked immediately by the professor by showing the output of the unittests and by a quick code review.  Otherwise, submit the URL of your GitHub repository on Canvas. **Make sure to commit and push your updates to GitHub.**
