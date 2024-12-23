## KeyWords

- **For Print** -> `quack`  
  Example: `quack "Hello World"`

- **Input from User** -> `getFeathers`  
  Example: `setFeather userName = getFeathers "Enter your name: "`

- **If** -> `ifFlap`  
  Example: `ifFlap x > 5`

- **Else** -> `elseWaddle`  
  Example: `elseWaddle quack "Not Greater"`

- **ElseIf** -> `elifFlap`  
  Example: `elifFlap x == 5`

- **While** -> `whilePaddle`  
  Example: `whilePaddle x < 10`

- **For Loop** -> `forFlap`  
  Example: `forFlap i = 0; i < 10; i++`

- **Function** -> `duckFunc`  
  Example: `duckFunc sayHello() { quack "Hello!" }`

- **Return** -> `returnNest`  
  Example: `returnNest x + 2`

- **Variable Declaration** -> `setFeather`  
  Example: `setFeather x = 10`

- **True/False** -> `yesFlap` / `noFlap`  
  Example: `ifFlap x == yesFlap`

- **Loop** -> `doFlap`  
  Example: `doFlap i = 0; i < 10; i++`

- **Break Loop** -> `breakPaddle`  
  Example: `breakPaddle`

- **Continue Loop** -> `keepFlap`  
  Example: `keepFlap`

- **Switch Case** -> `switchNest`  
  Example:  
  ```  
  switchNest x {  
    case 1: quack "One"; breakPaddle  
    case 2: quack "Two"; breakPaddle  
    default: quack "Other"; breakPaddle  
  }
  ```

- **Function Call** -> `callDuck`  
  Example: `callDuck add(5, 10)`

---

## Operators

- **Addition** -> `addFeathers`  
  Example: `x addFeathers y`

- **Subtraction** -> `loseFeathers`  
  Example: `x loseFeathers y`

- **Multiplication** -> `spreadWings`  
  Example: `x spreadWings y`

- **Division** -> `dividePond`  
  Example: `x dividePond y`

- **Equality** -> `sameNest`  
  Example: `x sameNest y`

- **Not Equal** -> `diffNest`  
  Example: `x diffNest y`

- **Greater Than** -> `biggerNest`  
  Example: `x biggerNest y`

- **Less Than** -> `smallerNest`  
  Example: `x smallerNest y`

- **Logical AND** -> `bothFlap`  
  Example: `x bothFlap y`

- **Logical OR** -> `eitherFlap`  
  Example: `x eitherFlap y`

- **Logical NOT** -> `noFlap`  
  Example: `noFlap x`

---

## Data Types

- **Integer** -> `egg`  
  Example: `setFeather age = 25`

- **String** -> `feather`  
  Example: `setFeather name = "Duckling"`

- **Boolean** -> `yesFlap` / `noFlap`  
  Example: `setFeather isHappy = yesFlap`

- **Array/List** -> `flock`  
  Example: `setFeather birds = flock[1, 2, 3]`

- **Object** -> `duckling`  
  Example: `setFeather myDuck = duckling{name: "Donald", age: 2}`

- **Null** -> `pondEmpty`  
  Example: `setFeather myVariable = pondEmpty`

---

## Functions

- **Define Function** -> `duckFunc`  
  Example: `duckFunc add(a, b) { returnNest a addFeathers b }`

- **Anonymous Function (Lambda)** -> `quickDuck`  
  Example: `setFeather multiply = quickDuck(x, y) { returnNest x spreadWings y }`

- **Function Return** -> `returnNest`  
  Example: `returnNest x + 2`

---

## Comments

- **Single-line comment** -> `#`  
  Example: `# This is a comment`

- **Multi-line comment** -> `##`  
  Example:  
  ```  
  ## This is a  
  multi-line comment  
  ##  
  ```

---

## Flow Control

- **Continue Loop** -> `keepFlap`  
  Example: `keepFlap`

- **Break Loop** -> `breakPaddle`  
  Example: `breakPaddle`

- **Switch Case** -> `switchNest`  
  Example:  
  ```  
  switchNest x {  
    case 1: quack "One"; breakPaddle  
    case 2: quack "Two"; breakPaddle  
    default: quack "Other"; breakPaddle  
  }
  ```

---

## Special Structures

- **Class Declaration** -> `ducklingClass`  
  Example:  
  ```  
  ducklingClass Duck {  
    setFeather name  
    setFeather age  
  
    duckFunc introduce() {  
      quack "I am " addFeathers name addFeathers " and I am " addFeathers age addFeathers " years old."  
    }  
  }  
  ```

- **Object Instantiation** -> `newDuck`  
  Example: `setFeather myDuck = newDuck Duck(name = "Donald", age = 5)`

---

## Math Functions

- **Square Root** -> `swimDuck`  
  Example: `setFeather sqrtValue = swimDuck 16`

- **Power** -> `wingPower`  
  Example: `setFeather result = wingPower 2 3`

- **Random Number** -> `pondRandom`  
  Example: `setFeather randomNum = pondRandom 1 100`

---

## File Operations

- **Read File** -> `duckRead`  
  Example: `setFeather content = duckRead "file.txt"`

- **Write File** -> `duckWrite`  
  Example: `duckWrite "file.txt" content`

---

## Type Casting

- **To Integer** -> `eggCast`  
  Example: `setFeather number = eggCast "25"`

- **To String** -> `featherCast`  
  Example: `setFeather str = featherCast 25`


---

## Additional Concepts

- **Array Length** -> `flockSize`  
  Example: `setFeather size = flockSize birds`

- **Array Access** -> `flockAt`  
  Example: `setFeather bird = flockAt birds 2`

- **Ternary Operator** -> `duckCondition`  
  Example: `setFeather result = duckCondition x biggerNest 5 then "Big" else "Small"`
