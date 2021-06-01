
URL=$1
ID=$2

[ -z $URL ] && { echo "Error: URL not found"; exit 3; }
[ -z $ID ] && { echo "Error: ID not found"; exit 3; }

curl -s -X DELETE "$1$2"
