
# 1 Linear Algebra

**Author**: Zhiyin Zhang

---

## 1.1 Introduction to Matrices

A **matrix** is a rectangular array of numbers arranged in rows and columns.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$

This is an $m \times n$ matrix.

For example, a $2 \times 3$ matrix:

$$
M= \begin{bmatrix}
60 & 98 & 42 \\ 170 & 16 & 14
\end{bmatrix}
$$

**Columns:**
- Carbs: 60, 70
- Fat: 98, 16
- Protein: 42, 14

**Rows:**
- Milk: 60, 98, 42
- Cereals: 170, 16, 14

### 1.1.1 Types of Matrices

1. **Square Matrix**: Number of rows = number of columns.

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$

2. **Zero Matrix**: All elements are zero.

$$
A = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
$$

3. **Identity Matrix**: Square matrix with ones on the diagonal.

$$
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

### 1.1.2 Matrix Operations

1. **Addition**: Only possible for matrices of the same size.

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix},
B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
$$

$$
A + B = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix}
$$

2. **Multiplication by Scalar**: Each element of the matrix is multiplied by a constant.

$$
2 \times \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 6 & 8 \end{bmatrix}
$$

3. **Matrix Multiplication**: Number of columns in the first matrix must equal the number of rows in the second.

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix},
B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
$$

$$
A \times B = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
$$

4. **Transpose**: Flip rows and columns.

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
$$

### 1.1.3 Matrix Multiplication Example

