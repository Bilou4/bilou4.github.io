# Example of a complete analysis

## Static analysis

### Loading the file into PEID

![Loading the file into PEID](img/Lab03-03-PEid-1.png)

### List of sections

Here we can see that there are resources inside the binary.

![List of sections](img/Lab03-03-PEid-section.png)

### Strings in the binary

The `svchost.exe` string in a binary is not usual.

![Strings in the binary](img/Lab03-03-PEid-strings.png)

### Extracting resources

![Extracting resources](img/Lab03-03-resource-hacker.png)

Note that the extracted resource contains a lot of `0x41`. Perhaps a xor is performed to hide the resources.

### DependencyWalker Imports

![DependencyWalker Imports](img/Lab03-03-dependency-walker.png)

## Dynamic analysis

### Procmon in capture

![procmon before capture](img/Lab03-03-procmon-before-capture.png)



### Regshot 1/2

Before launching the binary, you need to do a first shot with RegShot to get a fingerprint of the Windows registry and see which ones have been modified.

![regshot 1st shot](img/Lab03-03-regshot-1st-shot.png)

### Regshot 2/2

Here we have all registry that have been modified or added during the process execution.

![Regshot comparison](img/Lab03-03-regshot-comparison.png)

### Process explorer

On the process explorer capture, we can see that after we started the malware, a new process called `svchost.exe` was also started.

![process explorer](img/Lab03-03-svchost-created-by-malware.png)

### Comparing strings

When comparing strings present in the binary and strings present in memory, we can see that they are not the same.

![Strings in the binary](img/Lab03-03-procexplo-strings-comparison-image.png)

Strings in memory look like keyboard keys. There is also a log file name. Could it be a keylogger?

![Strings in memory](img/Lab03-03-procexplo-strings-comparison-memory.png)



### Execution

During the execution, we can see that the `svchost.exe` process is created and that nothing is going through the network (the wireshark window stays empty).

![malware execution](img/Lab03-03-execution.gif)



While our **infected** `svchost.exe` continues to run, let's relaunch **procmon** and filter on the **infected** PID. And let's write to a notepad. We can see some operations such as `CreateFile`, `WriteFile`, `CloseFile`...

![procmon keylogger](img/Lab03-03-procmon-keylogger.gif)

You can find the path where the registered keyboard keys are located.

![log file path](img/Lab03-03-procmon-writefile-path.png)

Content of the created log file.

![log file content](img/Lab03-03-content-of-the-logfile.png)
