var xmlrpc = require('xmlrpc');

setTimeout(function () {
	// Creates an XML-RPC client. Passes the host information on where to
	// make the XML-RPC calls.
	var client = xmlrpc.createClient({ host: 'localhost', port: 9000, path: '/'})
   
	// Sends a method call to the XML-RPC server
	// client.methodCall('anAction', ['aParam'], function (error, value) {
	//   // Results of the method response
	//   console.log('Method response for \'anAction\': ' + value)
	// })

	client.methodCall('hello', [], function (error, value) {
	  // Results of the method response
	  console.log('Method response for \'hello\': ' + value)
	})
   
  }, 1000)