Let $A$ be a $2 \times 3$ matrix, and $B$ be a $3 \times 2$ matrix:

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}, \quad
B = \begin{bmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{bmatrix}
$$

Since the number of columns in $A$ (3) is equal to the number of rows in $B$ (3), we can multiply these matrices. The result will be a $2 \times 2$ matrix $C$, where each element of $C$ is calculated as:

$$
C = A \times B = \begin{bmatrix}
(1 \times 7 + 2 \times 9 + 3 \times 11) & (1 \times 8 + 2 \times 10 + 3 \times 12) \\
(4 \times 7 + 5 \times 9 + 6 \times 11) & (4 \times 8 + 5 \times 10 + 6 \times 12)
\end{bmatrix}
$$

Calculating each element:

$$
C = \begin{bmatrix}
7 + 18 + 33 & 8 + 20 + 36 \\
28 + 45 + 66 & 32 + 50 + 72
\end{bmatrix}
= \begin{bmatrix}
58 & 64 \\
139 & 154
\end{bmatrix}
$$

Thus, the product of matrices $A$ and $B$ is:

$$
C = \begin{bmatrix} 58 & 64 \\ 139 & 154 \end{bmatrix}
$$

---

## 1.2 Composition & Combination

### 1.2.1 Steps of Gaussian Elimination

1. **Form the augmented matrix**: Represent the system of linear equations as an augmented matrix.
2. **Forward elimination**: Select a pivot (nonzero leading coefficient) in the first column.
   - Use row operations to create zeros below the pivot.
   - Move to the next column and repeat for the remaining rows.
3. **Row echelon form**: Continue applying row operations until the matrix is in upper triangular form.
4. **Back-substitution**: Solve for the variables by starting from the last equation and working upwards.

### 1.2.2 Example

Consider the system of equations:

$$
\begin{aligned}
x + 2y + 3z &= 9 \\
2x + 3y + z &= 8 \\
3x + y + 2z &= 7
\end{aligned}
$$

The augmented matrix is:

$$
\begin{bmatrix}
1 & 2 & 3 & | & 9 \\
2 & 3 & 1 & | & 8 \\
3 & 1 & 2 & | & 7
\end{bmatrix}
$$

Applying Gaussian elimination, we perform row operations:

**Eliminate column 1:**
1. Second row: subtract the first row 2 times.
2. Third row: subtract the first row 3 times.

After forward elimination:

$$
\begin{bmatrix}
1 & 2 & 3 & | & 9 \\
0 & -1 & -5 & | & -10 \\
0 & -5 & -7 & | & -20
\end{bmatrix}
$$

**Eliminate column 2:**
- Third row: subtract the second row 5 times.

After forward elimination:

$$
\begin{bmatrix}
1 & 2 & 3 & | & 9 \\
0 & -1 & -5 & | & -10 \\
0 & 0 & 18 & | & 30
\end{bmatrix}
$$

From here, back-substitution can be used to solve for $x, y, z$.

$$
x = \frac{2}{3}, \quad y = \frac{5}{3}, \quad z = \frac{5}{3}
$$


---

# 2 Determinants & Inverses

## 2.1 Determinants

The determinant of a square matrix is a scalar value that can be computed from its elements. det(A)

For a $2 \times 2$ matrix:

$$
A = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The determinant is given by:

$$
\text{det}(A) = ad - bc
$$

For a $3 \times 3$ matrix:

$$
A = \begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

The determinant is calculated as:

$$
\text{det}(A) = a \begin{vmatrix} e & f \\ h & i \end{vmatrix} - b \begin{vmatrix} d & f \\ g & i \end{vmatrix} + c \begin{vmatrix} d & e \\ g & h \end{vmatrix}
$$

For larger matrices, the determinant can be computed recursively using cofactor expansion.

### 2.1.1 Properties of Determinants

1. **Multiplicative Property**: If $A$ and $B$ are square matrices of the same size, then:

$$
\text{det}(AB) = \text{det}(A) \cdot \text{det}(B)
$$

2. **Invertibility**: A matrix is invertible if and only if its determinant is non-zero. That is, a matrix $A$ is invertible if:

$$
\text{det}(A) \neq 0
$$

3. **Determinant of Transpose**: The determinant of the transpose of a matrix is the same as the determinant of the original matrix:

$$
\text{det}(A^T) = \text{det}(A)
$$

## 2.2 Matrix Inverses

A matrix $A$ is said to have an inverse, denoted as $A^{-1}$, **if and only if it is square and its determinant is non-zero.** The inverse of a matrix satisfies the following property:

$$
A \cdot A^{-1} = A^{-1} \cdot A = I
$$

Where $I$ is the identity matrix of the same size as $A$.

> **Note**: $A^{-1}$ does not exist if and only if $\det(A) = 0$.

**Proof:**

For a $1 \times 1$ matrix $A=(a)$:

$$
(a) ^ {-1} = (a ^ {-1}) = \left(\frac{1}{a}\right)
$$

$$
\Leftrightarrow \nexists (a)^{-1} \quad \text{iff} \quad a = 0
$$

For an $n \times n$ matrix $A$:

$$
A^{-1} = \frac{\text{something}}{\det(A)}
$$

$$
\Leftrightarrow \nexists A^{-1} \quad \text{iff} \quad \det(A) = 0
$$

For a $2 \times 2$ matrix:

$$
A = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The inverse of $A$, if it exists, is given by:

$$
A^{-1} = \frac{1}{\text{det}(A)} \begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
$$

Note that the determinant must be non-zero for the inverse to exist. If $\text{det}(A) = 0$, then the matrix is singular and does not have an inverse.

For larger matrices, the inverse can be computed using the adjoint method or Gauss-Jordan elimination.

---

# 3 Einstein Summation Convention

## 3.1 Introduction to Einstein Summation Convention

The Einstein Summation Convention is a notational simplification used in tensor and matrix operations. The fundamental idea is that when an index appears twice in an expression (once as a subscript and once as a superscript), it implies summation over that index without the need to explicitly write the summation symbol. This convention simplifies complex expressions and makes tensor operations more concise.

For example, the matrix product of two matrices $A$ and $B$ is represented as:

$$
C_{ij} = \sum_k A_{ik} B_{kj}
$$

Using Einstein's Summation Convention, the summation symbol can be omitted:

$$
C_{ij} = A_{ik} B_{kj}
$$

Here, the index $k$ is implicitly summed over.

## 3.2 Simplification of Matrix Operations Using Einstein's Summation Convention

In matrix and tensor operations, the Einstein Summation Convention simplifies the notation by automatically implying summation over repeated indices. This becomes especially useful when dealing with high-dimensional matrices or tensors. Without the convention, the same operation would require multiple summation symbols, which can be cumbersome for more complex expressions.

For instance, when dealing with higher-dimensional tensors, the summation convention eliminates the need to write out every summation explicitly:

$$
C_{ijk} = \sum_l \sum_m T_{il} S_{lm} U_{mj}
$$

By using Einstein's Summation Convention, this becomes:

$$
C_{ijk} = T_{il} S_{lm} U_{mj}
$$

This simplified notation is not only shorter but also more intuitive for physicists and mathematicians, particularly when dealing with complicated tensor equations.

## 3.3 Projection

The Einstein summation convention simplifies operations involving vectors and matrices by omitting summation symbols and using repeated indices. Projection allows us to express how components of a vector relate to other vectors (e.g., unit vectors or vectors along specific directions).

By applying projection, we can extract the component of a vector $r$ along another vector $s$.

$$
\text{Proj}_{s}(r) =  \frac{r \times s}{r \times r} \times s
$$

### 3.3.1 Removing Unrelated Components

When dealing with calculations involving multiple directions or vectors, projection helps to remove components that are not relevant to the direction of interest. For example, when adjusting vector **r**, subtracting the projection component along the direction of **s** ensures that only the components related to other directions are considered. This is especially useful when solving equations or optimization problems, such as **minimizing errors or adjusting weights.**

### 3.3.2 Projection Operation with Identity Matrix

The identity matrix $I$ represents a transformation that leaves the vector unchanged, while the projection matrix $I_{3j}$ is used to exclude components of the vector that are not aligned with a specific direction (e.g., $e^3$). This allows the vector's structure to be preserved and simplifies complex matrix operations.

## 3.4 Example Analysis

Let us analyze the following equation:

$$
\mathbf{r}_i' = \mathbf{r}_i - \frac{S_i [e^3]_j r_j}{S_3}
$$

This formula represents the adjustment of the vector $\mathbf{r}_i$ by subtracting a term related to the third component $r_3$. The adjustment is scaled by the factor $\frac{S_i}{S_3}$, and it is aligned with the unit vector $\mathbf{e_3}$ in the $z$-direction.

$$
\mathbf{r}_i' = \left( \mathbf{I}_{ij} - \frac{S_i [e_3]_j r_j}{S_3} \right) r_j
$$

This formula represents subtracting from the original vector $\mathbf{r}_i$ the quantity related to the $j$-th component and the $e_3$ direction. Specifically, it applies a correction to the vector, reducing or increasing the influence along the third direction (e.g., the $z$-axis).

This is often important when dealing with rotational or directional corrections in physical systems.

## 3.5 Applications in Physics

In physics, especially in *general relativity*, *fluid dynamics*, and *electromagnetism*, the Einstein Summation Convention is extensively used to simplify the notation for tensor operations. Tensors are used to describe physical quantities such as stress, energy, and momentum, and the summation convention makes the equations more compact and easier to manipulate.

# 4 Changing Basis

## 4.1 Projection Calculation

Imagine you are observing a vector, represented by a set of coordinates in a particular reference frame (say, your own frame of reference). Now, consider another frame of reference where the vector appears differently. This is the process of changing the basis. For example:

- You have a vector $\mathbf{v}$ in your frame.
- A vector $\mathbf{v'}$ in the pandas' frame, which has a different orientation.
- The vector $\mathbf{v'}$ in your frame can be represented by a linear combination of the new basis vectors.

Let us consider the following vector and bases:

$$
\mathbf{v} = \begin{bmatrix} 5 \\ -1 \end{bmatrix}, \quad
\mathbf{b_1} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad
\mathbf{b_2} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

To express $\mathbf{v}$ in the new coordinate system defined by $\mathbf{b_1}$ and $\mathbf{b_2}$, we need to compute the projection of $\mathbf{v}$ onto both $\mathbf{b_1}$ and $\mathbf{b_2}$.

1. The projection of a vector $\mathbf{v}$ onto a vector $\mathbf{b_1}$ is given by:

$$
\frac{\mathbf{v} \cdot \mathbf{b_1}}{\mathbf{b_1} } = \text{Magnitude of the projection of } \mathbf{v} \text{ on } \mathbf{b_1}.
$$

$$
\frac{\mathbf{b_1}}{|\mathbf{b_1}|} = \text{Unit vector in the direction of } \mathbf{b_1}.
$$

$$
\text{proj}_{\mathbf{b_1}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{b_1}}{\mathbf{b_1} \cdot \mathbf{b_1}} \mathbf{b_1}
$$

First, compute the dot products:

$$
\mathbf{v} \cdot \mathbf{b_1} = 5 \times 1 + (-1) \times 1 = 4
$$

$$
\mathbf{b_1} \cdot \mathbf{b_1} = 1^2 + 1^2 = 2
$$

Now compute the projection:

$$
\text{proj}_{\mathbf{b_1}}(\mathbf{v}) = \frac{4}{2} \mathbf{b_1} = 2 \times \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}
$$

1. Similarly, the projection of $\mathbf{v}$ onto $\mathbf{b_2}$ is:

$$
\text{proj}_{\mathbf{b_2}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{b_2}}{\mathbf{b_2} \cdot \mathbf{b_2}} \mathbf{b_2}
$$

Compute the dot products:

$$
\mathbf{v} \cdot \mathbf{b_2} = 5 \times 1 + (-1) \times (-1) = 6
$$

$$
\mathbf{b_2} \cdot \mathbf{b_2} = 1^2 + (-1)^2 = 2
$$

Now compute the projection:

$$
\text{proj}_{\mathbf{b_2}}(\mathbf{v}) = \frac{6}{2} \mathbf{b_2} = 3 \times \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ -3 \end{bmatrix}
$$

### 4.1.1 New Coordinates

Now that we have the projections of $\mathbf{v}$ onto $\mathbf{b_1}$ and $\mathbf{b_2}$, we can write the vector $\mathbf{v}$ as a linear combination of the two basis vectors:

$$
\mathbf{v} = x \mathbf{b_1} + y \mathbf{b_2}
$$

Where $x$ and $y$ are the coefficients that we need to solve for. These coefficients are simply the projections we calculated earlier:

$$
\mathbf{v} = \begin{bmatrix} 2 \\ 2 \end{bmatrix} + \begin{bmatrix} 3 \\ -3 \end{bmatrix} = \begin{bmatrix} 5 \\ -1 \end{bmatrix}
$$

Thus, the new coordinates of $\mathbf{v}$ in the basis defined by $\mathbf{b_1}$ and $\mathbf{b_2}$ are:

$$
x = 2, \quad y = 3
$$

Therefore, the vector $\mathbf{v}$ can be expressed as:

$$
\mathbf{v} = 2 \mathbf{b_1} + 3 \mathbf{b_2}
$$

---

## 4.2 Orthogonal Matrices

A matrix $Q$ is said to be **orthogonal** if its rows and columns are orthonormal vectors. In other words, a matrix $Q$ is orthogonal if:

$$
Q^T Q = Q Q^T = I
$$

Where $Q^T$ is the transpose of $Q$, and $I$ is the identity matrix.

### 4.2.1 Properties of Orthogonal Matrices

1. **Determinant of Orthogonal Matrix**: The determinant of an orthogonal matrix is always either $+1$ or $-1$:

$$
\text{det}(Q) = \pm 1
$$

2. **Inverse of Orthogonal Matrix**: The inverse of an orthogonal matrix is equal to its transpose:

$$
Q^{-1} = Q^T
$$

3. **Preserving Lengths and Angles**: Orthogonal matrices preserve the Euclidean length of vectors and the angles between them.

For example, the following matrix is orthogonal:

$$
Q = \begin{bmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
-\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{bmatrix}
$$

We can verify that $Q^T Q = I$, which confirms that $Q$ is orthogonal.

---

## 4.3 Rotation Matrix

A two-dimensional rotation matrix that rotates a vector by an angle $\theta$ is given by:

$$
R(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
$$

When this matrix is multiplied by a vector $\mathbf{v} = \begin{bmatrix} x \\ y \end{bmatrix}$, it rotates the vector by $\theta$ degrees:

$$
\mathbf{v}' = R(\theta) \cdot \mathbf{v} = \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
$$

This results in:

$$
\mathbf{v}' = \begin{bmatrix}
x\cos\theta - y\sin\theta \\
x\sin\theta + y\cos\theta
\end{bmatrix}
$$

Thus, the vector $\mathbf{v}$ is rotated counterclockwise by $\theta$ radians. This matrix is an example of an orthogonal matrix.

---

# 5 Eigenvalues, Singular Values, and Applications

## 5.1 Eigenvalues & Singular Values

- **Singular Values**: Maximum action  
- **Eigenvalues**: Invariance action  

An eigenvalue is a scalar associated with a square matrix $\mathbf{A}$ that characterizes the action of the matrix on a vector $\mathbf{x}$. An eigenvector is **a non-zero vector that only changes in scale (not direction)** when the matrix is applied.

The eigenvalue problem asks for values $\lambda$ and non-zero vectors $\mathbf{x}$ that satisfy the equation:

$$
A \mathbf{x} = \lambda \mathbf{x}
$$

To find the eigenvalues, solve the characteristic equation:

$$
\det(A - \lambda I) = 0
$$

For example, given:

$$
A = \begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix}
$$

Solving the characteristic equation, we get:

$$
\lambda = 1 \quad \text{or} \quad \lambda = 3
$$

In sum, the process for calculating eigenvalues is as follows:

1. **Starting with the equation and expanding the determinant gives the quadratic equation:**

$$
\det(A - \lambda I) = 0
$$

$$
\lambda^2 - (a + d) \lambda + ad - bc = 0
$$

2. **Calculating $A - \lambda I$:**

$$
\det \begin{bmatrix}
A & b \\
c & d
\end{bmatrix} - \begin{bmatrix}
\lambda & 0 \\
0 & \lambda
\end{bmatrix} = 0
$$

   The next step is to subtract $\lambda$ from the top-left and bottom-right entries of the matrix. This can be written as:

$$
\det \begin{bmatrix}
A - \lambda & b \\
c & d - \lambda
\end{bmatrix} = 0
$$

3. **Next, consider the matrix equation:**

$$
(A - \lambda I) \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

   The result gives the eigenvectors $v_1, v_2$.

---
## Matrix Diagonalization
Given a symmetric matrix: $$
A = QSQ^T
$$ where: $$
A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}
$$ is a symmetric matrix. 

**1. Eigenvalue and Eigenvectors 

The eigenvalues and corresponding eigenvectors are: 
$$
\lambda_1 = 1, \quad v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$
$$
\lambda_2 = 3, \quad v_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$
- According to **Theorem 1**: 
 If $A$ is a symmetric matrix, then any two eigenvectors from different eigenspaces are orthogonal. 
 
 **Normalization of Eigenvectors**
To normalize a vector, we compute its length (or norm), which is given by:
$$
\| v \| = \sqrt{| v_1 |^2 + | v_2 |^2}
$$
For example, for the vector $v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$:
$$
\| v_1 \| = \sqrt{1^2 + 1^2} = \sqrt{2}
$$
 The normalized vectors are:
$$
q_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad q_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} -1 \\ 1 \end{bmatrix}
$$
 
 **Constructing the orthogonal matrix** $Q$: 
$$
Q = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}
$$
 
 Its transpose is: $$
