#Computer Sciense

## Algorithms:

* **Linera search** : 

  * O(n)

* **Binary search** :   ***(min + max) / 2***, number of searis is $log_2(n)$

  * The logarithm function grows very slowly. Logarithms are the inverse of ***exponentials***

    That makes it easy to calculate the runtime of a binary search algorithm on an ***n*** that's exactly a ***power*** of 2. If ***n*** is 128, binary search will require at most 8.

* **Insert search : **

  * If we have k elements and amount of lines to execute is constant c (**case when every inserted element is lower than sorted elemnts in array**):
    * c\*1 + c\*2 + c\*3 + ... + c\*(n-1) = c (1 + 2 + 3 + ... + n-1)
    * $c *\frac{(1+(n-1))*(n-1)}{2}$ => $c*\frac{n*(n-1)}{2}$ => $c*\frac{n^2 - n}{2}$ => $\frac{cn^2 - cn}{2}$ Using ***BigTheta*** notation we discard constant **c** , $\frac{1}{2}$ and $\frac{cn}{2}$ => $\Theta(n^2)$
  * If **every insert elemnt is equal or greater then all sorted elements** :
    * Ther is **n-1** calls with constant time **c** => **c \* (n-1) ** => Discard **c** and **1** => $\Theta (n)$
  * If we have array woth random sorted numbers in it we asume that average time to sort the array would take **k/2**. But in asymptotic notation, where constant coefficients don't matter, the running time in the average case would still be $\Theta (n^2)$, worst case.
  * **Consclusion**:
    * Worst case $\Theta (n^2)$
    * Best case $\Theta (n)$
    * Average case $\Theta (n^2)$
    * Best case $\Theta (n)$

* **Recursive search** :

  * TBD

* **Asymptotic notation** : 

  * Algorithm complexity:
    * f(n) = O(1) - constant
    * f(n) = O(log(n)) - Logorithmic grow
    * f(n) = O(n) - Linear growth
    * f(n) = O(n*Log(n)) - Quasiliner growth
    * f(n) = O($n^m$) - polynominal growth
    * f(n) = O($2^n$) - exponential growth

* **Algoritm analisys** : 

  *  $\frac{n^2}{2 + n/2}$
    * Nested loops : example 2 nested loops = $n^2$, if we have 3 commands asume they are equal 5 time units = $5*f(n^2)$
  
* **Arithmentic sequence** :

  * Arithmetic sum => $a_n$ = $a_1 + d(n-1)$, $S_n$ = $\frac{a_1 + a_n}{2} * n$ ,   $n = \frac{a_n - a_1}{d}+1$  => ($S(n) = \frac{n*(n+1)}{2}$)
