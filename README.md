# [\[07JCJ**\] - Computer Sciences @ PoliTO 2022-2023](https://didattica.polito.it/pls/portal30/gap.pkg_guide.viewGap?p_cod_ins=07JCJLI&p_a_acc=2021&p_header=S&p_lang=IT&multi=N)

This repository is dedicated to the laboratory sessions of the course "Computer Sciences" of Politecnico di Torino. 

As an assistance towards the students, we provide to you some <u>**indicative**</u> solutions to the laboratory sessions. 

:warning: 
**Be extremely careful!** The solutions that you see here are not to be followed blindly. You should **first** attempt to solve EACH exercise by yourselves and then use (if needed) any of the solutions you can find here as a hint or support. If you do not practice and hone your coding skills by yourselves, eventually you will not succeed.

Also, these solutions represent the author's way to approach the problem, which may differ from the way you would approach and solve the problem. This does not render your solution wrong or inferior. Programming is a school of thought, and most of the times there are more than 1 correct solutions to a problem. 

With that said, each set of solutions will be uploaded **2 weeks** after the lab delivery. For example, the solutions for lab 1 will be uploaded during the delivery of lab3, the solutions for lab2 during the delivery of lab4 and so on.

### Upload Schedule 

| Laboratory | Upload Date | 
| :--------: | :-----------:|
| [lab1](https://github.com/NikosDelijohn/CS-polito/tree/master/lab1)          | ~~03-Oct-22~~   |
| [lab2](https://github.com/NikosDelijohn/CS-polito/tree/master/lab2)       | ~~24-Oct-22~~   | 
| [lab3](https://github.com/NikosDelijohn/CS-polito/tree/master/lab3)       | ~~07-Nov-22~~   |
| [lab4](https://github.com/NikosDelijohn/CS-polito/tree/master/lab4)      | 14-Nov-22   |
| [lab5](https://github.com/NikosDelijohn/CS-polito/tree/master/lab5)       | 21-Nov-22   |
| [lab6](https://github.com/NikosDelijohn/CS-polito/tree/master/lab6)       | 28-Nov-22   |
| lab7       | 05-Dec-22   |
| lab8       | 12-Dec-22   |
| lab9       | 19-Dec-22   |
| lab10      | 09-Dec-22   |
| lab11      | _TBA_  :construction:       |
| lab12      | _TBA_    :construction:     |

### Some `Python3` tips 
1. Don't be afraid to use representative variable names! Remember that the readability of your code plays a key role to its understanding by other readers or even by you when you try to debug it. Use `nouns` for variables and for functions use `full sentences`. For example: `minimum = find_minimum(integer_list)`. For functions specifically, if they return a `boolean` value it is a good practice to have the `has_` or `is_` as a prefix to their name (e.g., `if is_prime(number):`) 

2. Use capital letters for "global" variables and constants. For example: `PI = 3.14`

3. Avoid using python3 keywords as variable names. In the case you still want to do it, end the variable name with a single underscore e.g., `list_ = [1,2,3]`

4. Use the boilerplate:
    ```
    def main():
        """
        Your Code Here
        """
    if __name__ == "__main__":
        main()
    ```
5. In case of handling exceptions, be specific and as acurate as  posible with your `try except` blocks. Do not engulf huge code segments but only the point of failure. For example:
   - :heavy_check_mark: do :heavy_check_mark: :
   ```
    try:
        with open("numbers.txt") as infile:

            """
            read the file contents
            """
    except FileNotFoundError:
        """
        handle it
        """
    """
    do stuff with the just read file contents
    """
    exit

   ```
   - :x: don't :x: :
    ```
    try:
        with open("numbers.txt") as infile:

            """
            read the file contents
            """

            """
            do stuff with the just read file contents
            """
            exit
    except FileNotFoundError:
        """
        handle it
        """

    ```
     - Always advise [the pydocs](https://docs.python.org/3/library/exceptions.html) for the existing exception classes and their hierarchy.

6. In the case that you are opening files using the plain `open()` function instead of the `with open()` statement, DO NOT FORGET to use `close()` as well when you are done with the file :bangbang:

7. 
   - Q: What is the very first line I see in some python3 scripts `#!/usr/bin/python3` ?
   - A: Its called [shebang](https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3-shebang)
## Auxiliary Information
- Advise prof. Squillero's [repository](https://github.com/squillero/computer-sciences/tree/master/Python) for extra information.

- Bookmark https://docs.python.org/3/ as your main `goto` place for finding useful information about the standard library with convenient examples and use cases.