Q^T = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}
$$
The diagonal matrix: $$
S = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}
$$
 
 Thus, the decomposition of $A$: $$
A = Q S Q^T
$$ represents a simple scaling transformation with a diagonal matrix.

## Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is a method of decomposing a matrix into three other matrices. It is one of the most powerful tools in linear algebra, especially in data science, image processing, and machine learning.

Given a matrix $A$ of dimensions $m \times n$, the SVD is given by:

$$
A = U \Sigma V^T
$$

$$
\text{Rotation} \times \text{Complete Matrix} \times \text{Rotation}
$$

### Properties:

- $U$ is an $m \times m$ orthogonal matrix whose columns are the **left singular vectors**.
- $\Sigma$ is an $m \times n$ **diagonal matrix** with non-negative real numbers on the diagonal, called the **singular values**.
- $V^T$ is an $n \times n$ orthogonal matrix whose rows are the **right singular vectors**.
- If $\Sigma$ is real, $U$ and $V^T$ can be orthogonal matrices, satisfying:

$$
U^T U = I, \quad V^T V = I
$$


- $A^T$ has dimensions $3 \times 2$ 
- $A$ has dimensions $2 \times 3$ 
- $A^T A$ has dimensions $3 \times 3$ and is the **right symmetric matrix** 
- $A A^T$ has dimensions $2 \times 2$ and is the **left symmetric matrix**
-  $U$ is a $2 \times 2$ matrix, corresponding to the eigenvectors of $A A^T$, 
-  $V^T$ is a $3 \times 3$ matrix, corresponding to the eigenvectors of $A^T A$.


