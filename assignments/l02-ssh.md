## SSH Practice

Note: `directory` and `folder` are interchangeable in the following tasks.

0. Your `Public and Private SSH keys` should live on your system at ~/.ssh/id_rsa.pub and ~/.ssh/id_rsa respectively.

1. Your username is your BU email address without the `@bu.edu`. Copy your public SSH key to the virtual machine at `34.138.171.158`
   **Note: Replace `YOUR_NAME` with your actual BU username**

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub YOUR_NAME@34.73.153.69
# password: YOUR_PASSWORD
```

2. SSH into the machine running at IP address `34.73.153.69`.

```bash
ssh -i ~/.ssh/id_rsa YOURNAME@34.73.153.69
```

3. Create a new directory `commandline-practice`..

4. Write the output of the `date` command into a file named `output.txt` located in the directory you created in Step 2

6. Run the following:

```bash
curl -o ./commandline-practice/joke.sh https://raw.githubusercontent.com/DS219/spark-seprep/main/joke.sh
```

6. Use chmod to make it possible to run the command `/home/YOURNAME/commandline-practice/joke.sh`

7. Run the script and append the joke to the file you created in Step 3. You can copy/paste _or_ use `>>` to redirect the output of the script to the file.

8. Complete [this](https://forms.gle/hNTTpmmsGC9yA22z5) form.

**HAVE FUN and ASK QUESTIONS!!**
