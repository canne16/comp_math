
# Computational mathematics

The repository contains some algorithms which can be applied to a wide range of computational problems. The top ones are often simpler and easier to code as the bottom ones are more complex, but can work better. Almost all the code is written in python, but can be easily translated to other programming languages.

## Systems of linear equations

One of the most popular problems is linear system solving. There are several methods that can be used (with certain reservations).
Let $`A\textbf{x} = \textbf{b}` be a square system of n linear equations, where:
![matrix](https://wikimedia.org/api/rest_v1/media/math/render/svg/98608e9e95d5acad149813eca75c8108acec308a)

List of methods:

- [x] Jacobi method
- [ ] Seidel method

### Jacobi method

Jacobi method is based on the *Contraction mapping theorem*. That is why there are some conditions without which the iterative sequence won't converge.

The method works if:

- cond1
- cond2
- ...
