# AgileTrailblazers
This is a server for solving the Longest Common Substring (LCS) problem.

To setup the server run the shell script contained in the repo on the linux command line with sudo. 'sudo ./trailblaze_setup.sh'

This will setup a location for the flask file, create a virtual environment, install dependencies (flask, gevent), and run the server.

To test various outcomes, the curl command can be used as follows:

curl --header "Content-Type: application/json" --request POST --data '{"setOfStrings" : [ {"value":"chcast"}, {"value":"chromecastic"}, {"value":"broadcaster"}]}' http://localhost:5000/lcs
