When using CodeDeploy, there are two types of deployments available to you: in-place and blue/green.
## In place deployment
The application on each instance is stopped, the latest application revision is installed, and the new version of the application is started and validated. Only deployments that use the Amazon EC2 or on-premises compute platform can use in-place deployments.

## Blue/green deployment
A blue/green deployment is used to update your applications while minimizing interruptions caused by the changes of a new application version. CodeDeploy provisions your new application version alongside the old version before rerouting your production traffic. This means during deployment, you’ll have two versions of your application running at the same time.

All Lambda and Amazon ECS deployments are blue/green. An Amazon EC2 or on-premises deployment can be in-place or blue/green. 

Blue/green deployments offer a number of advantages over in-place deployments:
- Testing on the green environment without disrupting the blue environment
- Switching to the green environment involves no downtime. It only requires the redirecting of user traffic
- Rolling back from the green environment to the blue environment in the event of a problem is easy. You can redirect traffic to the blue environment without having to rebuild it.

