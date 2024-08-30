Create a local `<--folder name-->` of the project.
Create a `module` folder that will contain all the helper functions in the module folder.
**Imp**: A `__init__.py` must be initialized in order to use the functions from the `module` folder in other parts of the project.
Create a `dependencies` folder which will contain all the packages required for running the program successfully.
Use `pipreqs .` to generate a `requirements.txt` if it is not already initialized.
Use `pipreqs --force` to update `requirements.txt` if changes are needed.
To zip the entire bundle, run: `cd <--folder name-->`, then `zip -rq ../deployment_V1.zip . && echo "Zipping completed!"`.
