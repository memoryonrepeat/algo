const MongoClient = require('mongodb').MongoClient;
const DB_NAME = 'testdb';
const COLLECTION_NAME = 'transactions';
const MINIMUM_CONFIRMATIONS = 6;
const URL = `mongodb://mongo:27017/${DB_NAME}`;
const KNOWN_ADDRESSES = {
  'mvd6qFeVkqH6MNAS2Y2cLifbdaX5XUkbZJ': 'Wesley Crusher',
  'mmFFG4jqAtw9MoCC88hw5FNfreQWuEHADp': 'Leonard McCoy',
  'mzzg8fvHXydKs8j9D2a8t7KpSXpGgAnk4n': 'Jonathan Archer',
  '2N1SP7r92ZZJvYKG2oNtzPwYnzw62up7mTo': 'Jadzia Dax',
  'mutrAf4usv3HKNdpLwVD4ow2oLArL6Rez8': 'Montgomery Scott',
  'miTHhiX3iFhVnAEecLjybxvV5g8mKYTtnM': 'James T. Kirk',
  'mvcyJMiAcSXKAEsQxbW9TYZ369rsMG6rVV': 'Spock',
};

function initDB() {
  MongoClient.connect(URL, (err, client) => {
    if (err) {
      return console.log(err);
    }
    const collection = client.db(DB_NAME).collection(COLLECTION_NAME);
    const transactions = JSON.parse(require('fs').readFileSync('txs.json')).transactions;

    // Clear the collection before importing to avoid any duplicate
    collection.remove({}, (err, success) => {
      if (err) {
        return console.log(err);
      }
      collection.insertMany(transactions, (err, result) => {
        if (err) {
          return console.log(err);
        }
        filterTransactions(collection, () => {
          client.close();
        });
      });
    });
  });
};

function filterTransactions(collection, callback) {
  collection.find({
    confirmations: {
      $gte: MINIMUM_CONFIRMATIONS,
    },
    amount: {
      $gte: 0
    }
  }, (err, cursor) => {
  	if (err) {
      console.log(err);
      return callback();
  	}
    var result = {
      smallest: Number.MAX_VALUE,
      largest: Number.MIN_VALUE,
    };

    // Using forEach for cursor to stream partial results
    // instead of using toArray to store the whole result
    // in RAM which is more memory consuming.
    cursor.forEach((tx) => {
      updateResult(result, tx);
    }, (err) => {
      if (err) {
        console.log(err);
        return callback();
      }
      console.log(mapResult(result));
      callback();
    });
  });
};

function updateResult(result, tx) {
  var processedTransaction = {
    amount: tx.amount,
    address: (tx.address in KNOWN_ADDRESSES) ? tx.address : 'unknown',
  };
  if (!result.hasOwnProperty(processedTransaction.address)) {
    result[processedTransaction.address] = {
      sum: processedTransaction.amount,
      count: 1,
    };
  } else {
    result[processedTransaction.address].sum += processedTransaction.amount;
    result[processedTransaction.address].count += 1;
  }
  result.smallest = Math.min(processedTransaction.amount, result.smallest);
  result.largest = Math.max(processedTransaction.amount, result.largest);
};

function mapResult(result) {
  return `Deposited for Wesley Crusher: count=${result['mvd6qFeVkqH6MNAS2Y2cLifbdaX5XUkbZJ'].count} sum=${result['mvd6qFeVkqH6MNAS2Y2cLifbdaX5XUkbZJ'].sum}
Deposited for Leonard McCoy: count=${result['mmFFG4jqAtw9MoCC88hw5FNfreQWuEHADp'].count} sum=${result['mmFFG4jqAtw9MoCC88hw5FNfreQWuEHADp'].sum}
Deposited for Jonathan Archer: count=${result['mzzg8fvHXydKs8j9D2a8t7KpSXpGgAnk4n'].count} sum=${result['mzzg8fvHXydKs8j9D2a8t7KpSXpGgAnk4n'].sum}
Deposited for Jadzia Dax: count=${result['2N1SP7r92ZZJvYKG2oNtzPwYnzw62up7mTo'].count} sum=${result['2N1SP7r92ZZJvYKG2oNtzPwYnzw62up7mTo'].sum}
Deposited for Montgomery Scott: count=${result['mutrAf4usv3HKNdpLwVD4ow2oLArL6Rez8'].count} sum=${result['mutrAf4usv3HKNdpLwVD4ow2oLArL6Rez8'].sum}
Deposited for James T. Kirk: count=${result['miTHhiX3iFhVnAEecLjybxvV5g8mKYTtnM'].count} sum=${result['miTHhiX3iFhVnAEecLjybxvV5g8mKYTtnM'].sum}
Deposited for Spock: count=${result['mvcyJMiAcSXKAEsQxbW9TYZ369rsMG6rVV'].count} sum=${result['mvcyJMiAcSXKAEsQxbW9TYZ369rsMG6rVV'].sum}
Deposited without reference: count=${result['unknown'].count} sum=${result['unknown'].sum}
Smallest valid deposit: ${result.smallest}
Largest valid deposit: ${result.largest}`;
}

initDB();