- Substituting $A = U\Sigma V^T$ into $AA^T$, we have:

$$
\begin{aligned}
A A^T &= U\Sigma V^T (U \Sigma V^T)^T \\
&= U \Sigma V^T V \Sigma^T U^T \\
&= U \Sigma \Sigma^T U^T \\
&= U \Lambda U^T \\
&= U \Lambda U^{-1}
\end{aligned}
$$
i.e., $(AA^T) = U\Lambda U^{-1}$
i.e., the column vectors of $U$ are the eigenvectors of $AA^T$. 
- Similarly, the column vector of $V$ are the eigenvectors of $A^T A$.
- $\Sigma = \begin{bmatrix}\sigma_1 & 0 & 0 \\ 0 & \sigma_2 & 0 \end{bmatrix} \Rightarrow \Sigma \Sigma^T = \begin{bmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$ 
 $\Sigma^T \Sigma = \begin{bmatrix}\sigma_1^2 & 0 & 0 \\ 0 & \sigma_2^2 & 0 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 & 0 \\ 0& \lambda_2 & 0 \\ 0 & 0 & 0\end{bmatrix}$
 i.e., $AA^T$ and $A^TA$ have the same non-zero eigenvalues.
- The singular values $\sigma$ are the non-negative square roots of the eigenvalues of the matrix $A^T A$ or $AA^T$: $$
\sigma_i = \sqrt{\lambda_i}
$$
#### Example: SVD of a Matrix

For a given matrix $A$:
$$
A = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
$$

- We calculate the SVD by finding the eigenvalues  and eigenvectors and of $A^T A$ or $AA^T$
- Then construct the matrices $U$, $\Sigma$, and $V^T$. This decomposition allows for dimensionality.
- Take the square root of the diagonal elements of $\Sigma$.

---

## PageRank

PageRank is an algorithm developed by Google founders Larry Page and Sergey Brin that is used to rank web pages based on their importance.

### Key Points:

1. **Link-based Ranking**: A web page’s importance is determined by the number and quality of links pointing to it. If a web page is linked by many other important pages, it is considered important.
2. **Importance Propagation**: A page with a high PageRank contributes more to the rank of other pages it links to.
3. **Iterative Calculation**: The algorithm uses an iterative process to compute the rank of each page. Initially, each page is assigned an equal rank, and then the rank of each page is recalculated by considering the ranks of the pages linking to it. This process continues until the ranks converge to stable values.
4. **Damping Factor**: To prevent infinite loops or overemphasis on specific pages, PageRank includes a damping factor, typically set at 0.85. This factor accounts for the likelihood that a user might randomly jump to any page, rather than just following links.
5. **Mathematical Model**: Represented as a system of linear equations, and solving these equations yields the final ranks of all pages.

### (1) Using Code to Calculate PageRank

```python
def pageRank(linkMatrix, d):
    n = linkMatrix.shape[0]  # Number of pages (matrix size)
    M = d * linkMatrix + (1 - d) / n * np.ones([n, n])  # Create the transition matrix M
    r = 100 * np.ones(n) / n  # Initialize rank vector r, equally distributed
    lastR = r  # Save the last rank vector to check convergence
    r = M @ r  # Compute the first new rank vector by multiplying M with r
    while la.norm(lastR - r) > 0.01:  # Check convergence, stop if the difference is less than 0.01
        lastR = r  # Update lastR with current r
        r = M @ r  # Continue computing the next rank vector
    return r  # Return the final rank vector r
```

```python
# Eigenvalues
M = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 3]])
vals, vecs = np.linalg.eig(M)
vals
```

```python
# Eigenvectors - Note, the eigenvectors are the columns of the output.
M = np.array([[4, -5, 6],
              [7, -8, 6],
              [3/2, -1/2, -2]])
vals, vecs = np.linalg.eig(M)
vecs
```

### (2) using code to calculate eigenvectors, eigenvalues, and diagonal matrix

```python
import sympy as sp
# Step 1: Define the matrix A symbolically 
A = sp.Matrix([[2/3, -1],
               [-1/2, 1/2]])  # 写成分数形式sp

# Step 2: Compute eigenvalues and eigenvectors symbolically
eigenvalues, eigenvectors = A.eigenvals(), A.eigenvects()

# Step 3: Form the matrix C using the eigenvectors
# Extracting the eigenvectors from the list and forming matrix C
C = sp.Matrix.hstack(*[vec[2][0] for vec in eigenvectors])  

# Step 4: Calculate the diagonal matrix D = C^(-1) * A * C 
C_inv = C.inv()  
D = C_inv @ A @ C 

# Print results
print("Eigenvalues of A:")
for eigenvalue in eigenvalues:
    print(f"λ = {eigenvalue}")

print("\nEigenvectors (Matrix C):")
sp.pprint(C)

print("\nDiagonal matrix D:")
sp.pprint(D)
```
