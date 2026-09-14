# Artificial Intelligence Agent For Solving Raven's Progressive Matrices

### What Are Raven's Progressive Matrices?
The Raven's Progressive Matrices test (RPM) is a commonly used intelligence test based on visual reasoning. RPMs involve 2x2 or 3x3 matrices with each cell containing different shapes and relationships.  The cell that completes the pattern has to be chosen from a list of six or eight possible solution cells.  While these problems are purely visual, they provide a good test of general intelligence. (The correct answer below is 4)

![problem_5.png](img/problem.png)

## How Does The Agent Work?
The agent was designed to mimic human reasoning by using multiple different approaches to problem solving, similar to the way people solve RPMs.  The agent relies on a three layered approach to finding solutions.  The first layer searches for obvious patterns where the agent can propose an answer that can be explicitly searched for in the list of possible solution cells.  The second layer provides a filter for the possible solution cells, and removes cells that violate the observed patterns.  The third layer generates attributes for a proposed solution and analyzes the remaining solutions for similarity to the proposed solution attributes, and returns the solution with the highest similarity score.  Each layer is able to help in a way that the other layers cannot, and when combined, can solve problems with a high degree of accuracy.

![problem_5.png](img/layers.png)

## How Accurate Is The Agent?
On 2x2 problems, the agent sovled 11/12 of the basic problems, and 2/8 of the challenge problems.  For a set of problems it had never seen before, the agent scored 17/20.

| Problem Set   | Results       | %     |
| ------------- |:-------------:| -----:|
| Basic Set     |      11/12    | 91.7% |
| Challenge Set |       2/8     |  25%  |
| Unseen Set    |      17/20    |  85%  |

## Using The Agent

To use the agent, you must have Python and the image processing library Pillow installed on your local computer.

### Installation
Find the directory where you wat to install the agent, and run `git clone https://github.com/teldridge11/RPM-AI-Agent.git`

### Testing The Agent
To test the agent against the included problems, `cd` into the Agent directory and run `python Test.py`.  The results will be output into ProblemResults.csv.
