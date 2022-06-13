# CI/CD - An Overview
CI/CD -> Continuous Integration and Continous Delivery
Development methodology prevalent in the DevOps space. 

# Continuous Integration
### Sample problem
Working on an application, and when merging, many conflicts occur
**Continuous Integration eliminates this problem**
* Continuously merge changes with the main branch of the application
    * Keep size of changes very low
    * Keep everyone up-to-date
* Developers are expected to performed extensive (usually automated) testing on code before merging to main
* CI Process provides a number of benefits, as every commit allows system to run many tasks
* May occasionally need approvalsd to enable pipeline to continue

### Example CI Pipeline Tasks
* Code Compilation
* Unit Test Execution
* Static code analysis
* Integrating testing
* Packaging and versioning
* Publishing version package to Docker Hub
Not all commits need to trigger all of the CI Pipeline

# CI/CD Benefits
* Integration with Agile Methodologies
    * Every commit is a working version of software
* Shorter Mean Time To Resolution
    * Changes are smaller and easier to troubleshoot
* Automated Deploment
    * Can use blue-green or other strategies, where one set of users gets one version, and another gets another version
    * Live testing of new features before global roll-out
* Less Disruptive Feature Releases
    * Small chunks always have deployable artifacts
    * Present users with small changes
* Improve Quality
    * Less chance of accruing technical debt
    * More throughly tested before wide-scale adoption
* Improved Time to Market
    * Features rolled out individually, and can be offered quicker 

# Jenkins Demo
Fundamental unit - the job
## Jenkins Jobs
**Can do all sorts of things (Examples)**
* Retrieve code from a repository
* Build an application using a script
* Package an application and run it on a server
## Demo
**Goal - retrieve a version from github and run a build script**
1. Log into Jenkins interface
2. Click 'create new jobs' link
3. Enter a name, and then select 'freestyle project', and then click 'OK'
4. Scroll to Source Code Management, select git, and enter a Github Repo URL
5. Scroll down to build and click 'add build step'
6. Choose 'execute shell'
7. Choose a shell scipt that is located in your repo, and then click 'save'
8. Use Build Trigger to run immediately after another job

**Goal - build a Jenkins Pipeline**
1. Log into Jenkins interface
2. Click 'create new jobs' link
3. Click 'pipeline'
4. Determine desired build triggers
5. Determine desired scripts to run
``` javascript
    node {
       stage('Preparation') {
           catchError(buildResult: 'SUCCESS') {
              sh 'sudo docker stop runningsample'
              sh 'sudo docker rm runningsample'
           }
       }
       stage('Build') {
           build ‘BuildAppJob’
       }
       stage('Results') {
           build ‘TestAppJob’
       }
    }
```
* First, execute the pipeline on a single node
* Three stages, Preparation, build, and Results
    * If one stage fails, the pipeline stops
* Use preparation to stop and remove the container  if it's already running
* Use build stage to run BuildAppJob
* Use Testing to run TestappJon
6. 

