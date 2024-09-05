
# Computational mathematics

The repository contains some algorithms which can be applied to a wide range of computational problems. The top ones are often simpler and easier to code as the bottom ones are more complex, but can work better. Almost all the code is written in python, but can be easily translated to other programming languages.

## Systems of linear equations

One of the most popular problems is linear system solving. There are several methods that can be used (with certain reservations).
Let $A\boldsymbol{x} = \boldsymbol{b}$ be a square system of n linear equations, where:

```math
A_{n,n} = 
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{n,1} & a_{n,2} & \cdots & a_{n,n} 
 \end{pmatrix}, \quad

\boldsymbol{x} = 
 \begin{pmatrix}
  x_{1}\\
  x_{2}\\
  \vdots\\
  x_{n} 
 \end{pmatrix}, \quad

 \boldsymbol{b} = 
 \begin{pmatrix}
  b_{1}\\
  b_{2}\\
  \vdots\\
  b_{n} 
 \end{pmatrix}, \quad
```

List of methods:

- [x] Jacobi method
- [ ] Seidel method

### Jacobi method

Jacobi method is based on the *Contraction mapping theorem*. That is why there are some conditions without which the iterative sequence won't converge.

The method works if:

- cond1
- cond2
- ...
