#!/bin/sh
touch benchmark_compression.log
touch benchmark_no_compression.log
echo 'Benchmark started... Hold on for one or two minutes'
echo 'Testing using compression algorithm'
node ./receiver/index compress > received_event_stream.log & RECEIVER_PID=$!
cat sample_event_stream.log | node ./sender/index compress
kill -15 $RECEIVER_PID
sort sample_event_stream.log > sample_event_stream.log.sort
sort received_event_stream.log  > received_event_stream.log.sort
DIFF=$(diff received_event_stream.log.sort sample_event_stream.log.sort)
if [ -z "$DIFF" ];
  then
  echo 'All events were successfully transferred using compression'
  else
  echo 'Failed, the received event dump does not match the sample input in compression mode!'
fi

echo 'Testing using no compression algorithm'
node ./receiver/index nocompress > received_event_stream.log & RECEIVER_PID=$!
cat sample_event_stream.log | node ./sender/index nocompress
sort received_event_stream.log  > received_event_stream.log.sort
kill -15 $RECEIVER_PID
DIFF=$(diff received_event_stream.log.sort sample_event_stream.log.sort)
if [ -z "$DIFF" ];
  then
  echo 'All events were successfully transferred without compression'
  else
  echo 'Failed, the received event dump does not match the sample input in non-compression mode!'
fi
cat benchmark_compression.log
cat benchmark_no_compression.log
