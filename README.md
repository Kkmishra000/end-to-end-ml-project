# end-to-end-ml-project

## Workflows


1. Update config.yaml    # artifacts , model save path, data path 
2. Update schema.yaml    # how data looks like - column names and data type
3. Update params.yaml    # epochs, learning rate
4. Update the entity     # yaml to python object 
5. Update the configuration manager in src config                                          - #Read YAML files and convert them into entities.Bridge between configs and code.

6. Update the components # write logic for preprocessing,training,evaluation
7. Update the pipeline    # connects all components - data--train--evaluate
8. Update the main.py   #start pipe line from command line
9. Update the app.py  #web app for prediction



