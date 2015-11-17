################################################################################################
# Name: Abimael Carrasquillo-Ayala
# Email: abimael.carrasquillo@gmail.com
###############################################################################################
import sys, subprocess,os, datetime

global PLATFORM
global PATH
global FILENAME

def Print_Help():
    '''
        Description:
            This function will print how this script should be run and the optional parameters that can recieve.
    '''
    print """
    memory.py: Outputs total system memory, system memory in use and total system memory available.

        Usage:
            python memory.py -p <output-path> (Optional)

        Optional Command line argument:
            output-path: String | The path to save the output-file (Defaults: '/Users/Home' (Linux) and 'C:\User\Home' (Windows) )

        The results will be written on output-file: memory-output YYYY-MM-dd HH-mm-ss.txt\n"""
def Exc_Command(command, platform, path, filename):
    '''
        Description:
            Excecutes a platform specific command and calls the function to parse the
            command output.

        Parameters:
            <command> String | platfrom specific command
            <platform> String | platform specific name, provided by `sys.platfrom`
            <path> String | Valid OS path directory to save the results
            <filename> The filename of the output.
    '''
    try:

        print "Retrieving Information ..."

        output = subprocess.check_output(command) # excecute given command and return the output

        Parse_Output(output, platform, path, filename) # Parse the output of the command

    except Exception as e:

        sys.exit("\nThere was an error excecuting platform command\n\t Details:" + str(e)) # end program and output error message.

def Parse_Linux(output):
    '''
        Description :
            Parses linux 'free' bash command output.

        Parameters :
            <output> String | The output string of the linux 'free' bash command.
    '''
    try:

        output = [l.strip() for l in output.split('\n')] #get the list of lines on the output

        header = output[0].split() # get the list of  header columns

        rows = output[1:len(output) - 1] # get the list of rows

        rows = [(r.split(':')[0], r.split(':')[1].split()) for r in rows] # get the key,values tuple list

        table = dict()

        for key,values in rows:
            k = key.lower() # remove case sensitive
            if k == 'mem':
                table[k] = dict() # add the row key to the data table
                for i in xrange(len(values)):
                    table[k][header[i]] = values[i] # add the values to the row key

        return table

    except Exception as e:

        raise Exception("\nError parsing linux output\n\t Details:" + str(e))

def Parse_Windows(output):
    '''
    Description:
        Parses Windows 'systeminfo /FO CSV' command  output to collect the needed data.
        The 'systeminfo' command will return the data as a comma separated string, utilizing the '/FO CSV' parameter.
    Parameters:

        <output> : String   | output string from the windows 'systeminfo' command.
    '''

    try:
        output = output.split('\r\n')   # Separate the list on ['"header1","header2,...",'"value1","value2","...."'] string
        headers = output[0].split('","')  # Get the headers list

        values = output[1].split('","')   # Get the values list

        # get the info related to physical memory, We need to convert the size to numbers so the comma and MB string need to be removed

        results = [(headers[i],values[i].replace(' MB','').replace(',','')) for i in xrange(len(headers)) if (headers[i].lower().find("memory") != -1 and headers[i].lower().find("physical") != -1)]

        table = {'mem':dict()}         # create the result table using the required data

        for k,v in results:

            if k.lower().find('total') == -1:
                # save free memory value
                table['mem']['free'] = v
            else:
                # save total memory value
                table['mem']['total'] = v

        # calculate used memory using the total and free memory information
        table['mem']['used'] = int(table['mem']['total']) - int(table['mem']['free'])

        return table

    except Exception as e:

        raise Exception("\nError parsing windows output\n\t Details: " + str(e))

def Parse_Output(output, platform, path,filename):
    '''
    Description: Excecutes linux 'free -m' bash command and parses the output to collect the needed data.
    Then it will write the data on a file with the given <filename> to the local OS given <path>.
    Parameters:

        <output>    : STRING | The string containing the string to parse.
        <platform>  : STRING | The OS platform name.
        <filename>  : STRING | The filename that will contain the memory information.
        <path>      : STRING | The path were the memory information will be saved.
    '''

    global table

    try:

        print "Parsing output ..."

        if platform.startswith('linux'): # linux platform 'free -m' bash command parse

            table = Parse_Linux(output)

        else: # window platfrom 'systeminfo /FO CSV' command parse

            table = Parse_Windows(output)

        if table:
            Write_File(table,path,filename)

    except Exception as e:
        raise Exception("\nError parsing command output\n\t Details:" + str(e))

def Write_File(table, path, filename):
    '''
        Description :
            Write file to the given path.

        Parameters :
            <table> Dictionary | Contains the data to write to the file.
            <path> String | Valid OS path to store the file.
            <filename> String | The name of the file to store the results.
    '''

    try:

        print "Writing results..."

        results = """Results:
        \t1. Total system memory : %s MB
        \t2. Total system memory in use : %s MB
        \t3. Total system memory available : %s MB\n""" % (table['mem']['total'], table['mem']['used'], table['mem']['free'])

        f = open(os.path.join(path,filename),'w')
        f.write(results)
        f.close()

        print "The results have been saved on %s" % os.path.join(path,filename)

    except Exception as e:

        raise Exception("\nError saving the file\n\t Details: " + str(e))

def Get_Path():
    '''
        Description :
        Returns the path where the results will be saved.
    '''
    try:
        path = ""
        if len(sys.argv) == 3 and sys.argv[1].lower() == "-p":
            #User has provided an output path
            path = os.path.normpath(sys.argv[2])

        else:
            #Set default output path
            path = os.path.expanduser('~')

        if os.path.isdir(path) : # if path is a directory

            return path # return the path

        else:

            raise Exception # else raise Exception

    except Exception as e:

        print "The was an error getting the output path. The current working directory has been set as output path"

        return os.getcwd() # on Exception return current working directory as output path

def main():
    '''
        Description: Main function
    '''

    #Show help
    if len(sys.argv) == 2 or len(sys.argv) > 3:
        # If 2 arguments recieved and -help flag is given
        Print_Help()
        return 0
    elif len(sys.argv) == 3:
        # If three arguments are recived and the second argument is not the -p flag
        if sys.argv[1].lower() != "-p":
            Print_Help()
            return 0

    PLATFORM =  sys.platform     #Get the platform name

    PATH = Get_Path() # Get the path

    FILENAME = datetime.datetime.now().strftime("memory-output %Y-%m-%d %I-%M-%S%p.txt") # add the timestamp to the filename



    if PLATFORM.startswith('linux'):
        Exc_Command(command=['free', '--mega'], platform = PLATFORM, path = PATH, filename = FILENAME) # excecute linux 'free --mega' command

    elif PLATFORM.startswith('win'):
        Exc_Command(command=['systeminfo', '/FO', 'CSV'], platform = PLATFORM, path = PATH, filename = FILENAME) # excecute windows  'systeminfo /FO CSV' command

    else:
        # Display platform error message
        return
        """
        Error: Invalid platform

        Supported platform are linux and windows.
        Current: %s
        """ % PLATFORM

    return 0

if __name__ == "__main__":
    sys.exit(main())
