Create a local <--folder name--> of the project
Create a module folder that will contain all the helper functions in module folder 
**Imp** 
  **A __init__.py must be intialised in order to use the function from the module folder to whichever function required**
Create a dependencies folder which will contain all the packages that are required for running the program successfully.
Following commands will be implemented:
    `pipreqs .` -> If the requirement.txt is not initialised.
    `pipreqs --force` -> If changes in requirement.txt needs to be updated.
For zipping entire bundle use the following commands:
    ` cd <--folder name-->`
    ` zip -rq ../deployment_V1.zip . && echo "Zipping completed!" `
