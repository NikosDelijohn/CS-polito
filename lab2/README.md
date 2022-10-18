# Computer Science Laboratory \#2

## Part 1 - Arithmetic Operations

**[1.1]**  Write a program that stores two integers in two constants defined in code, and then displays their:
    
1. The sum.
2. The difference.
3. The product.
4. The average value.
5. The distance (i.e. the absolute value of the difference).
6. The maximum value (i.e. the greater of the two).
7. The minimum value (i.e. the lesser of the two).

>Tip: Use the max() and min() functions defined in Python. They accept a sequence of commaseparated values in input and return the maximum and minimum value of the sequence, respectively (for example, max(10, 5) returns 10).

**[1.2]**  Consider the following analog circuit:

```             
                 R1
       ________/\/\/\_____.______.
   +  |                   |      |
    -----                 /      /
 E   ---               R2 \   R3 \
   -  |                   /      /
      |                   |      |
      |___________________|______|
``` 
Write a program that, starting from the resistance of the three resistors, given by the user, calculates the total resistance, using Ohm's law.

**[1.3]** Write a program that stores in a constant a positive five-digit integer (therefore between 10000 and 99999), and displays the individual digits of which it is composed. For example, having the number 16384, the program must display, on separate lines: 
```
1
6
3
8
4
```

**[1.4]** Write the pseudocode and its Python program that helps a person decide
whether or not to buy a hybrid car. The inputs of the program should be:

-  the cost of a new car;
-  the estimate of the kilometers traveled in a year;
-  the estimate of the cost of fuel;
-  the efficiency in kilometers per liter;
-  the estimate of the resale value of the used car after 5 years.

Calculate the total cost of ownership of the car for 5 years (for simplicity, do not take into account the cost of financing). To provide input to the program, search the Web for realistic prices and consumption for two alternatives for buying a new car in the same price range: a hybrid model or and a gasoline. Run the program twice to compare the two alternatives, considering the current fuel price and the forecast of traveling 30,000 kilometers per year.

**[1.5]** According to Coulomb's law, the electric force (expressed in Newtons) between two charged charged particles, respectively, Q1 and Q2, separated by a distance r, is: 
$$F = \frac{Q_1 \times Q_2}{4\pi\epsilon r^2}$$

Where $\epsilon$ = $8.854$ $\times$ $10^{-12}$ $\frac{Farad}{meter}$. Write a program that calculates and shows on screen the force  relative to a pair of charged particles, allowing the user to choose the values $Q_1$, $Q_2$ (in Coulomb) and $r$ (in meters).

## Part 2 - String Manipulation

**[2.1]** Write a program that stores a string in a variable and displays the first three characters of the string, followed by three periods, again followed by the last three characters. For example, if the string is initialized to the value `"Mississippi"`, the program must display `"Mis...ppi"`. What happens to the string is shorter than 6 characters? What if it's shorter than 3 characters?

**[2.2]** The following pseudocode describes how to transform a string
containing a ten-digit telephone number (such as `"4155551212"`) into a more easily readable string, formatted in the U.S. style, such as `"(415) 555–1212"`:

1. Take the string consisting of the first three characters and surround it with round brackets (this is the prefix, called "area code");
2. Concatenating the prefix with the string containing the next three characters, a hyphen, and the string consisting of the last four characters results in the number in the required format. 

Translate this pseudocode into a Python program that stores a 10-digit phone number in a string, and then display it in the format just described. 

**[2.3]** 
Format the output of exercise 02.1.1 so that descriptions and numbers are
aligned vertically, for example: 
```
Sum:          45
Difference:   -5
```

**[2.4]**
[According to data collected by the Unicode Consortium](https://home.unicode.org/emoji/emoji-frequency/) the non-profit organization responsible for digitizing the world's languages, "tears of joy" (😂) account for more than 5% of all emojis used (the only other character that comes close to it is the ❤️). The top ten emojis used worldwide are: 😂 ❤️ 🤣 👍 😭 🙏 😘 🥰 😍 😊
When exchanging messages on Telegram (or on your favorite messaging app), which are the three emojis that you personally use most frequently? Using the Unicode encoding information [collceted here](https://unicode-table.com/en/) you can create a program that shows a scheme for each of these three emojis: 

1. the position in the ranking (rank).
2. the Unicode Number.
3. the Unicode Name.
4. the emoji itself. 

Format the output so that the information related to each of the three emojis is collected on one line, and the different fields are aligned vertically.

**[2.5]** The id of the students of a University is composed of two parts: a letter and a sequence of numbers. Write a program that, starting from two student ids, shows them on the screen in ascending order based on the numerical part only. 
>Tip: Use the default functions of the Python language