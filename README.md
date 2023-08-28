# Amazon-Internship-Test

Proof of Concept script created as a solution to one of the Amazon Internship Tests

# This is the challenge:

One of Amazon's offices has recently received n projects, each of which will be assigned to one of the n Amazon developers. The project assignment should satisfy certain criteria.\
You are given n projects with their respective difficulties in the form of an array of integers, difficulties[n], and the skills of n developers as an array of integers, skills[n]. A hypothetical parameter called the mod-efficiency of a project is defined as the sum of the difficulty of the project "i" and the skill of developer "j" to whom the project is assigned, modulo n. Mathematically, mod-efficiency[i] = ( difficulties[i] + skills[j] ) % n where % is the modulo operator.\
A project can be assigned to any developer. Find the assignment mapping from projects to developers such that the resulting mod-efficiency array is lexicographically minimum. Return the final mod-efficiency array.\
An array c1 is lexicographically smaller than an array c2 if c1[i] < c2[i] for the lowest index i where c1[i] ≠ c2[i].

Example:\
For n = 3, difficulties = [0, 1, 2] and skills = [2, 1, 0], the operations leading to the optimal solution are:

Assign difficulties[0] to skills[2].\
Assign difficulties[1] to skills[0].\
Assign difficulties[2] to skills[1].

The lexicographically minimum mod-efficiency array is [(0 + 0) % 3, (1 + 2) % 3, (2 + 1) % 3] = [0, 0, 0].

- Function Description:

getMinModEfficiency has the following parameter(s):\
int difficulties[n]: the difficulties of each project\
int skills[n]: the skills of each Amazon developer

Returns\
int[n]: the lexicographically minimum array

Constraints:\
1 ≤ n ≤ 2 · 105\
0 ≤ difficulties[i], skills[i] < n

Input Format For Custom Testing:\
The first line contains an integer, n, the number of elements in difficulties.\
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, difficulties[i].\
The first line contains an integer, n, the number of elements in skills.\
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, skills[i].

- Sample Case 0:\
  Sample Input For Custom Testing:\
  → n = 3\
  → difficulties = [0, 1, 1]

→ n = 3\
→ skills = [0, 1, 0]

Sample Output:\
0\
1\
2

Explanation:

The operations leading to the optimal solution are:

Assign difficulties[0] to skills[0].\
Assign difficulties[1] to skills[2].\
Assign difficulties[2] to skills[1].

mod-efficiency is [(0 + 0) % 3, (1 + 0) % 3, (1 + 1) % 3] = [0, 1, 2]

- Sample Case 1:\
  Sample Input For Custom Testing:\
  → n = 4\
  → difficulties = [0, 1, 2, 1]

→ n = 4\
→ skills = [1, 3, 2, 3]

Sample Output:\
1\
0\
0\
0

Explanation:

The operations leading to the optimal solution are:

Assign difficulties[0] to skills[0].\
Assign difficulties[1] to skills[1].\
Assign difficulties[2] to skills[2].\
Assign difficulties[3] to skills[3].

mod-efficiency is [(0 + 1) % 4, (1 + 3) % 4, (2 + 2) % 4, (1 + 3) % 4] = [1, 0, 0, 0]
