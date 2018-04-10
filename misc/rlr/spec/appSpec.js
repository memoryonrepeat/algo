let assert = require('assert')
let mockObject = {"deviceId":"9bde4d3e-dfc7-4b31-90bc-9032961793c0","readings":[{"path":"","meaning":"humidity","value":24.012}],"received":1479907316977}
let mockArray = [{"bn":"amb1/modbus/etima-strom/","bt":1480001428.655},{"n":"V a-n","v":230.5494384765625,"u":"V"},{"n":"V b-n","v":230.12722778320312,"u":"V"},{"n":"V c-n","v":230.29534912109375,"u":"V"},{"n":"I a","v":24.63257598876953,"u":"A"},{"n":"I b","v":25.195981979370117,"u":"A"},{"n":"I c","v":23.139299392700195,"u":"A"},{"n":"P a","v":5462.740234375,"u":"W"},{"n":"P b","v":5624.10302734375,"u":"W"},{"n":"P c","v":5121.3876953125,"u":"W"},{"n":"MP a","v":13727.556640625,"u":"W"},{"n":"MP b","v":14837.0654296875,"u":"W"},{"n":"MP c","v":13078.4951171875,"u":"W"}]
let mockString = 'The quick brown fox jumps over the lazy dog'
let client = require('../sender/transmit')
let request = require('request')
let server

describe('App', () => {

  describe('Client', () => {

    describe('#compressThenSend()', () => {

      it('should compress and send object successfully', (done) => {
        client.compressThenSend(mockObject, (err,res) => {
          assert.equal(err,null)
          done()
        })
      })

      it('should compress and send array successfully', (done) => {
        client.compressThenSend(mockArray, (err,res) => {
          assert.equal(err,null)
          done()
        })
      })

      it('should compress and send string successfully', (done) => {
        client.compressThenSend(mockString, (err,res) => {
          assert.equal(err,null)
          done()
        })
      })

    })

    describe('#sendAsIs()', () => {

      it('should send non-compressed object successfully', (done) => {
        client.sendAsIs(mockObject, (err,res) => {
          assert.equal(err,null)
          done()
        })
      })

      it('should send non-compressed array successfully', (done) => {
        client.sendAsIs(mockArray, (err,res) => {
          assert.equal(err,null)
          done()
        })
      })

      it('should send non-compressed string successfully', (done) => {
        client.sendAsIs(mockString, (err,res) => {
          assert.equal(err,null)
          done()
        })
      })

    })

  })

  describe('Server', () => {

      it('should fail to decompress non-compressed messages', (done) => {

        request({
          method: 'POST',
          url: client.URL,
          json: true,
          headers: {
            'Content-Encoding': 'gzip'
          },
          body: mockString,
        }, (err, res, body) => {
          assert.notEqual(res.statusCode, 200)
          done()
        })

      })

  })

});
