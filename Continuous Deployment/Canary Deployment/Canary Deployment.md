Canary deployments are a type of segmented deployment. You deploy a small part of your application (called the canary) with the rest of the application following later. 

What makes a canary deployment different is you test your canary with live production traffic. With canary deployments in CodeDeploy, traffic is shifted in two increments. 
- The first shifts some traffic to the canary.
- The next shifts all traffic to the new application at the end of the selected interval.

You design the application to run the canary tests during the interval and review alarms based on technical or business metrics. If the results meet the acceptable criteria, continue with the deployment or else rollback gracefully.

The following example demonstrates a simple version of a serverless application using CodeDeploy to gradually shift customers to your newly-deployed version of the Lambda function:

```sh
Resources:
 MyLambdaFunction:
   Type: AWS::Serverless::Function
   Properties:
     Handler: index.handler
     Runtime: nodejs12.x
     CodeUri: s3://bucket/code.zip

     AutoPublishAlias: live

     DeploymentPreference:
       Type: Canary10Percent10Minutes 
       Alarms:
         # A list of alarms that you want to monitor
         - !Ref AliasErrorMetricGreaterThanZeroAlarm
         - !Ref LatestVersionErrorMetricGreaterThanZeroAlarm
       Hooks:
         # Validation Lambda functions that are run before & after traffic shifting
         PreTraffic: !Ref PreTrafficLambdaFunction
         PostTraffic: !Ref PostTrafficLambdaFunction
```

