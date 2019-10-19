# Computer Sciense

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

  * Permutationa and combination :
    * **n! / k! * (n-k)!** 
  * **Example of recursion based on factorial** : 
    * x = 5 => $\frac{5*4!=>4*3!=>3*2!=>2*1!=>1*0!}{5*24(120)=>4*6(24)=>3*2(6)=>2*1(2)=>1*1(1)}$ 5! = 120

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
  
* **Statistics and probability **

  * Conting, premutations and combinations:
    * **Permutation** => A, B, C, D, E to filve different location => 5! => 5 * 4 * 3 * 2 * 1 => 120, but if we have for example only 3 place awaylable it is going to be =>  $\frac{n!}{(n-r)!}$ 
    * **Fractorial** n! => n * (n-1) * (n-2) *(n - 3) * ... * 1
    * **Combination** => 6 people for 3 char => $\frac{6!}{(6-3)!}$ => $\frac{720}{6}$ => 120, now we want to 3 out 6 people to see how much combination it might have, $n^ck = \frac{n!}{k!*(n-k)!}$ => $\frac{720}{6 * 6}$ => 20

## Hanoi Tower

**recursion_1(n-1)**

**move(n)**

**recursion_2(n-1)**

* **Case where n = 5 ** 

**All recursion completed case return to initial call solveTower(n=5)**

n = 5 => steps after first recursion

> move(5) => **move disk nr. : 5**		**DONE(1)** 
>
> recursion_2(5 - 1) => 4
>
> > n=4
> >
> > recursion_1(4-1) => 3
> >
> > > n=3
> > >
> > > recursion_1(3-1) => 2
> > >
> > > > n=2
> > > >
> > > > recursion_1(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) => **move disk nr. : 1** 		***DONE(2)***
> > > > >
> > > > > recursion_2(1-1) =>  exit **return 1**
> > > >
> > > > move(2) => **move disk nr. :2**			***DONE(3)***
> > > >
> > > > recursion_2(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) => **move disk nr. 1**		***DONE(4)***
> > > > >
> > > > > recursion_2(1-1) => exit **return 1**
> > >
> > > move(3) **move disk nr. 3**		**DONE(5)**
> > >
> > > recursion_2(3-1) => 2
> > >
> > > > n=2
> > > >
> > > > recursion_1(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) => **move disk nr. : 1**		**DONE(6)**
> > > > >
> > > > > reursion_2(1-1) => exit **return 1**
> > > >
> > > > move(2) => **move disk nr. : 2**		**DONE(7)**
> > > >
> > > > recursion_2(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) => **move disk nr. : 1**		**DONE(8)**
> > > > >
> > > > > recursion_2(1-1) => exit **return 1**
> >
> > move(4) **move disk nr. : 4**		**DONE(9)**
> >
> > recursion_2(4-1) => 3
> >
> > > n=3
> > >
> > > recursion_1(3-1) => 2
> > >
> > > > n=2
> > > >
> > > > recursion_1(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1)  => **move disk nr.: 1**		**DONE(10)**
> > > > >
> > > > > recursion_2(1-1) => exit **return 1**
> > > >
> > > > move(2) **move disk nr.:2**		**DONE(11)**
> > > >
> > > > recursion_2(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) => **move disk nr.:1**		**DONE(12)**
> > > > >
> > > > > recursion_2(1-1) => exit **return 1**
> > >
> > > move(3) **move disk nr.:3**		**DONE(13)**
> > >
> > > recusrion_2(3-1) => 2
> > >
> > > > n=2
> > > >
> > > > recursion_1(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) **move disk nr.:1**		**DONE(14)**
> > > > >
> > > > > recursion_2(1-1) => exit **return 1**
> > > >
> > > > move(2) => **move disk nr.:2**		**DONE(15)**
> > > >
> > > > recursion_2(2-1) => 1
> > > >
> > > > > n=1
> > > > >
> > > > > recursion_1(1-1) => exit **return 1**
> > > > >
> > > > > move(1) **move disk nr.:1**		**DONE(16)**
> > > > >
> > > > > recursion_2(1-1) => exit **return 1**

