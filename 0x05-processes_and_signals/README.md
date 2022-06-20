# Processes and signals

- [0-what-is-my-pid](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/0-what-is-my-pid) - Bash script that displays its own PID

- [1-list_your_processes](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/1-list_your_processes) - Bash script that displays a list of currently running processes
  - Shows all processes, for all users, including those which might not have a TTY
  - Displays in a user-oriented format
  - Shows process hierarchy

- [2-show_your_bash_pid](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/2-show_your_bash_pid) - Bash script that displays lines containing the `bash` word

- [3-show_your_bash_pid_made_easy](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/3-show_your_bash_pid_made_easy) - Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

- [4-to_infinity_and_beyond](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/4-to_infinity_and_beyond) - Bash script that displays `To infinity and beyond` indefinitely
  - In between each iteration of the loop, is a `sleep 2`

- [5-dont_stop_me_now](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/5-dont_stop_me_now) - Bash script that stops `4-to_infinity_and_beyond` process with `kill` command

- [6-stop_me_if_you_can](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/6-stop_me_if_you_can) - Bash script that stops `4-to_infinity_and_beyond` process without `kill` or `killall` command

- [67-stop_me_if_you_can](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/67-stop_me_if_you_can) - Copy of `6-stop_me_if_you_can` that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` process

- [7-highlander](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/7-highlander) - Bash script that displays:
  - `To infinity and beyond` indefinitely
  - With a `sleep 2` in between each iteration
  - `I am invincible!!` when receiving a `SIGTERM` signal

- [8-beheaded_process](https://github.com/KristiSeraj/holberton-system_engineering-devops/blob/main/0x05-processes_and_signals/8-beheaded_process) - Bash script that kills the process `7-highlander`
