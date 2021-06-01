
URL=$1
ID=$2
[ -z $URL ] && { echo "Error: URL not found"; exit 3; }
[ -z $ID ] && { echo "Error: ID not found"; exit 3; }

API=$1$2
DT=$(date +'%F %T')
JS='{"name":"Mini Banana","mobile":"04133888666","email":"mini.banana@mail.com","gender":"Male","update":"'$DT'"}'
curl -s -H 'Content-Type: application/json' -X PUT \
    -d "$JS" \
    "$API"
