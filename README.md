# Admera Take Home Assessment

The following is a take home assesment to review your skills with designing and implementing solutions with code.
The estimated times for each problem are for reference and are not relevant to the assessment's overall grading.
You will have 1 week to complete this assessment prior and can spend as much as needed to complete the assessment within that time frame.
You will go over your solutions during the interview.

The solutions will be reviewed for:
- Completion
    - Does the solution work?
    - Does the soltuon work for basic and edge cases?
- Design
     - Is the design of the solution optimal for the problem?
     - Are there justifications for the design choices made?
- Code quality
    - Is the code up to common development standards?

You may complete the following assessment in any programming language you like.
However, you must implement each solution with only default, basic data structures.
No external libraries or modules are allowed.

# Problem A (estimated time 1 hour)

1. Implement a Binary Search Tree (BST)
2. Create a function that convert can convert the following list to a BST
    - [5, 10, 12, 6, 100000, 9, 75]
3. Create a function that can convert the BST back into a list
    - The resulting list's order does not matter

# Problem B (estmated time 3 hours)

## Background

You are a programmer working for a renowned genetics company. The company's main service is providing NGS to clients, where clients send biological samples to the company and the company sends back sequencing data.

The demand for the company's NGS service is growing rapidly and prioritizing projects has become difficult.
Until now, the NGS team in the lab has been sequencing samples first come first serve. As in, samples are sequenced in the order the lab receives them. However, this is not efficient. Some samples that arrive sooner may have a delivery date that's way into the future. Other samples received after, may be due incredibly soon.
The NGS team and project management have attempted to combat this but frequently communicating over email.
However, with the large sample volume this form of communication has become infeasible.
To combat this, the company has asked its team of programmers to automate the organizing and prioritizing of client samples.

The lab has been gracious enough to provide a basic visualization of the lab's workflow.


sample (direction 1) --> sample (direction 2 FOR DIFFERENT SERVICE) --> PQ step in middle
--> different service is to test future proofing


## Queston

You're job is to develop a Priority Queue that will automatically assign a priority level to incoming samples before they reach the lab.
Lab scientists will use the assigned priority level to decide which samples to sequence first.

There are two types of samples and each have different turnover rates.
Turnover starts the day a sample is received by the company.

Types:
- Regular Sample
    - Sequencing data must be delivered within 14 days
- Expedited Sample
    - Clients pay extra for sped up services
    - Sequencing data must be delivered within 7 days

Each sample will have the following information
1. The day the sample was received by the company
2. Whether the sample is a regular or expedited sample

If a sample is delayed, as in by the time the lab receives a sample it has already missed its expected delivery date, it has 3 days to be delivered.

Priority should be determined by how many days are left until its expected delivery date.
Feel free to use the provided test data file pq_test_data.txt.
For testing, assume the current date is 07/18/2022.

Once lab receives a sample it takes a full day for data to be delivered.