# Objective
To simulate a software development life cycle of a project. Whenever some changes are pushed to the **dev** branch. Automatically a build will begin and
start testing on the Jenkins slave node **test server**. If the build and testing is successfull, it will trigger another build on the Jenkins slave node **production sever**

# Steps
1. Setup a Jenkins **Master Server** Node and 2 Slave Nodes: **test-server** and **prod-server**.
2. Written code for a basic Hellow World **webapp** using **streamlit** in **python**.
3. Containerize the application using **Docker**.
4. Create a pipeline job in Jenkins and add a **github webhook** to trigger build whenever push changes to **dev** branch.
5. Add a **post build** action for the above pipeline to deploy webbapp on **prod-server** if the build is sucessfull.
