# Objective
To demonstrate **Ansible** using a python webapp containerized inside **Docker**.

# Steps
1. Setup an **Ansible Master Server** and a **slave node** for deployment.
2. Written code for a demo hello-world webapp using **streamlit** in **python**.
3. Containerize the above webapp using **Docker**.
4. Setup a **Jenkins** pipeline to trigger a build(execute the **Ansible playbook**) on the **Ansible Master Server**.
5. The playbook pulls the Git repo on the **Ansible Slave Node** and **deploys** the application on the **Ansible Slave Node**.
