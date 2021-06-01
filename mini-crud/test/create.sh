
URL=$1
[ -z $URL ] && { echo "Error: URL not found"; exit 3; }

API=$1
DT=$(date +'%F %T')
JS='{"name":"Mini Mongo","mobile":"0412345678","email":"mini.mongo@mail.com","gender":"Female","created":"'$DT'"}'
curl -s -H 'Content-Type: application/json' -X POST \
    -d "$JS" \
    "$API"
