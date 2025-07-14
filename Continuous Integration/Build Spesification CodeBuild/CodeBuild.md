CodeBuild needs a build project to define how to gather application dependencies, run tests, and build the output to be used in preparing the deployment.

A project includes information such as:
- Source code location
- Build environment to use
- Build commands to run
- Storage of build output

A build environment is the combination of operating system, programming language runtime, and tools used by CodeBuild to run a build. You use buildspec.yml file to specify build commands. The buildspec file is a YAML Ain't Markup Language (YAML)-formatted file used by CodeBuild that includes a collection of build commands and related settings that CodeBuild uses to run a build. You can include a buildspec as part of the source code or define a buildspec when you create a build project.

When included as part of the source code, the buildspec file is named buildspec.yml and is located in the root of the source directory. It can be overridden with create-project or update-project commands.

## Version
1. The versions of the buildspec standard being used are 0.1 and 0.2 (recommended). 
2. Several additions and changes were made to version 0.2.
- 0.2 CodeBuild changes the build environment to run all commands in the same instance of the default shell in the build environment.
- environment_variables changed to env in 0.2.
- plaintext was renamed to variables in 0.2.
- type property for artifacts was deprecated in 0.2.

## Phases
Define the build phases during which you can instruct CodeBuild to run commands.

1. Install: Commands, if any, that CodeBuild runs during installation 
- Runtime versions are supported with Ubuntu standard images or Amazon Linux 2 standard. Other runtimes are supported in the runtimes versions of the buildspec file. For example:
```sh
 phases:
    install:
        runtime-versions:
            java: ocorretto8
            python: 3.x
```

2. Pre-Build: Commands to run before the build
3. Build: Commands to run during the build
4. Post-build: Commands to run after the build
5. Finally blocks: These can be called after each section’s command blocks run even if a command in the command block fails.

## Artifacts
1. Artifacts represent a set of build artifacts that CodeBuild uploads to the output bucket
2. discard-paths specifies if the build artifact directories are flattened in the output
    -No: The build artifacts are output with their directory structure intact.
    -Yes: The build artifacts are placed in the same directory.
3. base-directory represents one or more top-level directories relative to the original build location. CodeBuild uses this to determine which files and subdirectories to include in the build output artifact.

## Cache
1. Location where you can cache dependencies for reuse between projects
2. Can be an S3 location or local
3. Improves the build time by reducing the amount of dependencies downloaded
4. Can be invalidated


## The following is an example of the 'buildspec.yml' file, which contains:
1. Custom environment variables with the key of JAVA_HOME set
2. Custom environmental variable for the Systems Manager Parameter store stored as LOGIN_PASSWORD
3. Update to the build environment where Maven is installed
4. Docker login password
5. Software build phase
6. Report group that generates reports during the build
7. Location of where to upload the build files to an output location
8. Location of cached dependencies on the local host