## KeyWords

- For Print -> ```quack``` (eg. quack Hello World )
-For beggining any program begin it with '''quack class name'''(e.g. quack sum (inorder to find the sum ) we can give any name to the class or program in ducklang but it must be related to the program if we want to
give space between two words it must be given with a '--')
- For assigning Data types, it  must be of two kinds one is quick_(data type)variable (if we want to specify the type of the variable)(e.g.quick_(int)language or quick_(integer)language for integer data type and for others it must be like
quick_(char)charac or quick_(character)charac and for floating point integers we have quick_(float)decimal and quick_(double)decimal)
Another type is duck variable(e.g duck decimal or duck charac and so on here the variable assigned with the variable can be of any data type ( this is extracted from kotlin like var and val))
Now the type of data in boolean would be either quick_(bool)variable=f(for false) or quick_(boolean)variable=f (e.g. quick_(bool)x=f or quick_(boolean)x=f) and in case of true value quick_(bool)y=t or quick_(boolean)=t
or simply we can write duck x=f and duck y=t( if we don't want to specify it)
now integer data type would contain positive , negative numbers including zero (upto 4 bytes ) more than four bytes we shall use quick_(long) variable or duck variable (and the value of this variable must be more than 4 bytes)
for floating or decimal point numbers we shall use float (upto 4 bytes) if it is more than that we shall use double
for character we can use a single character only no word or no two letters and all of it can be enclosed in single or double quotes
for word or sentence we will use string like quick_(string)variable="word" or duck variable="word"
for ASCII we shall use (A-Z(65-90) for a-z(97-122) for 0-9(48-57))
just like in java or c we terminate the statement using ; here we shall use -->':q?'(e.g. quick_(integer)x=15:q?)
  in order to terminate the entire program we shall use return quack:q?
  the post fix and prefix operators would remain same like (e.g. quick_(int)s=++a(prefix operator) and quick_(int)s=a++(postfix operator) similar in case of postfix decrement and prefix decrement)
  the arithmetic operators would also remain same (like '+' for addition '-' for subtraction '*' for multiplication and '/' for finding the quotient and % for finding remainder)
  /* Conditional control of ducklang.exe*/
  first we have only if where the syntax is
  if ( condition):quack
  {
  statements
  .....
  }
  Secondly we have if -duck_if( it would function like if elseif  in java or c or c++) 
  and the syntax is :
  if(condition):quack
  {
  statements
  ..}
  duck_if(condition):quack
  {
  statements
  ...}
  and thirdly we have if -duck_if-duck_end( it would function like if-elseif-else ,like in java or c or c++)
  syntax is :
  if(condition):quack
  {
  statements....
  }
  duck_if(condition):quack
  {
  statements...

}
duck_end:quack
{ 
statements...}
/* ternary operator in ducklang.exe*/
(condition):quack!!condition1;condition2:q?
  /* relational operators*/
  (>>(for greater sign), <<(for lesser sign) >>=(for greater equal to) <<=(for lesser equal to), ==(for equal to equal to), !=(for not equal to))
  /*logical operators*/
  ( &( for and) , ||(for or), !(for not))
  /* Looping structures*/
  1.for loop
  for(duck i=value:q?condition:q?i++):quack
  {
statements....
}
2.while loop 
while(condition):quack
{
statements....
}
3. do while loop
do:quack
{
statements....
}while(condition):q?
here just like c, java for and while loop are entry controlled and do while is exit controlled loop
COMMENTS in ducklang.exe
1.Single line comment
// comment
2. Multiline comment
/*comment*/
or /**comment**/
/* Functions in ducklang.exe*/
Syntax:
duck function name(parameters):quack(in case of any data type)
quick_(datatype)function name(parameters):quack(in case of specific data type)
in case of function call there does not need any object creation it will simply be done with the help of keyword and syntax is :quack_ducklang(function name (parameter if required..)):q?
//packages in quacklang//
1.import quacklang scan:q?
for integer it must be quick_(int)a=quack scan.nextInt():q?
for double it must be quick_(double)a=quack scan.nextDouble():q?
similarly for other data types also we shall surely discuss it later now let's write a simple program in ducklang.exe to find the sum of two unteger numbers after which we shall discuss the other packages and concept of recursion in ducklang.exe
//starting to write the program
import quacklang scan:q?
quack sum--twonumbers
{
quick_(int) sum:q?
quack Enter first number:q?
quick_(int)a=quack scan.nextInt():q?
quack Enter second number:q?
quick_(int)b=quack scan.nextInt():q?
sum=a+b:q?//performing sum in ducklang
quack sum 
return quack:q?
}
now in case of printing the statement we shall use one more feature 
quack--nextline(varible or statement) (in order to print it in next line)
and only quack to print it in same line just like in above case
now doing the above program using quack--nextline
import quacklang scan:q?
quack sum--twonumbers
{
quick_(int) sum:q?
quack--nextline Enter first number:q?
quick_(int)a=quack scan.nextInt():q?
quack--nextline Enter second number:q?
quick_(int)b=quack scan.nextInt():q?
sum=a+b:q?//performing sum in ducklang
quack --nextline sum :q?
return quack:q?
}
Now let's discuss the statement of package using float,character, string,boolean
for float-->
quick_(float)a=quack scan.nextFloat():q?
for character
quick_(char)a=quack scan.nextcharAt(0):q?
for string we have 
quick_(string)a=quack scan.next():q?(for printing oneline)
quick_(string)a=quack scan.nextline():q?(for printing a paragraph)
now we shall discuss recursion in quacklang.exe
//**recursion**//
syntax:
if (base condition):quack
return(statement):q?
duck_end:quack
return (condition):q?
e.g. finding factorial of a number using recursion 
import quacklang scan:q?
quack factorial
{
quack--nextline enter a number:q?
quick_(int)x=quack scan.nextInt():q?
quick_(int)factorial(x):quack
{
if(x==0)
return(1):q?
duck_end:quack
return(x*quack_ducklang(factorial (x-1))):q?
}
quack main()//creation of main method in ducklang 
{
duck y=5;
duck f= quack_ducklang(factorial(y)):q?
quack--nextline factorial,f:q?(comma used to seperate variable from the statement )
}
return quack:q?
}
//ARRAYS in DUCKLANG//
1 . Single dimensional arrays
Syntax:
quick_(datatype)arrayvariable[arraysize]:q?(e.g quick_(int)x[20]:q?)
OR
duck arrayvariable[arraysize]:q?(e.g. duck x[12]:q?)
2. Double dimensional arrays
Syntax:
quick_(datatype)arrayvariable[no.of rows][no.of columns]:q?(e.g. quick_(int)x[10][10]:q?)
OR
duck arrayvariable[no.of rows][no.of columns]:q?(e.g. duck x[10][10]:q?)
|| finding the total length of array if size is assumed a variable
arrayvariable.ducksize():q?(e.g.x.ducksize():q?)
///*** ACCESSiNG Data from single and double dimensional arrays***///
1. Single dimensional arrays
 import quacklang scan:q?
 quick_(int)x[10]:q?
   for(quick_(int)i=0:q?i<x.ducksize():q?i++):quack
   {
   x[i]=quack scan.nextInt():q?
   }
 2. Double dimensional arrays

  import quacklang scan:q?
  quick_(int)x[5][5]:q?
  for(quick_(int)i=0:q?i<5:q?i++):quack
  {
  for(quick_(int)j=0:q?j<5:q?j++):quack
   {
   x[i][j]=quack scan.nextInt():q?
   }
   }
   /////@@@ hERE WE HAVE ALMOST STATED ALL THE MAIN KEY FEATURES OF DUCKLANG
         anD IF WE ADD ANY MORE FEATURES WE WILL UPDATE LATER HERE
                                           @@@/////
   
