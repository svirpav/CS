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
  
* **Divide and Conquer Algorithms**

s = 0, m = 0, e = 7

s = start

m = midpoint

e = end

**initial call** : devideArray(**e=0**, **e=7**)

> if(**s=0** < **e=7**):
>
> > m = 0 + math.floor((7-0) / 2 ) => 3
> >
> > divideArray(**s=0**, **e=m(3)**)
> >
> > > if(**s=0** < **e=3** )
> > >
> > > m = 0 + math.floor((3-0) / 2) => 1
> > >
> > > divideArray(**s=0**, **e=m(1)**)
> > >
> > > > if(**s=0** < **e=1**):
> > > >
> > > > m = 0 + math.floor((1-0) / 2) => 0
> > > >
> > > > divideArray(**s=0**, **e=m(0)**
> > > >
> > > > > if(**s= 0 < e = 0**) : ***EXIT - condition not met***
> > > > >
> > > > > ***This is the base case for first recursion divideArray(start, end)***
> > > >
> > > > divideArray(**s=m+1(1), e=1**)
> > > >
> > > > > if(**s=1 < e = 1**) : ***EXIT - condition not met***
> > > > >
> > > > > ***This is the base case for second recursion divideArray(mid+ 1, end)*** 
> > > >
> > > > mergeArray(**s=0**, **m=0**, **e=1**) => ***Sort first sub array[i[0], i[1]]***
> > >
> > > divideArray(**s=m+1(2)**, **e=3**)
> > >
> > > > if(**s=2** < **e=3**):
> > > >
> > > > > m = 2 + math.floor((3-2) / 2) => 2
> > > > >
> > > > > divideArray(**s=2**, **e=m(2)**)
> > > > >
> > > > > > if(**s=2** > **e=2**) => ***EXIT - Condition not met***
> > > > > >
> > > > > > ***Base case for first recursion divideArray(start, mid)***
> > > > >
> > > > > divideArray(**s=m+1(3)**, **e=3**)
> > > > >
> > > > > > if(**s=3** < **e=3**) => ***EXIT - Condition not met***
> > > > > >
> > > > > > ***Base case for second recursion divideArray(mid+1, end)***
> > > > >
> > > > > mergeArray(**s=2**, **m=2**, **e=3**)
> > >
> > > mergeArray(**s= 0, m = 1, e = 3**)
> >
> > divideArray(**s=m+1(4)**, **e=7**)
> >
> > > if(**s=4 < e=7**):
> > >
> > > > m = 4 + math.floor((7-4) / 2) => 5
> > > >
> > > > divideArray(**s=4, e=m(5)**)
> > > >
> > > > > if(**s=4 < e=5**):
> > > > >
> > > > > > m = 4 + math.floor((5-4) / 2) => 4
> > > > > >
> > > > > > divideArray(**s=4, e=m(4)**)
> > > > > >
> > > > > > > if(**s=4 < e=4**) => ***EXIT - condotion not met***
> > > > > > >
> > > > > > > ***Base case for the first recursion divideArray(start, mid)***
> > > > > >
> > > > > > divideArray(**s=m+1(5), e=(5)**)
> > > > > >
> > > > > > > if(**s=5 < e=5**)	=> ***EXIT - condition not met***
> > > > > > >
> > > > > > > ***Base case for the second recursion divideArray(mid+1, e)***
> > > > > >
> > > > > > mergeArray(**s = 4, m=4, e=5**)
> > > >
> > > > divideArray(**s = m+1(6), e = 7**)
> > > >
> > > > > if(**s = 6 < e = 7**)
> > > > >
> > > > > > m = 6 + math.floor((7-6) / 2) => 6
> > > > > >
> > > > > > divideArray(**s=6, e=m(6)**)
> > > > > >
> > > > > > > if(**s=6 < e=6**)	=> ***EXIT - condition not met***
> > > > > > >
> > > > > > > ***Base case for firs recursion met divideArray(start, mid)***
> > > > > >
> > > > > > divideArray(**s=m+1(7), e = 7**)
> > > > > >
> > > > > > > if(**s = 7 < e = 7**): ***EXIT - condition not met***
> > > > > > >
> > > > > > > ***Base case for second recursion divideArray(mid+1, e)***
> > > > > >
> > > > > > mergeArray(**s=6, m = 6, e = 7**
> > > >
> > > > mergeArray(**s = 4, m = 5, e = 7**)
> >
> > mergeArray(**s = 0, m = 3, e = 7**)	=> *** The last call in this recursion => merge initial array [0...7]



### Quick sort - programm flow

array[9, 7, 5, 11, 12, 2, 14, 3, 10, 6]

* ***Intial call***  quickSort(array, p(0), r-1(9))

> if(***0 < r(9)-p(0) = 9***) : ***r = 9***
>
> > q = partition(array, p, r)	=> ***q = 3***	[9, 7, 5, 11, 12, 2, 14, 3, 10, **6**]	=>	[5, 2, 3, **6**, 9, 7, 11, 14, 12, 10]
> >
> > quickSort(***array, p = 0, r = q-1(2)***)	=> ***This is first time caling recursion***
> >
> > > if(***1 < (r(2) - p(0)) = 2***):  ***r = 2***
> > >
> > > > q = partition(***array, p = 0, r=2***)	=> ***q = 1***	[5, 2, **3**]	=> [2, **3**, 5]
> > > >
> > > > quickSort(***array, p = 0, r = q-1(0))***
> > > >
> > > > > if(***0 < (r(0) - p(0))***):	=> ***EXIT - condition not met***
> > > > >
> > > > > ***This is the base case for first recursion quickSort(array, p, r = q -1)***
> > > >
> > > > quickSort(***array, p=q+1(2), r = 2*** )
> > > >
> > > > > if(**0 < (r(2) - p(2))**):	=> ***EXIT - condition not met***
> > > > >
> > > > > ***This is the exit from second recursion quickSort(array, p = q+1, r)***
> >
> > quickSort(**array, p = q+1(4), r = 9**)
> >
> > > if(**0 < (r(9) - p(4))**):	=> **r = 9**
> > >
> > > > q = partitioning(**array, p = 4, r = 9**)	=> **q = 2**	[9, 7, 11, 12, 14, **10**]	=>	[9, 7, **10**, 11,14, 12] 
> > > >
> > > > quickSort(**array, p = 4, r = q+1(6)**)



#### Partitioning Algorith

array[9, 7, 5, 11, 12, 2, 14, 3, 10, 6]

q = s(0)

key = array[e] => 6 

> for i in range(s, e):
>
> > if(key > array[i]):
> >
> > > swap(array, i, q)
> > >
> > > q += 1
>
> swap(array, q, e)
>
> return q

[9, 7, 5, 11, 12, 2, 14, 3, 10, (6)]

[**9**, 7, 5, 11, 12, 2, 14, 3, 10, (6)] 	=> i = 0, q = 0 ***(9 > 6)***

[9, **7**, 5, 11, 12, 2, 14, 3, 10, (6)] 	=> i = 1, q = 0 ***(7 > 6)***

[9, 7, **5**, 11, 12, 2, 14, 3, 10, (6)] 	=> i = 2, q = 0 ***(5 < 6)***	=> swap(array[i], array[q]) ***q += 1***

[5|, 7, 9, **11**, 12, 2, 14, 3, 10, (6)] 	=> i = 3, q = 1 ***(11 > 6)***

[5|, 7, 9, 11, **12**, 2, 14, 3, 10, (6)] 	=> i = 4, q = 1 ***(12 > 6)***

[5|, 7, 9, 11, 12, **2**, 14, 3, 10, (6)] 	=> i = 5, q = 1 ***(2 < 6)***	=> swap(array[i], array[q]) ***q += 1***

[5, 2|, 9, 11, 12, 7, **14**, 3, 10, (6)]	=> i = 6, q = 2 ***(14 > 6)***

[5, 2|, 9, 11, 12, 7, 14, **3**, 10, (6)]	=> i = 7, q = 2 ***(3 < 6)***	=> swap(array[i], array[q]) ***q += 1***

[5, 2, 3|, 11, 12, 7, 14, 9, **10**, (6)]	=> i = 8, q = 3 ***(10 > 6)***

***Sorted Sub-Array = [5, 2, 3|, 11, 12, 7, 14, 9, 10] return q = 3*** 



### Example for merge function ***mergeArray(array, start, mid, end)***

Initial array [1, 3, 35, 44, 0, 2, 12, 15]

slice the arry in two arrays

a[1, 3, 35, 44] : b[0, 2, 12, 15] => **a[i] : b[j]**

a[**1**, 3, 35, 44] >< b[**0**, 2, 12, 15] => **a[0]	b[0]** => array[0]

a[**1**, 3, 35, 44] >< b[**x**, **2**, 12, 15] => **a[0]	b[1]** => array[0, 1]

a[**x**, **3**, 35, 44] >< b[**x**, **2**, 12, 15] => **a[1]	b[1]** => array[0, 1, 2]

a[**x**, **3**, 35, 44] >< b[**x**, **x**, **12**, 15] => **a[1]	b[2]** => array[0, 1, 2, 3]

a[**x**, **x**, **35**, 44] >< b[**x**, **x**, **12**, 15] => **a[2]	b[2]** => array[0, 1, 2, 3, 12]

a[**x**, **x**, **35**, 44] >< b[**x**, **x**, **x**, **15**] => **a[2]	b[3]** => array[0, 1, 2, 3, 12, 15]

a[**x**, **x**, **35**, 44] >< b[**x**, **x**, **x**, **x**] => **a[2]	b[3]** => array[0, 1, 2, 3, 12, 15, 35]

a[**x**, **x**, **x**, **44**] >< b[**x**, **x**, **x**, **x**] => **a[3]	b[3]** => array[0, 1, 2, 3, 12, 15, 35, 44]







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