# organization_management
Organization Management App for NebriOS

This app is intended for use in a NebriOS instance. Visit https://nebrios.com to sign up for free!

<h4>Setup</h4>
This app requires very little in terms of setup. Please ensure that all files are placed in the correct places over SFTP.

  - add_department.py should be copied to /scripts
  - organization_management.py should be copied to /api

<h4>Usage</h4>
  - Currently, we are using a single organization system
  - When a department is added, the api checks if an organization process already exists. If not, it creates one.
  - Creating a department is very simple, just trigger the script from debug mode with a department name argument
  
    ```
    add_department := True
    name := Development
    ```
  - Once a department is created, it is possible to create employees with https://github.com/briem-bixly/human_resources
