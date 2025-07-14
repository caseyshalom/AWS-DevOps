There are two methodologies used in software development projects: 
- Test-driven development (TDD) and Behavior-driven development (BDD).

A benefit of both TDD and BDD is that errors in requirements are caught early, helping development teams and lowering overall cost. Select each tab to learn why you would use one versus the other.

TDD is a software development process that relies on the repetition of very short development cycles. TDD development encourages simple designs and inspires confidence in the code. The process takes requirements and turns them into test cases after which code is written or improved so that the test cases pass.

1. Start with writing the test first for every new feature added to the project. Use cases and user stories can help the developer understand the requirements.
2. Run the new test to see if it fails so the developer can verify the test harness is working correctly. The test should fail the first time it’s run.
3. Write the code that will cause the test to pass.
4. Run the tests and verify that the new code passes.
5. Refactor the code, remove duplication, and clean up old code.
6. Repeat by starting with a new test cycle.


BDD is an agile software development process that encourages collaboration among developers, quality assurance, and business partners. It encourages teams to use conversations and concrete examples to formalize an understanding of how applications should behave. 

Behavior Driven Development is an extension of TDD that makes use of simple domain-specific scripting languages (DSL). These DSLs can be converted into tests. Some of the features of DSL are:

1. The behavior of a user is defined in simple English.
2. The English words are converted into automated scripts against functional code.
3. The development team writes code to pass the test case.
4. User behaviors are often scenario-based, for example:
- A given user visited the site
- A user clicked the Orders button
- A user accessed the Orders page

# Differences
- BDD focuses on the behavior of the application for the end-user.
- TDD focuses on the functionality.