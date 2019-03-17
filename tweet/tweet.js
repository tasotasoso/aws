var twitter = require('twitter');

var bot = new twitter({
    consumer_key        : ' ',
      consumer_secret     : ' ',
        access_token_key    : ' ',
          access_token_secret : ' '
});
bot.post('statuses/update', {status: 'tweet from lambda'}, function(error, tweet, response){
if (!error) {
console.log(tweet);
    } else {
console.log('error');
    }
});