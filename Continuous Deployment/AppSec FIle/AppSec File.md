# An AppSpec file is a YAML or JSON file used in CodeDeploy.
The AppSpec file is used to manage each deployment as a series of lifecycle event hooks, which are defined in the file. The structure of the AppSpec file can differ depending on the compute platform you choose. 

## Amazon ECS
```sh
version: 0.0    
resources:
    ecs-service-spesifications
hooks:
    deployment-lifecycle-event-mappings
```

## Lambda
```sh
version: 0.0
resources:
    lambda-function-spesifications
hooks:
    deployment-lifecycle-event-mappings
```

## Amazon EC2 or on-premises
```sh
version: 0.0
os: operating-system-name
files:
    source-destination-file-mappings
permissions:
    permissions-spesifications
hooks:
    deployment-lifecycle-event-mappings
```