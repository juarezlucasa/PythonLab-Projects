var copy = require('copy-dynamodb-table').copy

var globalAWSConfig = { // AWS Configuration object http://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Config.html#constructor-property
  accessKeyId: 'ASIAW6N4AK4NK7UWEAIB',
  secretAccessKey: 'WgHh/f7yrqdqgouXlS1worf+BQbeDLkCqXQ+PblB',
  sessionToken: 'FwoGZXIvYXdzEPD//////////wEaDPFh+tm3XdV581oSASKGAYfkbvzlUMd9usXABTmSo5D6tRNlxmIZbzXfOK2XAZbiB+Dnwwo9n1TxL74gsDquTdd6yB9A5oAyO6fJIZfgiq3ujONyI1dTGqz+yM2fapX3U77OBnAmhll/txjWrNv5O74UP2mZl/oEzxpNU0Dh7i6EBtAJ3xyWhUQa+AYcleKOynlnX+2mKOK6oJoGMii8ZtkTrhLBr+4Ms1YPOhLafAsYTc83CCtJ4DNfEGa3jfy+/w6JlPNM',
  region: 'us-east-1'
}

copy({
  config: globalAWSConfig, // config for AWS
  source: {
    tableName: 'CL00059-FraudMonitoring-Parameters-DEV', // required
  },
  destination: {
    tableName: 'CL00059-FraudMonitoring-Parameters-Global-DEV', // required
  },
  log: true, // default false
  create: true // create destination table if not exist
},
  function (err, result) {
    if (err) {
      console.log(err)
    }
    console.log(result)
  })
