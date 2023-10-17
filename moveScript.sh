# !/bin/sh
echo "Script name: $0"
mkdir "$1";
echo "New directory: $1"
echo "Command to do: $2"
echo "File type to do command on: $3"
echo "The complete list of arguments is $@"
echo "Total Number of Parameters: $#"
echo "The process ID is $$"

yourfilenames=`ls *$3`
for eachfile in $yourfilenames
do
   $2 $eachfile $1
   echo "Command executed: $2 $eachfile $1"
done
echo "Exit code for $0: $?"
