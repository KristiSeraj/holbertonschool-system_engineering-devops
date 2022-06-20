# Loops, conditions and parsing

- [0-RSA_public_key.pub](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/0-RSA_public_key.pub) - RSA public key

- [1-for_best_school](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/1-for_best_school) - Bash script that displays `Best School` 10 times with `for` loop

- [10-fizzbuzz](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/10-fizzbuzz) - Bash script that displays numbers from 1 to 100
  - Displays `FizzBuzz` when the number is a multiple of 3 and 5
  - Displays `Fizz` when the number is multiple of 3
  - Displays `Buzz` when the number is a multiple of 5
  - Otherwise, displays the numbers

- [100-read_and_cut](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/100-read_and_cut) - Bash script that displays the content of the file `/etc/passwd`
  - The script only displays:
  - username
  - user id
  - Home directory path for the user

- [101-tell_the_story_of_passwd](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/101-tell_the_story_of_passwd) - Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS
  - Format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`

- [2-while_best_school](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/2-while_best_school) - Bash script that displays `Best School` 10 times with `while` loop

- [3-until_best_school](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/3-until_best_school) - Bash script that displays `Best School` 10 times with `until` loop

- [4-if_9_say_hi](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/4-if_9_say_hi) - Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line with `while` loop

- [5-4_bad_luck_8_is_your_chance](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/5-4_bad_luck_8_is_your_chance) - Bash script that loops with `while` from 1 to 10 and:
   - displays `bad luck` for the 4th iteration
   - displays `good luck` for the 8th iteration
   - displays `Best School` for other iterations

- [6-superstitious_numbers](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/6-superstitious_numbers) - Bash script that displays numbers from 1 to 20 with `while` loop and:
   - displays `4` and then `bad luck from China` for the 4th iteration
   - displays `9` and then `bad luck from Japan` for the 9th iteration
   - displays `17` and then `bad luck from Italy` for the 17th loop iteration
   - `case` statement is used

- [7-clock](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/7-clock) - Bash script that displays the time for 12 hours and 59 minutes:
  - displays hours from 0 to 12
  - displays minutes from 1 to 59

- [8-for_ls](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/8-for_ls) - Bash script that displays:
  - The content of the current directory
  - In a list format
  - Where only the part of the name after the first dash is displayed

- [9-to_file_or_not_to_file](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x04-loops_conditions_and_parsing/9-to_file_or_not_to_file) - Bash script that gives you information about the `school` file
  - Checks if the file exists or not and prints:
    - if the file exits: `school file exists`
    - if the file does not exist: `school file does not exist`
  - If the file exists, prints:
    - if the file is empty: `school file is empty`
    - if the file is not empty: `school file is not empty`
    - if the file is a regular file: `school file is a regular file`
    - if the files is not a regular file: (nothing)
