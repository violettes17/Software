exports.hello = function(event, callback) {
	console.log("event", event);

	var name = event.data;
	if ( name == "" ) {
		name = "World"
	}

	callback(null, "Hello " + name + " from OVH Functions!")
}