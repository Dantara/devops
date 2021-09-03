## CI best practices:

* Take a ‘security first approach’
* Assess your organization’s readiness to utilize a microservices architecture
* Build only once
* Use on-demand testing environments
* Minimize operations: smaller size and avoid wasting time on unnecessary things
* Don't store passwords in the code
* Use job dependency
* Try to avoid script injection attacks
* Consider not to use self-hosted runners in public repositories
* Declare environment variables close to their usage
* Cache installed tools and dependencies
* Split work between phases
* Use job filters on branch names and tags
* Use a custom base image with all necessary tools installed
* When using third-party operations, bind them to the commit SHA so that they will not be maliciously changed

## Jenkins best practices:

* Use the docker agent to run jobs in it
* Correctly set the credentials of external services such as GitHub to achieve efficient access
