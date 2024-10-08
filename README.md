
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
 \end{pmatrix} 
```

### [Jacobi method](https://en.wikipedia.org/wiki/Jacobi_method)

Jacobi method is based on the *Contraction mapping theorem*. That is why there are some conditions without which the iterative sequence won't converge (diagonal dominance). The $\boldsymbol{x}^j$ are calculated separately, so the process can be paralleled.

### [Seidel method](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)

Seidel's method is a modification of Jacobi, in which the calculated $\boldsymbol{x}^{1}, \cdots, \boldsymbol{x}^{j}$ are being pasted in $\boldsymbol{x}^{j+1}$ *before the next iteration*.

```math
    \begin{cases}
      x_1^{j+1} = c_{12}x_2^j + c_{13}x_3^j + \cdots + c_{1n}x_n^j + d_1 \\
      x_2^{j+1} = c_{21}x_1^{j+1} + c_{23}x_3^j + \cdots + c_{2n}x_n^j + d_2 \\
      \cdots \\
      x_n^{j+1} = c_{n1}x_1^{j+1} + c_{n2}x_2^{j+1} + \cdots + c_{n(n-1)}x_{n-1}^{j+1} + d_n 
    \end{cases}
```
