var express = require('express');
var streznik = express();
var port = process.env.PORT || 3000;


/**
 * Ko uporabnik obišče začetno stran,
 * izpiši začetni pozdrav
 */
streznik.get('/', function (zahteva, odgovor) {
  odgovor.send(
    '<h1>Prvi test?</h1>'
  );
});


/**
 * Poženi strežnik
 */
streznik.listen(port, function () {
  console.log('Strežnik je pognan na portu ' + port + '!');
});


module.exports = streznik;