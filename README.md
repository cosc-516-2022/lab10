## Set up
Create a free Datastax account at https://www.datastax.com/

  Click Create Database

  <img src="Cassandra/README.assets/clip_image002.jpg" alt="Create Cluster">
   

  Name your database and keyspace – remember your keyspace’s name! Select under provider and region “Google Cloud” -“North America” -“Moncks Corner, South California”. Make sure the current plan is free, and click “Create Database”.

  <img src="Cassandra/README.assets/clip_image004.jpg" alt="Create Cluster">

   

   

   

  Make sure to save your token details, as you would not be able to access it later.

  Once it’s saved, click “Go to Database”.

  <img src="Cassandra/README.assets/clip_image006.jpg" alt="Create Cluster">

  Under dashboard, click the database you just created and go to “CQL Console”.

 <img src="Cassandra/README.assets/clip_image008.jpg" alt="Create Cluster">
  
## Run CQL queries in the Datastax console

  In the console, you could test your CQL queries.

 <img src="Cassandra/README.assets/clip_image010.jpg" alt="Create Cluster">

  Datastax has its own documentary “DataStax Python Driver” for how to execute CQL queries using Python.

  Cassandra’s official documentary also includes information on how Cassandra works.

   

   

  Write Python code using VS Code. The file to edit is “cassandra.py”. The test file is “test_cassandra.py”. Fill in the methods requested (search for **TODO**). Marks for each method are below. You will receive the marks if you pass the pytest tests **AND** have followed the requirements asked for in the question (including documentation and proper formatting).
## Tasks
  - +1 mark -  Write the method connect() to create a connection to Datastax.
  - +1 mark -  Write the method create() to create a table with proper schema, PLEASE NAME IT "Customer".
  - +2 marks - Write the methods load() customer.csv into the Datastax. Use appropriate data structures.
  - +2 marks - Write the method query1() that returns the age of the customer whose id is 979863.
  - +2 marks - Write the method query2() that returns information of customers who  are “MALE” and age is 25 or 35.

## Bonus Marks: (up to 2)

- Up to +2 bonus marks for demonstrating some other unique feature of Cassandra.

## Submission

The lab is marked immediately by the professor by showing the output of the unittests and by a quick code review.  Otherwise, submit the URL of your GitHub repository on Canvas. **Make sure to commit and push your updates to GitHub.**
