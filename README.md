#Computer Sciense

## Algorithms:

* **Linera search** : 

* **Binary search** :   ***(min + max) / 2***, number of searis is ***log2n***

* The logarithm function grows very slowly. Logarithms are the inverse of ***exponentials***

  That makes it easy to calculate the runtime of a binary search algorithm on an ***n*** that's exactly a ***power*** of 2. If ***n*** is 128, binary search will require at most 8.

* **Asymptotic notation** : 

  * Algorithm complexity:
    * f(n) = O(1) - constant
    * f(n) = O(log(n)) - Logorithmic grow
    * f(n) = O(n) - Linear growth
    * f(n) = O(n*Log(n)) - Quasiliner growth
    * f(n) = O(n^m) - polynominal growth
    * f(n) = O(2^n) - exponential growth

* **Algoritm analisys** : 

  * n^2/2 + n/2
    * Nested loops : example 2 nested loops = n^2, if we have 3 commands asume they are equal 5 time units = 5*f(n^2)
