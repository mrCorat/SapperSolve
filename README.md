+There 2 classes and 2 functions
#1. Function to get neighbour cells
Moore distance get cell as tuple of 2 integers and gives you list of cells of neighbour cells  which also are tuples of 2 integers? which has distance of [moore neighbours](https://en.wikipedia.org/wiki/Moore_neighborhood).

|Scenarious|Values|
|----------|------|
|Tuple of 2 integers|list of 8 neighbour tuple of 2 integer cells|
|Not integer number|empty list|
|Not correct size tuple| empty list|
#2. Validator class
Class, where we analizing symbols.
Symbols card:
 - 0,1,2,3,4,5,6,7,8 - number near mines(but entrance is not verified in first variants)
 - x - bomb gain (tests with that symbol must be included hen symbol included)
 - ? - undefined cell(first test with that, but in second step not be there)
 - " " - ignoring as divider
 - other - non-correct number
 In Testing we include all symbols
 
 |Parameter|Result|
 |---------|------|
 |correct number|True|
 |9|False|
 |x|True|
 |?|True|
 |string without valid number|False|
 |string with '?'|False|
 |string with number < '8'|False|
 |ASCII code of '0' - '8' or '?'|False|
#3. Minefield class
Class converts rectangle string to class with getting information about it cells
Our fiel are rectangles, but algorithm should works on every variants of 2-dimentional field, but problems with getting this field.
Also in solver there must be at least 1 0-number cell.
When the class gets string it should take alphabet {?, 0}
Then class should changes values in alphabet {'0' - '8', 'x'}
other element is number of bombs. It must be positive integer.
Class Making

|Parameters|Result|
|----------|-------|
|Correct rectangle string without " "| Full Field System|
|Correct rectangle string with " "| Full Field System|
|Elements with not correct chars| Empty Field|
|String are not rectangle without " "|Empty Field|
|String are not rectangle with " "|Empty Field|
|size is positive|size are included|
|size is not positive|Empty Field|

##Class get_entrance

|Parameters|Result|
|----------|-------|
|there is a zeros in entrance|cells with zeros|
|there is no zeros|Exception of not correct int|
Changing Class parameters

|Parameters|Result|
|----------|-------|
|Get char in correct cell|changing field in class|
|Get char in non-correct cell| Exception of cell|
|Get not correct char in cell|Exception of char|
|Get not char in cell|Exception of first type|
|Get non 2-tuple type in parameter|Exception of second type|
|Get correct char in cell|change field in class|
