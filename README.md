# Admera Take Home Assessment

## Directions:

1. Clone this repository
2. Store your solution in your own Github repository

The following is a take home assesment to review your skills with designing and implementing solutions in code.
You will have 1 week to complete this assessment and can spend as long as needed to complete the assessment within that time frame. We will go over your solutions during the interview.

The solutions will be reviewed for:
- Completion
    - Does the solution work?
    - Does the soltuon work for basic and edge cases?
- Design
     - Is the design of the solution optimal for the problem?
     - Are there justifications for the design choices made?
- Code quality
    - Is the code up to common development standards?

You may complete the following assessment in any programming language you'd like.
However, you may not use any libraries or third party modules that trivialize the problem.

For example, using the heapq module in python3 for Problem A is not allowed.

# Problem A
1. Design a Binary Heap
2. Using the design from #1, implement a Min Heap
3. Using the design from #1, implement a Max Heap

# Problem B

Review the Python3 code in groceries.py
The code will be used to keep track of and calculate the prices of groceries for users for a grocery delivery app.
However there's a bug and the prices for the groceries are not accurate.

1. Identify the bug in the code.
2. Write a fix.
3. Be ready to explain the bug.

# Problem C

## Background

You are a programmer working for a renowned genetics company. The company's main service is providing NGS to clients, where clients send biological samples to the company and the company sends back sequencing data.

The demand for the company's NGS service is growing rapidly and prioritizing projects has become difficult.
Until now, the NGS team in the lab has been sequencing samples first come first serve. As in, samples are sequenced in the order the lab receives them. However, this is not efficient. Some samples that arrive sooner may have a delivery date that's way into the future. Other samples may be due immediately after lab receives them.

The NGS team and project management have attempted to remedy this by frequently communicating over email.
However, with the large sample volume this form of communication has become infeasible.
To combat this, the company has asked its team of programmers to automate the organizing and prioritizing of client samples.

The lab has also expressed if this is successful, they would like to apply this priority program to other services the lab provides. Some services also use samples, others receive different inputs from customers.

## Question

You're job is to develop a Priority Queue that will assign a priority level to given samples and organize them based on this priority.
The notification program developed by other members of the team will use this Priority Queue to decide when to send samples to the lab for sequencing.

There are two types of samples and each have different turnover rates.
Turnover starts the day a sample is received by the company.

Types:
- Regular Sample
    - Sequencing data must be delivered within 14 days
- Expedited Sample
    - Clients pay extra for faster services
    - Sequencing data must be delivered within 7 days

Each sample will have the following information
1. A sample id
2. The day the sample was received by the company
3. Whether the sample is a regular or expedited sample

If a sample is delayed, as in by the time the lab receives a sample it has already missed its expected delivery date, it has 3 days to be delivered.

Priority should be determined by how many days are left until its expected delivery date.

Sequencing data will be delivered the day after lab receives the sample.

Feel free to use the provided test data file 'pq_test_data.txt'.

Assume the current date is 07/18/2022.