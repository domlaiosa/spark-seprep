## Arielle Maravilla - Assignment 7

### I ran the Codegen Application

Here is my Codegen Application Screenshot:

![Arielle's Screenshot](./images/arielle_codegen_screenshot.png)

#### What went well
The application launched successfully after troubleshooting the port mapping. I was able to generate Python code snippets, including a "Hello World" script and a Fibonacci sequence generator.

#### What didn’t go well
Initially, I had trouble accessing the application because the default URL didn’t work. I had to troubleshoot using `podman ps` to identify the correct port. Once resolved, the app worked as expected.

Also noticed that processing the prompts was quite slow. I am a little confused with some of the bot's responses as well. For example, rather than returning code, the bot responded with "Generate the code block at first, and explain the at the end". Another instance is when I asked for a "Hello World" python script. The both wrote the python, but also proceeded to translate it to Ruby without me specifying to do so.