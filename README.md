1.Create a local `<--folder name-->` of the project.

2.Create a `module` folder that will contain all the helper functions.

3. **Imp**: 
** A `__init__.py` must be initialized in order to use the functions from the `module` folder in other parts of the project.**

4. Create a `dependencies` folder which will contain all the packages required for running the program successfully.

5. Use `pipreqs .` to generate a `requirements.txt` if it is not already initialized.

6. Use `pipreqs --force` to update `requirements.txt` if changes are needed.

7. To zip the entire bundle, run:
- `cd <--folder name-->`
- `zip -rq ../deployment_V1.zip . && echo "Zipping completed!"`
