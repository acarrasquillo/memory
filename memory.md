Abimael Carrasquillo-Ayala

##Write a program in one language of choice that will run on a both Windows and Linux OS.


###You must not use more than one language. The program will output three things:

1. Total system memory.
2. Total system memory in use
3. Total system memory available.

Output the three things to some file on the local OS.


# Solution

##Programming Language: Python 2.7

###Description:
This program calls a platform specific command that would have the required memory information. The command output would be parsed to collect that information. The results would be wrote to a file on the home directory of the user running the program (This is the default if no path is provided), using the 'HOME' environment variable. The user can change the output path providing arguments to the program. The output file will be named ***memory-output YYYY-MM-dd HH-mm-ss.txt*** where *YYYY-MM-dd HH-mm-ss* is the time when the program was executed.

####Sample Usage:
`python memory.py`

`OR`

`python memory.py -p <output-path> (Optional)`

####Tested VM's:
 - Windows 8 VM (Only had Windows 8 license key)
 - Ubuntu Server, CentOS 7


####Utilized platform commands output examples:


#####Linux: `free`
The `free` linux bash command was utilized to solve this problem. The next example shows an output of running this command:

				  total        used        free      shared     buffers       cache
	Mem:            489         182         133           4           0         172
	Swap:           819           0         819

#####Windows: `systeminfo /FO CSV`
The `systeminfo` windows command was also utilized to solve this problem. The `/FO CSV` parameter allows to get the output as a comma separated string, useful to parse and retrieve the required data.

	'"Host Name","OS Name","OS Version","OS Manufacturer","OS Configuration","OS Bui
	ld Type","Registered Owner","Registered Organization","Product ID","Original Ins
	tall Date","System Boot Time","System Manufacturer","System Model","System Type"
	,"Processor(s)","BIOS Version","Windows Directory","System Directory","Boot Devi
	ce","System Locale","Input Locale","Time Zone","Total Physical Memory","Availabl
	e Physical Memory","Virtual Memory: Max Size","Virtual Memory: Available","Virtu
	al Memory: In Use","Page File Location(s)","Domain","Logon Server","Hotfix(s)","
	Network Card(s)","Hyper-V Requirements"\r\n"WINDOWS8-VM","Microsoft Windows 8.1
	Pro","6.3.9600 N/A Build 9600","Microsoft Corporation","Standalone Workstation",
	"Multiprocessor Free","email@hotmail.com","","xxxx-xxxxx-xxxxx-xxxxx","
	11/12/2015, 6:57:25 PM","11/12/2015, 6:56:43 PM","innotek GmbH","VirtualBox","x6
	4-based PC","1 Processor(s) Installed.,[01]: Intel64 Family 6 Model 58 Stepping
	9 GenuineIntel ~2893 Mhz","innotek GmbH VirtualBox, 12/1/2006","C:\\Windows","C:
	\\Windows\\system32","\\Device\\HarddiskVolume1","en-us;English (United States)"
	,"en-us;English (United States)","(UTC-08:00) Pacific Time (US & Canada)","1,024
	 MB","423 MB","2,752 MB","1,768 MB","984 MB","C:\\pagefile.sys","WORKGROUP","\\\
	\MicrosoftAccount","8 Hotfix(s) Installed.,[01]: KB2919355,[02]: KB2919442,[03]:
	 KB2937220,[04]: KB2938772,[05]: KB2939471,[06]: KB2949621,[07]: KB3020370,[08]:
	 KB3072318","1 NIC(s) Installed.,[01]: Intel(R) PRO/1000 MT Desktop Adapter,
		Connection Name: Ethernet,      DHCP Enabled:    Yes,      DHCP Server:     10
	.0.2.2,      IP address(es),      [01]: 10.0.2.15,      [02]: fe80::29e6:798b:32
	f9:bb26","A hypervisor has been detected. Features required for Hyper-V will not
	 be displayed."\r\n'

##References

- ##Libraries:

  - [Python.org: OS library](https://docs.python.org/2/library/os.html)
  - [Python.org: Subprocess library](https://docs.python.org/2/library/subprocess.html)
  - [Python.org: Datetime](https://docs.python.org/2.7/library/datetime.html#strftime-strptime-behavior)

- ##OS Information
  - [Python on Windows](https://docs.python.org/2/faq/windows.html)
  - [An A-Z Index of the Bash command line for linux](http://ss64.com/bash/)
  - [An A-Z Index of the Windows CMD command line](http://ss64.com/nt/)
