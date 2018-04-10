'use strict'

/*
*  Modify this file as needed.
*/

const http = require('http')
const fs = require('fs')
const zlib = require('zlib')
const BENCHMARK_PATH_COMPRESSION = './benchmark_compression.log'
const BENCHMARK_PATH_NO_COMPRESSION = './benchmark_no_compression.log'
const PORT = 8080
let bytesRead = 0
let requestCount = 0

process.on('SIGTERM', function() {
  if (process.argv[2]==='nocompress'){
    fs.writeFileSync(BENCHMARK_PATH_NO_COMPRESSION, `Performance using no compression || Bytes read: ${bytesRead}. Request count: ${requestCount}\n`);
  }
  else{
    fs.writeFileSync(BENCHMARK_PATH_COMPRESSION, `Performance using compression || Bytes read: ${bytesRead}. Request count: ${requestCount}\n`); 
  }
  process.exit(0)
})

const server = http.createServer(function(req, res) {
  let body = []
  requestCount += 1
  req.on('data', (data) => {
  	body.push(data)
  })
  req.on('end', () => {
  	if (req.headers['content-encoding']==='gzip'){
      bytesRead += req.socket.bytesRead
  		zlib.gunzip(Buffer.concat(body), (err, msg) => {
  			if (err){
  				res.statusCode = 400
  				res.write(JSON.stringify(err))
	    		res.end()	
  			}
  			else{
  				console.log(msg.toString())
	    		res.end()
  			}
	    })
  	}
  	else{
      bytesRead += req.socket.bytesRead
  		console.log(Buffer.concat(body).toString())
    	res.end()
  	}
  })
})

server.listen(PORT)