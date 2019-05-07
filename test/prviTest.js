var zahteva = require('supertest')
var streznik = require('streznik.js')


describe('Začetna stran', function() {
  it ('Prikaži besedilo "Testiramo teste ..."', function(done) {
    zahteva(streznik).get('/').expect(/<h1>Prvi test?<\/h1>/i, done);
  });
});