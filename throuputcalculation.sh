echo -n "Input ThroughPut = "
cat SecureFastChatlogs_* |grep Rec | cut -d ':' -f 1| awk '{if($1>_____ && $1 < _____){print($1)}}' | wc -l
echo -n "Output ThroughPut = "
cat SecureFastChatlogs_* |grep Sent | cut -d ':' -f 1| awk '{if($1>_____ && $1 < _____){print($1)}}' | wc -l
