---
url: https://openjscad.xyz/docs/module-array-utils.html#.toArray
scraped_at: 2025-09-08T16:28:50.989577
title: Untitled
---

Utility functions for arrays.

Source:

    

  * [utils/array-utils/src/index.js](utils_array-utils_src_index.js.html), [line 1](utils_array-utils_src_index.js.html#line1)

##### Example

    
    
    const { flatten, head } = require('@jscad/array-utils')

### Methods

#### (static) flatten(array) → {Array}

Source:

    

  * [utils/array-utils/src/flatten.js](utils_array-utils_src_flatten.js.html), [line 10](utils_array-utils_src_flatten.js.html#line10)

Flatten the given array into a single array of elements. The given array can
be composed of multiple depths of objects and or arrays.

##### Example

    
    
    const flat = flatten([[1], [2, 3, [4, 5]], 6]) // returns [1, 2, 3, 4, 5, 6]

##### Parameters:

Name | Type | Description  
---|---|---  
`array` |  Array | array to flatten  
  
##### Returns:

a flat array with a single list of elements

Type

     Array

#### (static) fnNumberSort(a, b) → {Number}

Source:

    

  * [utils/array-utils/src/fnNumberSort.js](utils_array-utils_src_fnNumberSort.js.html), [line 11](utils_array-utils_src_fnNumberSort.js.html#line11)

Compare function for sorting arrays of numbers.

##### Example

    
    
    const numbers = [2, 1, 4, 3, 6, 5, 8, 7, 9, 0]
    const sorted = numbers.sort(fnNumberSort)

##### Parameters:

Name | Type | Description  
---|---|---  
`a` |  Number | first number  
`b` |  Number | second number  
  
##### Returns:

result of a - b

Type

     Number

#### (static) head(array) → {*}

Source:

    

  * [utils/array-utils/src/head.js](utils_array-utils_src_head.js.html), [line 9](utils_array-utils_src_head.js.html#line9)

Return the first element of the given array.

##### Example

    
    
    let element = head([1, 2])

##### Parameters:

Name | Type | Description  
---|---|---  
`array` |  * | anything  
  
##### Returns:

first element of the array, or undefined

Type

     *

#### (static) insertSorted(array, element, compareFunction)

Source:

    

  * [utils/array-utils/src/insertSorted.js](utils_array-utils_src_insertSorted.js.html), [line 11](utils_array-utils_src_insertSorted.js.html#line11)

Insert the given element into the give array using the compareFunction.

##### Example

    
    
    const numbers = [1, 5]
    const result = insertSorted(numbers, 3, fnNumberSort)

##### Parameters:

Name | Type | Description  
---|---|---  
`array` |  Array | array in which to insert  
`element` |  * | element to insert into the array  
`compareFunction` |  function | a function that defines the sort order of elements  
  
#### (static) nth(array, index) → {*}

Source:

    

  * [utils/array-utils/src/nth.js](utils_array-utils_src_nth.js.html), [line 11](utils_array-utils_src_nth.js.html#line11)

Return the Nth element of the given array.

##### Example

    
    
    let value = nth([1], 2) // undefined
    let value = nth([1, 2, 3, 4, 5], 3) // 4

##### Parameters:

Name | Type | Description  
---|---|---  
`array` |  * | anything  
`index` |  Number | index of the element to return  
  
##### Returns:

Nth element of the array, or undefined

Type

     *

#### (static) padToLength(anArray, padding, targetLength) → {Array}

Source:

    

  * [utils/array-utils/src/padToLength.js](utils_array-utils_src_padToLength.js.html), [line 13](utils_array-utils_src_padToLength.js.html#line13)

Build an array of the given target length from an existing array and a padding
value. If the array is already larger than the target length, it will not be
shortened.

##### Example

    
    
    const srcArray = [2, 3, 4]
    const paddedArray = padToLength(srcArray, 0, 5)

##### Parameters:

Name | Type | Description  
---|---|---  
`anArray` |  Array | the source array to copy into the result.  
`padding` |  * | the value to add to the new array to reach the desired length.  
`targetLength` |  Number | The desired length of the returned array.  
  
##### Returns:

an array with at least 'target length" elements

Type

     Array

#### (static) toArray(array) → {Array}

Source:

    

  * [utils/array-utils/src/toArray.js](utils_array-utils_src_toArray.js.html), [line 9](utils_array-utils_src_toArray.js.html#line9)

Convert the given array to an array if not already an array.

##### Example

    
    
    const array = toArray(1) // [1]

##### Parameters:

Name | Type | Description  
---|---|---  
`array` |  * | anything  
  
##### Returns:

an array

Type

     Array

