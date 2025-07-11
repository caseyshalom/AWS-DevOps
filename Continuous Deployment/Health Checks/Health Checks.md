Health checks are tests performed on resources. These resources might be your application, compute resources like Amazon Elastic Cloud Compute (Amazon EC2) instances, and even your Elastic Load Balancers.

The results can determine if a deployment was successful or if an application is working as intended. Select the + symbol next to each category to learn about each one.

## Liveness Check
Liveness checks test the basic connectivity to a service and the presence of a server process. They are often performed by a load balancer or external monitoring agent, and they are unaware of the details about how an application works. Liveness checks tend to be included with the service and do not require an application author to implement anything. 

Some examples of liveness checks used at Amazon include the following:

- Tests that confirm a server is listening on its expected port and accepting new TCP connections
- Tests that perform basic HTTP requests and make sure the server responds with a 200 status code
- Status checks for Amazon EC2 that test for basic things necessary for any system to operate, such as network reachability

## Local Health Check
Local health checks go further than liveness checks to verify that the application is likely to be able to function. These health check test resources are not shared with the server’s peers. Therefore, they are unlikely to fail on many servers in the fleet simultaneously. 

Some examples of situations local health checks can identify are: 

- Inability to write to or read from disk: It might be tempting to believe a stateless service doesn't require a writable disk. Many services tend to use their disks for such things as monitoring, logging, and publishing asynchronous metering data.
- Critical processes crashing or breaking: Some services take requests using an on-server proxy (similar to NGINX) and perform their business logic in another server process. A liveness check might only test whether the proxy process is running. A local health check process might pass through from the proxy to the application to check that both are running and answering requests correctly. 
- Missing support processes: Hosts missing their monitoring daemons might leave operators unaware of the health of their services. Other support processes push metering and billing usage records or receive credential updates. Servers with broken support processes put functionality at risk in subtle, difficult-to-detect ways.

## Dependency Health Check
Dependency health checks thoroughly inspect the ability of an application to interact with its adjacent systems. These checks ideally catch problems local to the server, such as expired credentials, that are preventing it from interacting with a dependency. They can also have false positives when there are problems with the dependency itself. Because of those false positives, we must be careful about how we react to dependency health check failures. Dependency health checks might test for the following:

- A process might asynchronously look for updates to metadata or configuration but the update mechanism might be broken on a server. The server can become significantly out of sync with its peers. The server might misbehave in an unpredictable and untested way. When a server doesn’t see an update, it doesn’t know whether the update mechanism is broken or the central update system has stopped publishing. 
- Inability to communicate with peer servers or dependencies: Strange network behavior can affect the ability of a subset of servers in a fleet to talk to dependencies. This behavior might occur without affecting the ability for traffic to be sent to that server. Software issues, such as deadlocks or bugs in connection pools, can also hinder network communication.
- Other unusual software bugs that require a process bounce: Deadlocks, memory leaks, or state corruption bugs can make a server spew errors.

Health checks can be implemented in the deployment of your application in several different ways. One is with CodeDeploy and the help of your application specification (AppSpec) file. 

We will cover the AppSpec file in an upcoming lesson but the file indicates several different stages of your application’s deployment. 