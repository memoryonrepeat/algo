-------------------------------------
# How to run and test
- The system was optimized by using gzip to compress the message on client side and decompress on server side. For testing purpose, if the 'content-encoding' header is not specified as gzip, the message is sent without compression.
- To install the dependencies, run `npm install`
- Unit tests were written in Jasmine. To run, first start the server by running `node receiver/index.js` on a terminal window. Then on another terminal window, run `npm test` to start the tests. Test can be seen in the /spec folder.
- To easily compare the performance before/after optimization, I have made a script to benchmark. Just run `./benchmark.sh` to see the result. For the given event stream set, number of bytes transferred was reduced by more than 30% (83928 bytes using compression vs 120505 using no compression).
-------------------------------------
# Backend Test - Node.js

This is a framework for building a simple client and server in Node.js.  

## Objectives

The purpose of completing this test is to show us how you approach and solve a problem.  Ideally
you should not spend more than 2-3 hours on this.

- **State your assumptions.**  Anywhere you feel that the requirements are unclear please make
an assumption and document that assumption.
- **Describe Trade-offs.** When you're making a decision about using one design/approach vs. another
try to make a quick note about why you made the choice you did.
- **Provide tests.**  You should provide unit tests for the code that you write.  The choice of
testing tools is up to you.


## Requirements

This system simulates a client sending sensor readings to a remote server.  We would like you
to imagine that the client and server are separated by a connection with limited bandwidth.  Please
make an effort to minimize the number of bytes being sent between the client and server.  Messages
don't need to be received in real-time, but try to keep latency below 2 seconds for any given
message.

Please keep in mind that we are much more interested in seeing a well-designed and well-tested
solution than we are in getting the absolute best data compression.  

You are being provided with a basic framework of both the client and server.  It includes a sample
implementation using HTTP POSTs.  The example works, but we think you can do better!  Modify or
replace the provided implementation.  (Don't modify the existing file-reading and event emitting
logic.)

### Client

The provided code will read the sensor readings from a file and provide them at random intervals
(between 0 and 1000ms).  You job is to handle these messages and send them in an efficient manner
to the server.  Make your changes in the `sender/transmit.js` file.

### Server

Please print the received messages to `STDOUT` as in the example.  If you have other things you want
to output please use `STDERR`.

Make your changes in the `receiver/index.js` file.

## Test Script

We have provided a `bash` script for doing acceptance testing.  It will run both the client and
server.  It captures the output of the server, sorts it and then compares it to the input.  If they
are the same the test passes.  This should help to evaluate your solution.
