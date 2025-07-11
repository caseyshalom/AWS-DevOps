CodeGuru Reviewer checks for:
- Concurrency issues
- Potential race conditions
- Unsanitized or malicious inputs
- Resource leaks
- Inappropriate handling of sensitive data such as credentials that can lead to injection attacks or denial of service

It also detects race conditions and deadlocks in concurrent code, and when resources are incorrectly closed, which could create latency issues and outages.

CodeGuru Reviewer suggests best practices based on coding standards learned from major open-source projects and the Amazon code base.

CodeGuru Reviewer can also analyze source code and build artifacts of your Java application to provide code and security recommendations. CodeGuru Reviewer does not check for syntax errors or code styling. CodeGuru Reviewer is introduced after the code is unit tested and ready for review.

## Security Detector
CodeGuru Reviewer offers a separate review capability to perform security analysis in addition to the code reviews previously mentioned. The security detector in CodeGuru Reviewer analyzes Java code and build artifacts to detect how data flows through the different ways the code can be run. It discovers potential issues that involve sequences of operations that might span the application and involve multiple methods and classes.

CodeGuru Reviewer can help with the following types of security issues and best practices:

- Amazon Web Services (AWS) API security best practices when using AWS service APIs
- Java crypto library best practices to help check common Java cryptography libraries and ensure that they are initialized and called correctly
- Secure web applications to help check web-application-related security issues
- Sensitive information leak detection to help with compliance issues
- AWS security best practices to bring internal security expertise to your use cases

# Workflow
To use CodeGuru Reviewer, you first associate your AWS CodeCommit, GitHub, GitHub Enterprise, or Bitbucket repositories to allow Amazon CodeGuru to read your code. CodeGuru Reviewer needs read-only access to your code to provide recommendations.