## Lifecycle hooks are areas where you can specify Lambda functions or local scripts to run tests and verify during the deployment of your application.

Some tests might be as simple as checking a dependency before an application is installed using the BeforeInstall hook. Some might be as complex as checking your application’s output before allowing production traffic to flow through using the BeforeAllowTraffic hook. 

These Lambda functions or local scripts can also be used to gather traffic metrics. This is a sample AppSpec file for an Amazon ECS deployment.
```sh
version: 0.0
Resources:
  - TargetService:
      Type: AWS::ECS::Service
      Properties:
        TaskDefinition: "arn:aws:ecs:us-east-1:111222333444:task-definition/my-task-definition-family-name:1"
        LoadBalancerInfo:
          ContainerName: "SampleApplicationName"
          ContainerPort: 80
# Optional properties
        PlatformVersion: "LATEST"
        NetworkConfiguration:
          AwsvpcConfiguration:
            Subnets: ["subnet-1234abcd","subnet-5678abcd"]
            SecurityGroups: ["sg-12345678"]
            AssignPublicIp: "ENABLED"
Hooks:
  - BeforeInstall: "LambdaFunctionToValidateBeforeInstall"
  - AfterInstall: "LambdaFunctionToValidateAfterTraffic"
  - AfterAllowTestTraffic: "LambdaFunctionToValidateAfterTestTrafficStarts"
  - BeforeAllowTraffic: "LambdaFunctionToValidateBeforeAllowingProductionTraffic"
  - AfterAllowTraffic: "LambdaFunctionToValidateAfterAllowingProductionTraffic"
```

When using Lambda functions to perform tests on your environment, the server must be notified of the deployment ID and the lifecycle event hook execution ID using the putLifecycleEventHookExecutionStatus command. With this, your Lambda function has the information it needs to report back the results.

## Sample Lambda function in Node.js
```sh
'use strict';
 
 const AWS = require('aws-sdk');
 const codedeploy = new AWS.CodeDeploy({apiVersion: '2014-10-06'});
 
 exports.handler = (event, context, callback) => {
 
 	console.log("Entering AfterAllowTestTraffic hook.");
 	
 	// Read the DeploymentId and LifecycleEventHookExecutionId from the event payload
  var deploymentId = event.DeploymentId;
 	var lifecycleEventHookExecutionId = event.LifecycleEventHookExecutionId;
 	var validationTestResult = "Failed";
 	
 	// Perform AfterAllowTestTraffic validation tests here. Set the test result 
 	// to "Succeeded" for this tutorial.
 	console.log("This is where AfterAllowTestTraffic validation tests happen.")
 	validationTestResult = "Succeeded";
 	
 	// Complete the AfterAllowTestTraffic hook by sending CodeDeploy the validation status
 	var params = {
 		deploymentId: deploymentId,
 		lifecycleEventHookExecutionId: lifecycleEventHookExecutionId,
 		status: validationTestResult // status can be 'Succeeded' or 'Failed'
 	};
 	
 	// Pass AWS CodeDeploy the prepared validation test results.
 	codedeploy.putLifecycleEventHookExecutionStatus(params, function(err, data) {
 		if (err) {
 			// Validation failed.
 			console.log('AfterAllowTestTraffic validation tests failed');
 			console.log(err, err.stack);
 			callback("CodeDeploy Status update failed");
 		} else {
 			// Validation succeeded.
 			console.log("AfterAllowTestTraffic validation tests succeeded");
 			callback(null, "AfterAllowTestTraffic validation tests succeeded");
 		}
```

