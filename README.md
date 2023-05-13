# Railroad Routes Project

This is a project that implements a solution for the railroad routes problem. The problem is to provide information about the routes between different towns on a one-way railroad network. The information includes:

- The distance along a given route
- The number of different routes between two towns
- The shortest route between two towns
- The project uses Python as the programming language and unittest module as the testing framework. The input data is stored in a text file that follows a specific format. The output is printed to the console.


## Setup

Clone the project

```bash
  git clone https://github.com/tobitotaku/railroad-project.git
```

Go to the project directory

```bash
  cd my-project
```

## How to run
To run the project, you need to have Python 3.11+. Then, you can clone this repository and navigate to the project directory. To run the tests, use the command:

```bash
  python test.py
```

To run the main program, use the command:

```bash
  python example.py
```

input.txt is the name of the file that contains the input data. You can use the provided sample file or create your own following the same format.

Input format
The input file should contain one or more lines of text. Each line represents a route between two towns and its distance. For example, the line:

```txt
AB5
```

means that there is a route from town A to town B with a distance of 5. The towns are named using single letters from A to Z. The distance is a positive integer.

The input file should not contain any empty lines or invalid characters. The order of the lines does not matter.



## Output

The output consists of several lines of text, each answering a specific question about the routes. The questions are:

 - What is the distance of the route A-D?
 - What is the distance of the route A-B-C?
 - What is the distance of the route A-D-C?
 - What is the distance of the route A-E-B-C-D?
 - What is the distance of the route A-E-D?
 - How many routes are there from C to C with a maximum of 3 stops?
 - How many routes are there from A to C with exactly 4 stops?
 - What is the length of the shortest route from A to C?
 - What is the length of the shortest route from B to B?
 - How many different routes are there from C to C with a distance of less than 30?

For each question, the output should print either:

The answer as a number, or
The message NO SUCH ROUTE if there is no such route that satisfies the question.
For example, using the sample input file, the output should be:

- Output #1: 9
- Output #2: 5
- Output #3: 13
- Output #4: 22
- Output #5: NO SUCH ROUTE
- Output #6: 2
- Output #7: 3
- Output #8: 9
- Output #9: 9
- Output #10: 7
