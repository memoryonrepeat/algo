'use strict'

const request = require('request')
const zlib = require('zlib')
const URL = 'http://localhost:8080/'

// Function to compress the message using zlib before sending
function compressThenSend(eventMsg, callback){
	zlib.gzip(JSON.stringify(eventMsg), {
	  	level: zlib.constants.Z_BEST_COMPRESSION,
	  	strategy: zlib.constants.Z_FILTERED
	  }, (err, compressedMsg) => {
	  	request({
		  method: 'POST',
		  url: URL,
		  body: compressedMsg,
		  headers: {
		  	'Content-Encoding': 'gzip'
		  }
		}, (err, res, body) => {
			if (err){
				return callback(err)
			}
			if (res.statusCode !== 200){
				return callback(body)	
			}
			return callback(null)
		 })
	  })
}

// Original function without compression
function sendAsIs(eventMsg, callback){
	request({
	  	method: 'POST',
	  	url: URL,
	  	json: true,
	  	body: eventMsg,
	  }, (err, res, body) => {
		callback(err)
	  })
}

/*
*  This function will be called for each event.  (eg: for each sensor reading)
*  Modify it as needed.
*/
module.exports = function(eventMsg, encoding, callback) {
  
  /*
  * NOTE: 
  * Due to the nature of the problem which is sending sensor logs for server to proceed later, 
  * I assume that these logs will be put to a message broker to process later, 
  * therefore real-time update is not as important as compression quality,
  * so i decided to trade off compression speed to get the best compression possible.
  *
  * Also, after benchmarking with all existing strategies, I see that the default compression strategy 
  * does not give as good compression ratio as Z_FILTERED, so I switched to using Z_FILTERED.
  *
  * Lastly, I can also imagine doing message queuing on client side to maximize the compression
  * performance, but since the README already put a latency constraint of 2 seconds for any message and 
  * there is a random delay between 0 to 1 second for any message, which means in worst case where the delay
  * comes close to 1 second, I can only bundle 2 messages for compression, which likely won't improve much
  * so I decided to skip it.
  */
  if (process.argv[2]==='nocompress'){
  	sendAsIs(eventMsg, callback)
  }
  else {
  	compressThenSend(eventMsg, callback)
  }

  /*
  * To test using the original function, comment out compressThenSend then call sendAsIs instead
  */
  // sendAsIs(eventMsg, callback)

}

module.exports.compressThenSend = compressThenSend
module.exports.sendAsIs = sendAsIs
module.exports.URL = URL
